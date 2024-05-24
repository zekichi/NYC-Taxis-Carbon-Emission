import streamlit as st
import pandas as pd
import mysql.connector
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import plotly.express as px

# Datos para la conexión 
db_config = {
    'user': 'antonio',
    'password': 'nueva_contraseña',
    'host': 'localhost',
    'database': 'taxis'
}

# Cargar los modelos entrenados
with open('kmeans_model.pkl', 'rb') as file:
    kmeans = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Obtener los datos desde la base de datos
@st.cache_data
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

# Función para predecir el cluster
def predict_cluster(new_data):
    new_data_scaled = scaler.transform(new_data)
    predicted_cluster = kmeans.predict(new_data_scaled)
    return predicted_cluster[0]

# Configurar la página de Streamlit
st.title("Taxi Trip Clustering")

# Cargar los datos
df = get_data_from_db()

# Mostrar una vista previa de los datos
st.write("Vista previa de los datos:", df.head())

# Calcular los clusters
df['pickup_hour'] = pd.to_datetime(df['pickup_datetime']).dt.hour
features = ['trip_duration', 'trip_distance', 'PULocationID', 'DOLocationID', 'pickup_hour', 'passenger_count']
df_scaled = scaler.transform(df[features])
df['cluster'] = kmeans.predict(df_scaled)

# Mostrar un resumen de los clusters
st.subheader("Resumen de Clusters")
cluster_summary = df.groupby('cluster')[features].mean().reset_index()
st.write(cluster_summary)

# Mostrar gráficos interactivos con Plotly
st.subheader("Distribución de Duración de Viajes por Cluster")
fig_duration = px.histogram(df, x='trip_duration', color='cluster', title='Distribución de Duración de Viajes por Cluster')
st.plotly_chart(fig_duration)

st.subheader("Distribución de Distancia de Viajes por Cluster")
fig_distance = px.histogram(df, x='trip_distance', color='cluster', title='Distribución de Distancia de Viajes por Cluster')
st.plotly_chart(fig_distance)

# Predicción de un nuevo viaje
st.subheader("Predecir el Cluster de un Nuevo Viaje")
trip_duration = st.number_input('Duración del Viaje (minutos)')
trip_distance = st.number_input('Distancia del Viaje (millas)')
PULocationID = st.number_input('ID de Ubicación de Recogida')
DOLocationID = st.number_input('ID de Ubicación de Destino')
pickup_hour = st.number_input('Hora de Recogida')
passenger_count = st.number_input('Cantidad de Pasajeros')

new_data = pd.DataFrame([[trip_duration, trip_distance, PULocationID, DOLocationID, pickup_hour, passenger_count]],
                        columns=features)

if st.button('Predecir Cluster'):
    cluster = predict_cluster(new_data)
    st.write(f'El viaje pertenece al cluster {cluster}')
