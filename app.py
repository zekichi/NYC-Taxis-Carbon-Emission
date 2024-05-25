import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Cargar el DataFrame desde el archivo parquet
df = pd.read_parquet('combined_data.parquet')
df_clean = df.dropna()

# Filtrar datos por el mes de enero de 2023
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df['year_month'] = df['lpep_pickup_datetime'].dt.to_period('M')
df_january_2023 = df[df['year_month'] == '2023-01']

# Calcular participación de mercado por tipo de pago para enero de 2023
payment_types = df_january_2023['payment_type'].unique()
market_share = []

for payment_type in payment_types:
    total_trips = df_january_2023[df_january_2023['payment_type'] == payment_type].shape[0]
    market_share.append(total_trips / df_january_2023.shape[0] * 100)

# Configuración de Streamlit para la página principal
st.title("Dashboard de KPI de Participación de Mercado")

# Mostrar la participación de mercado actual y la meta
total_viajes_empresa = 68231
total_viajes_mercado = 500000
participacion_actual = (total_viajes_empresa / total_viajes_mercado) * 100
meta_incremento = 20
participacion_objetivo = participacion_actual * (1 + meta_incremento / 100)

# Mostrar métricas en Streamlit
st.header("Participación de mercado actual y objetivo")
st.metric(label="Actual", value=f"{participacion_actual:.2f}%")
st.metric(label="Objetivo", value=f"{participacion_objetivo:.2f}%")

# Gráfico de barras para la participación de mercado actual vs. objetivo
fig1, ax1 = plt.subplots()
ax1.bar(["Actual", "Objetivo"], [participacion_actual, participacion_objetivo], color=["blue", "green"])
ax1.set_ylabel('Participación de mercado (%)')
ax1.set_title('Participación de Mercado Actual vs. Objetivo')
st.pyplot(fig1)

# Descripción adicional
st.markdown("""
### Descripción
La participación de mercado representa la cuota de mercado que EcoTransit controla en relación con el total disponible en su industria. 
En este caso, se ha calculado la participación de mercado actual y se ha establecido una meta de incremento del 20% en los próximos dos años.
""")

# Datos ficticios para la tendencia histórica (últimos 12 meses)
meses = pd.date_range(start='2022-01-01', periods=12, freq='MS')
participacion_historica = [12.5, 12.7, 13.0, 13.2, 13.5, 13.8, 14.0, 14.2, 14.5, 14.7, 15.0, 15.2]

# Gráfico de línea para la tendencia histórica
st.subheader('Tendencia Histórica de la Participación de Mercado')
fig2, ax2 = plt.subplots()
ax2.plot(meses, participacion_historica, marker='o', linestyle='-', color='b')
ax2.set_xlabel('Mes')
ax2.set_ylabel('Participación de mercado (%)')
ax2.set_title('Tendencia Histórica de la Participación de Mercado')
ax2.grid(True)
st.pyplot(fig2)

# Datos ficticios para la comparación con competidores
competidores = ['Competidor A', 'Competidor B', 'Competidor C']
participacion_competidores = [15.5, 12.8, 14.2]

# Gráfico de barras para la comparación con competidores
st.subheader('Comparación con Competidores')
fig3, ax3 = plt.subplots()
ax3.bar(competidores, participacion_competidores, color='orange')
ax3.bar(["ECOTRANSIT"], [participacion_actual], color='blue', alpha=0.6)
ax3.set_ylabel('Participación de mercado (%)')
ax3.set_title('Comparación de Participación de Mercado con Competidores')
ax3.legend(['Competidores', 'ECOTRANSIT'], loc='upper left')
st.pyplot(fig3)

# Descripción adicional para la comparación con competidores
st.markdown("""
### Comparación con Competidores
Este gráfico muestra cómo se compara la participación de mercado de ECOTRANSIT con otros competidores clave en la industria.
""")

# Mostrar tabla de datos (opcional, para ver los datos filtrados)
st.subheader('Datos Filtrados por Enero de 2023')
st.write(df_january_2023)

# Gráfico de torta para el conteo de VendorID
st.subheader('Gráfico de Torta para VendorID')
vendor_counts = df_january_2023['VendorID'].value_counts()
fig_vendor, ax_vendor = plt.subplots()
ax_vendor.pie(vendor_counts, labels=vendor_counts.index, autopct='%1.1f%%', startangle=90)
ax_vendor.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig_vendor)

# Filtrar las columnas numéricas
numeric_cols = df_january_2023.select_dtypes(include=['float64', 'int64']).columns

# Calcular la matriz de correlación
corr_matrix = df_january_2023[numeric_cols].corr()

# Crear la figura del heatmap
fig_corr, ax_corr = plt.subplots(figsize=(10, 8))  # Ajustar el tamaño de la figura
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, linewidths=.5, 
            annot_kws={"size": 10}, fmt=".2f", ax=ax_corr)  # Ajustar el tamaño de las anotaciones

# Rotar las etiquetas para mejorar la legibilidad
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Mostrar la figura en Streamlit
st.subheader('Matriz de Correlación')
st.pyplot(fig_corr)

# Descripción adicional
st.markdown("""
### Descripción
Este dashboard muestra un análisis exploratorio de datos utilizando Streamlit. 
Incluye un gráfico de torta para el conteo de VendorID y una matriz de correlación para variables numéricas.
""")

# Convert payment_types to a list of strings, filtering out NaN
payment_types = df_january_2023['payment_type'].dropna().astype(str).unique()

# Calculate market share
market_share = []

for payment_type in payment_types:
    total_trips = df_january_2023[df_january_2023['payment_type'] == float(payment_type)].shape[0]
    if total_trips == 0:
        market_share.append(0)
    else:
        market_share.append(total_trips / df_january_2023.shape[0] * 100)

    # Debugging prints
    print(f"Payment Type: {payment_type}, Total Trips: {total_trips}, Market Share: {market_share[-1]}")

# Plotting the bar chart
st.title("Análisis de Participación de Mercado por Tipo de Pago")
fig2, ax2 = plt.subplots()
ax2.bar(np.arange(len(payment_types)), market_share, color='skyblue')
ax2.set_xlabel('Tipo de Pago')
ax2.set_ylabel('Participación de mercado (%)')
ax2.set_title('Participación de Mercado por Tipo de Pago')
ax2.set_xticks(np.arange(len(payment_types)))  # Set ticks for all payment types
ax2.set_xticklabels(payment_types, rotation=45)  # Rotate labels for better readability

# Display the plot using Streamlit
st.pyplot(fig2)