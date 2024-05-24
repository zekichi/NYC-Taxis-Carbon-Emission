import mysql.connector
from datetime import date
import logging
import requests
from io import BytesIO
import pandas as pd

def get_last_inserted_date(db_params):
    try:
        # Conectarse a MySQL
        conn = mysql.connector.connect(**db_params)

        # Crear un cursor
        cursor = conn.cursor()

        # Consultar la última fecha insertada en la tabla auditoria
        query = "SELECT MAX(ultima_carga_datos) FROM auditoria"
        cursor.execute(query)
        last_inserted_date = cursor.fetchone()[0]

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

        # Si hay una fecha insertada, devolverla
        if last_inserted_date:
            return last_inserted_date
        else:
            # Si no hay fecha insertada, devolver '2020-01-01'
            return date(2020, 1, 1)

    except Exception as e:
        print("Error:", e)

def insert_current_date(db_params):
    try:
        # Conectarse a MySQL
        conn = mysql.connector.connect(**db_params)

        # Crear un cursor
        cursor = conn.cursor()

        # Insertar la fecha actual en la tabla auditoria
        query = "INSERT INTO auditoria (ultima_carga_datos) VALUES (%s)"
        current_date = date.today()
        cursor.execute(query, (current_date,))

        # Confirmar la transacción
        conn.commit()

        print("Fecha actual insertada en la tabla auditoria.")

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error:", e)


def check_database_and_tables(db_params):
    try:
        # Conectarse a MySQL
        conn = mysql.connector.connect(**db_params)

        # Crear un cursor
        cursor = conn.cursor()

        # Verificar si la base de datos existe
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]
        if db_params['database'] in databases:
            print(f"La base de datos '{db_params['database']}' existe.")
            # Verificar si la base de datos tiene tablas
            cursor.execute(f"USE {db_params['database']}")
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                print(f"La base de datos '{db_params['database']}' tiene las siguientes tablas:")
                i=0
                for table in tables:
                    i += 1
                    print(f"Tabla: {i} ------ {table[0]}")
                            # Cerrar cursor y conexión
                cursor.close()
                conn.close()
                return True    
            else:
                print(f"La base de datos '{db_params['database']}' no tiene tablas.")
                        # Cerrar cursor y conexión
                cursor.close()
                conn.close()
                return False
        else:
            print(f"La base de datos '{db_params['database']}' no existe.")
                    # Cerrar cursor y conexión
            cursor.close()
            conn.close()
            return False



    except Exception as e:
        print("Error:", e)
        return False
    


# Fuente de datos:  Web Scrapping
def descargar_y_procesar_parquet(color, año, mes, db_params):
    # Construye la URL a partir del anio mes y color del taxi
    try:
        # Construir la URL del archivo parquet
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{color}_tripdata_{año}-{mes:02}.parquet"
        
        # Descargar el archivo parquet
        responsePARQUET = requests.get(url)
        responsePARQUET.raise_for_status()  # Levanta una excepción para errores HTTP
        parquet_content = BytesIO(responsePARQUET.content)   
        # Construye un Dataframe para manipular los datos    
        df = pd.read_parquet(parquet_content)  

        if color == "yellow":
            # Transformaciones en el Dataframe
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime']) 
            df['Month'] = df['tpep_pickup_datetime'].dt.month
            df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
            #Filtros del Dataframe
            carreras_por_locacion = df.groupby('PULocationID').size().reset_index(name='conteo_Carreras')
            ingreso_por_mes_por_locacion = df.groupby(['Month', 'PULocationID'])['total_amount'].sum().reset_index()
            conteo_de_horas = df.groupby(['PULocationID', 'pickup_hour']).size().reset_index(name='conteo_carreras')
            horas_laborales = df[(df['pickup_hour'] >= 7) & (df['pickup_hour'] <= 22) & (df['trip_distance'] > 0)]
            suma_de_distancia_en_horas_laborales = horas_laborales['trip_distance'].sum()
            total_de_viajes = len(horas_laborales['trip_distance'])
            promedio_de_distancia_en_horas_laborales = suma_de_distancia_en_horas_laborales / total_de_viajes


        elif color == "green":
            #Transformaciones del Dataframe
            df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])             
            df['Month'] = df['lpep_pickup_datetime'].dt.month
            df['pickup_hour'] = df['lpep_pickup_datetime'].dt.hour
            # Filtros del Dataframe
            carreras_por_locacion = df.groupby('PULocationID').size().reset_index(name='conteo_Carreras')
            ingreso_por_mes_por_locacion = df.groupby(['Month', 'PULocationID'])['total_amount'].sum().reset_index()
            conteo_de_horas = df.groupby(['PULocationID', 'pickup_hour']).size().reset_index(name='conteo_carreras')
            horas_laborales = df[(df['pickup_hour'] >= 7) & (df['pickup_hour'] <= 22) & (df['trip_distance'] > 0)]
            promedio_de_distancia_en_horas_laborales = horas_laborales['trip_distance'].sum()

        # Establecer conexión con la base de datos
        with mysql.connector.connect(**db_params) as conn:
            with conn.cursor() as cursor:
                # Insertar los datos en la tabla 'carrerasporzonas'
                sql_carreras = '''INSERT INTO carrerasporzonas (anio, mes, PUlocationId, conteo_carreras, taxi_cab)
                                  VALUES (%s, %s, %s, %s, %s)'''
                values_carreras = [(int(año), int(mes), int(row['PULocationID']), int(row['conteo_Carreras']), color)
                                   for _, row in carreras_por_locacion.iterrows()]
                cursor.executemany(sql_carreras, values_carreras)

                # Insertar los datos en la tabla 'ingresosporzonas'
                sql_ingresos = '''INSERT INTO ingresosporzonas (anio, mes, PUlocationId, total_ingresos, taxi_cab)
                                  VALUES (%s, %s, %s, %s, %s)'''
                values_ingresos = [(int(año), int(mes), int(row['PULocationID']), int(row['total_amount']), color)
                                   for _, row in ingreso_por_mes_por_locacion.iterrows()]
                cursor.executemany(sql_ingresos, values_ingresos)


                # Insertar los datos en la tabla 'horaspicoporzonas'
                sql_horas = '''INSERT INTO horaspicoporzonas (anio, mes, PUlocationId, pickup_hour, conteo_carreras, taxi_cab)
                                  VALUES (%s, %s, %s, %s, %s, %s)'''
                values_horas = [(int(año), int(mes), int(row['PULocationID']), int(row['pickup_hour']), int(row['conteo_carreras']), color)
                                   for _, row in conteo_de_horas.iterrows()]
                cursor.executemany(sql_horas, values_horas)

                # Commit 
                conn.commit()


                # Insertar los datos en la tabla 'horaspicoporzonas'
                sql_distancia = '''INSERT INTO distanciarecorridoturnolaboral (distancia_recorrida, anio, mes, taxi_cab)
                                  VALUES (%s, %s, %s, %s)'''
                values_distancia = [(int(promedio_de_distancia_en_horas_laborales), int(año), int(mes), color)]
                                   
                cursor.executemany(sql_distancia, values_distancia)

                # Commit 
                conn.commit()

        return f"parquet {url} procesado con exito"
    
    except requests.RequestException as e:
        logging.error(f"Error al descargar el archivo parquet: {e}")
        return f"Error al descargar el archivo parquet: {e}"
    except mysql.connector.Error as e:
        logging.error(f"Error al conectar con la base de datos: {e}")
        return f"Error al conectar con la base de datos: {e}"
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        return f"Error inesperado: {e}"


