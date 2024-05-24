from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta
import requests
import pyarrow.parquet as pq
import numpy as np

default_args = {
   'owner': 'airflow',
   'depends_on_past': False,
   'email_on_failure': False,
   'email_on_retry': False,
   'retries': 1,
   'retry_delay': timedelta(minutes=5),
}

def download_file(url, output_path):
   response = requests.get(url)
   with open(output_path, 'wb') as f:
       f.write(response.content)

def process_and_load_to_db(file_path):
    try:
        # Establecer conexión con la base de datos usando MySqlHook
        mysql_hook = MySqlHook(mysql_conn_id='MYSQL_DEFAULT2')
        engine = mysql_hook.get_sqlalchemy_engine()

        # Leer el archivo parquet usando pyarrow
        table = pq.read_table(file_path)
        data = table.to_pydict()

        # Reemplazar NaN por None y asegurarse de que todas las columnas necesarias existan
        required_columns = ['lpep_pickup_datetime', 'lpep_dropoff_datetime', 'PULocationID', 'DOLocationID',
                            'RatecodeID', 'payment_type', 'passenger_count', 'trip_distance', 'fare_amount', 'extra',
                            'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount',
                            'congestion_surcharge', 'airport_fee']
        for col in required_columns:
            if col not in data:
                data[col] = [None] * len(data[next(iter(data))])
            data[col] = [None if isinstance(x, float) and np.isnan(x) else x for x in data[col]]

        # Preparar y ejecutar las inserciones SQL
        connection = engine.connect()

        # Insertar datos en Dim_Tiempo y obtener los IDs generados
        tiempo_data = list(zip(data['lpep_pickup_datetime'], data['lpep_dropoff_datetime']))
        tiempo_data = list(set(tiempo_data))  # Eliminar duplicados
        tiempo_insert_query = "INSERT IGNORE INTO Dim_Tiempo (pickup_datetime, dropoff_datetime) VALUES (%s, %s)"
        connection.execute(tiempo_insert_query, tiempo_data)

        # Crear un diccionario para mapear las fechas con sus IDs generados
        tiempo_rows = connection.execute("SELECT tiempo_id, pickup_datetime, dropoff_datetime FROM Dim_Tiempo").fetchall()
        tiempo_id_map = {(row['pickup_datetime'], row['dropoff_datetime']): row['tiempo_id'] for row in tiempo_rows}

        # Insertar datos en Dim_Locacion y obtener los IDs generados
        locacion_data = list(zip(data['PULocationID'], data['DOLocationID']))
        locacion_data = list(set(locacion_data))  # Eliminar duplicados
        locacion_insert_query = "INSERT IGNORE INTO Dim_Locacion (PULocationID, DOLocationID) VALUES (%s, %s)"
        connection.execute(locacion_insert_query, locacion_data)

        # Crear un diccionario para mapear las locaciones con sus IDs generados
        locacion_rows = connection.execute("SELECT locacion_id, PULocationID, DOLocationID FROM Dim_Locacion").fetchall()
        locacion_id_map = {(row['PULocationID'], row['DOLocationID']): row['locacion_id'] for row in locacion_rows}

        # Insertar datos en Dim_Tarifa y obtener los IDs generados
        tarifa_data = list(zip(data['RatecodeID'], data['payment_type']))
        tarifa_data = list(set(tarifa_data))  # Eliminar duplicados
        tarifa_insert_query = "INSERT IGNORE INTO Dim_Tarifa (RatecodeID, payment_type) VALUES (%s, %s)"
        connection.execute(tarifa_insert_query, tarifa_data)

        # Crear un diccionario para mapear las tarifas con sus IDs generados
        tarifa_rows = connection.execute("SELECT tarifa_id, RatecodeID, payment_type FROM Dim_Tarifa").fetchall()
        tarifa_id_map = {(row['RatecodeID'], row['payment_type']): row['tarifa_id'] for row in tarifa_rows}

        # Insertar datos en Hecho_Viaje
        viaje_data = []
        for i in range(len(data['passenger_count'])):
            locacion_inicio = (data['PULocationID'][i], data['DOLocationID'][i])
            tiempo_inicio = (data['lpep_pickup_datetime'][i], data['lpep_dropoff_datetime'][i])
            tarifa = (data['RatecodeID'][i], data['payment_type'][i])

            # Verificar que los IDs existen en las tablas de dimensión
            if locacion_inicio not in locacion_id_map or tiempo_inicio not in tiempo_id_map or tarifa not in tarifa_id_map:
                continue  # O maneja este caso de forma adecuada

            viaje_data.append((
                locacion_id_map[locacion_inicio],  # locacion_inicio_id
                locacion_id_map[locacion_inicio],  # locacion_fin_id
                tiempo_id_map[tiempo_inicio],  # tiempo_inicio_id
                tiempo_id_map[tiempo_inicio],  # tiempo_fin_id
                data['passenger_count'][i],
                data['trip_distance'][i],
                tarifa_id_map[tarifa],  # tarifa_id
                data['fare_amount'][i],
                data['extra'][i],
                data['mta_tax'][i],
                data['tip_amount'][i],
                data['tolls_amount'][i],
                data['improvement_surcharge'][i],
                data['total_amount'][i],
                data['congestion_surcharge'][i],
                data['airport_fee'][i]
            ))

        connection.execute(
            """INSERT INTO Hecho_Viaje (locacion_inicio_id, locacion_fin_id, tiempo_inicio_id, tiempo_fin_id, passenger_count, trip_distance, tarifa_id, fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, congestion_surcharge, airport_fee)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            viaje_data
        )

        connection.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

with DAG(
    'process_green_taxi_data',
    default_args=default_args,
    description='A simple DAG to download, process, and load green taxi data',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 5, 17),
    catchup=False,
) as dag:

    download_task = PythonOperator(
        task_id='download_file',
        python_callable=download_file,
        op_kwargs={
            'url': 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2020-01.parquet',
            'output_path': '/home/antonio/Documentos/PF/scraping_download/green_tripdata_2020-01.parquet',
        },
    )

    process_and_load_task = PythonOperator(
        task_id='process_and_load_to_db',
        python_callable=process_and_load_to_db,
        op_kwargs={
            'file_path': '/home/antonio/Documentos/PF/scraping_download/green_tripdata_2020-01.parquet',
        },
    )

    download_task >> process_and_load_task