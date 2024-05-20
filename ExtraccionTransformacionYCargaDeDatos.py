
import pandas as pd
import mysql.connector
import logging
import geopandas as gpd
from datetime import datetime, timedelta
import time
from sql.methods import insert_current_date, check_database_and_tables, descargar_y_procesar_parquet, get_last_inserted_date
#########################################
#  _______                                        _______                        ___                     _                      _ 
# (_______)        _                       _     (_______)                      / __)                   (_)                    | |
#  _____   _   _ _| |_  ____ _____  ____ _| |_       _  ____ _____ ____   ___ _| |__ ___   ____ ____     _       ___  _____  __| |
# |  ___) ( \ / |_   _)/ ___|____ |/ ___|_   _)     | |/ ___|____ |  _ \ /___|_   __) _ \ / ___)    \   | |     / _ \(____ |/ _  |
# | |_____ ) X (  | |_| |   / ___ ( (___  | |_      | | |   / ___ | | | |___ | | | | |_| | |   | | | |  | |____| |_| / ___ ( (_| |
# |_______|_/ \_)  \__)_|   \_____|\____)  \__)     |_|_|   \_____|_| |_(___/  |_|  \___/|_|   |_|_|_|  |_______)___/\_____|\____|
                                                                                                                                
# Descripcion:
# Este programa es el encargado de insertar toda la informacion al  DATALAKE 
# Lo hace desde diferentes origenes
# El primero es Web Scrapping
# El segundo son archivos estaticos


#Parametros de Conexion para una base de datos MYSQL 
# Es prerequisito haber corrido el Script de definicion de tablas

db_params = {
    'host': 'localhost',
    'database': 'nyctaxisdb',
    'user': 'root',
    'password': '12345'
}



#################################################################################
#  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
# ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#  ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
#      ▐░▌     ▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌
#      ▐░▌     ▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌
#      ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌
#      ▐░▌     ▐░▌   ▐░▌ ▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌
#      ▐░▌     ▐░▌    ▐░▌▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌
#  ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
# ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                              

# 
#   ___                        _           
#  / __| __ _ _ __ _ _ __ _ __(_)_ _  __ _ 
#  \__ \/ _| '_/ _` | '_ \ '_ \ | ' \/ _` |
#  |___/\__|_| \__,_| .__/ .__/_|_||_\__, |
#                   |_|  |_|         |___/ 
if check_database_and_tables(db_params):
    fecha_inicio = get_last_inserted_date(db_params)
    fecha_fin = datetime.now().date()
    
    color = "green"
    print("Pasó la validacion de base de datos") 
   
    while fecha_inicio <= fecha_fin:
        if(fecha_inicio == fecha_fin):
            break
        anio = fecha_inicio.year
        mes = fecha_inicio.month
        
        resultados = descargar_y_procesar_parquet(color, anio, mes, db_params)
        print(resultados)
        
        # Incrementar la fecha de inicio al siguiente mes
        if fecha_inicio.month == 12:
            siguiente_mes = fecha_inicio.replace(year=fecha_inicio.year + 1, month=1, day=1)
        else:
            siguiente_mes = fecha_inicio.replace(month=fecha_inicio.month + 1, day=1)
        
        fecha_inicio = siguiente_mes
        time.sleep(5)

else:
    print ("No pasa la validacion de base de datos")    

###################################################################################
#  ___    _        _   _        
#  | __|__| |_ __ _| |_(_)__ ___ 
#  | _|(_-<  _/ _` |  _| / _/ _ \
#  |___/__/\__\__,_|\__|_\__\___/
                               
# Fuente de Datos  Estaticos
gdf = gpd.read_file(r"DataSets\taxi_zones\taxi_zones.shp")
# Función para convertir la geometría a WKT
def wkt_from_geometry(geom):
    return geom.wkt
try:
            # Establecer conexión con la base de datos
    with mysql.connector.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            # Insertar los datos en la tabla 'zonas'
            sql = '''INSERT INTO zonas (zone, LocationID, borough, geometry)
                                VALUES (%s, %s, %s, ST_GeomFromText(%s))'''
            values = [(row['zone'], int(row['LocationID']), row['borough'], wkt_from_geometry(row['geometry']))
                      for _, row in gdf.iterrows()]
            cursor.executemany(sql, values)

            # Commit 
            conn.commit()
    print("Zonas insertadas con exito")

except mysql.connector.Error as e:
    logging.error(f"Error al conectar con la base de datos: {e}")
    print(f"Error al conectar con la base de datos: {e}") 
except Exception as e:
    logging.error(f"Error inesperado: {e}")
    print (f"Error inesperado: {e}")


# Fuente de Datos: Estatico

estaciones_carga = pd.read_csv(r"DataSets\Electric and Alternative Fuel Charging Stations.csv")
condados_ny = ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
estaciones_elec_ny = estaciones_carga[estaciones_carga['City'].isin(condados_ny) & (estaciones_carga["State"] == "NY") & (estaciones_carga['Fuel Type Code'] == 'ELEC')]
estaciones_elec_ny = estaciones_elec_ny.reset_index(drop=True).drop_duplicates()
conteo_de_estaciones_por_condado = estaciones_elec_ny["City"].value_counts()
conteo_de_estaciones_por_condado = pd.DataFrame(conteo_de_estaciones_por_condado)

# Reiniciar el índice y renombrar las columnas
conteo_de_estaciones_por_condado.reset_index(inplace=True)
conteo_de_estaciones_por_condado.columns = ['Ciudad', 'Total_Cargadores']

try:
            # Establecer conexión con la base de datos
    with mysql.connector.connect(**db_params) as conn:
        with conn.cursor() as cursor:
            # Insertar los datos en la tabla 'zonas'
            sql = '''INSERT INTO cargadoresporcondado (ciudad, total_cargadores)
                                VALUES (%s, %s)'''
            values = [(row['Ciudad'], int(row['Total_Cargadores']))
                                    for _, row in conteo_de_estaciones_por_condado.iterrows()]
            cursor.executemany(sql, values)

            # Commit 
            conn.commit()
    print("Cargoders por condado insertados con exito")

except mysql.connector.Error as e:
    logging.error(f"Error al conectar con la base de datos: {e}")
    print(f"Error al conectar con la base de datos: {e}") 
except Exception as e:
    logging.error(f"Error inesperado: {e}")
    print (f"Error inesperado: {e}")      
    


insert_current_date(db_params)

#https://drive.google.com/file/d/1GEDvDxx0nC6fEk7I77AfpDvSQleGTupz/view?usp=sharing
