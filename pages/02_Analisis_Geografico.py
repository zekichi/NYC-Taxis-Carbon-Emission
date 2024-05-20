import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import geopandas as gpd

# Leer datos de estaciones de carga y condados de Nueva York
estaciones_carga = pd.read_csv("DataSets\Electric and Alternative Fuel Charging Stations.csv")
condados_ny = gpd.read_file("DataSets\Borough Boundaries.geojson")

# Filtrar estaciones de carga
estaciones_elec_ny = estaciones_carga[
    (estaciones_carga['City'].isin(condados_ny['boro_name'])) &
    (estaciones_carga['State'] == "NY") &
    (estaciones_carga['Fuel Type Code'] == 'ELEC')
].drop_duplicates(subset=['Latitude', 'Longitude'])

# Crear un mapa centrado en Nueva York
mapa_ny = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

# Diccionario de colores para cada condado
colores_condado = {
    'Bronx': 'blue',
    'Brooklyn': 'green',
    'Manhattan': 'red',
    'Queens': 'purple',
    'Staten Island': 'orange'
}

# Crear el MarkerCluster
marker_cluster = MarkerCluster().add_to(mapa_ny)

# Agregar los puntos de las estaciones de carga al MarkerCluster con colores específicos por condado
for _, row in estaciones_elec_ny.iterrows():
    condado = row['City']
    color = colores_condado.get(condado, 'gray')  # Asigna 'gray' si no se encuentra el condado en el diccionario
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Station Name'],
        icon=folium.Icon(color=color, icon='info-sign')
    ).add_to(marker_cluster)

# Función para definir el estilo de las fronteras
def estilo_frontera(feature):
    condado = feature['properties']['boro_name']  # Usar la clave correcta
    return {
        'fillColor': colores_condado.get(condado, 'gray'),
        'color': colores_condado.get(condado, 'gray'),
        'weight': 2,
        'fillOpacity': 0.1
    }

# Agregar las fronteras de los condados al mapa
folium.GeoJson(
    condados_ny,
    style_function=estilo_frontera,
    name='Fronteras de los Condados'
).add_to(mapa_ny)

# Agregar etiquetas de texto para los nombres de los condados
for _, row in condados_ny.iterrows():
    nombre_condado = row['boro_name']
    centroide = row['geometry'].centroid
    folium.Marker(
        location=[centroide.y, centroide.x],
        icon=folium.DivIcon(html=f"<div style='font-size: 14pt; color: black; font-weight: bold;'>{nombre_condado}</div>")
    ).add_to(mapa_ny)

# Agregar control de capas
folium.LayerControl().add_to(mapa_ny)

# Mostrar el mapa con Streamlit
st_folium(mapa_ny, width=725)
