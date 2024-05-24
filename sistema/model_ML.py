import pandas as pd
import mysql.connector
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

# Datos para la conexión
db_config = {
    'user': 'antonio',
    'password': 'nueva_contraseña',
    'host': 'localhost',
    'database': 'taxis'
}

# Obtener los datos desde la base de datos
def get_data_from_db():
    connection = mysql.connector.connect(**db_config)
    query = """
    SELECT 
        v.trip_distance, 
        v.passenger_count,
        l1.PULocationID, 
        l2.DOLocationID, 
        t.pickup_datetime, 
        t.dropoff_datetime, 
        TIMESTAMPDIFF(MINUTE, t.pickup_datetime, t.dropoff_datetime) AS trip_duration
    FROM 
        Hecho_Viaje v
    JOIN 
        Dim_Locacion l1 ON v.locacion_inicio_id = l1.locacion_id
    JOIN 
        Dim_Locacion l2 ON v.locacion_fin_id = l2.locacion_id
    JOIN 
        Dim_Tiempo t ON v.tiempo_inicio_id = t.tiempo_id
    """
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Obtener los datos
df = get_data_from_db()
df['pickup_hour'] = pd.to_datetime(df['pickup_datetime']).dt.hour

# Seleccionar las características
features = ['trip_duration', 'trip_distance', 'PULocationID', 'DOLocationID', 'pickup_hour', 'passenger_count']
X = df[features]

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar el modelo KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X_scaled)

# Guardar el escalador y el modelo
with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)

with open('kmeans_model.pkl', 'wb') as file:
    pickle.dump(kmeans, file)
