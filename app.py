import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos conocidos
total_viajes_empresa = 68231
total_viajes_mercado = 500000  # Número estimado o conocido del mercado total

# Calcular la participación de mercado actual
participacion_actual = (total_viajes_empresa / total_viajes_mercado) * 100

# Meta de incremento en participación de mercado
meta_incremento = 20

# Calcular la nueva participación de mercado objetivo
participacion_objetivo = participacion_actual * (1 + meta_incremento / 100)

# Configuración de Streamlit
st.title("Dashboard de KPI de Participación de Mercado")

# Mostrar la participación de mercado actual
st.header("Participación de mercado actual")
st.metric(label="Actual", value=f"{participacion_actual:.2f}%")

# Mostrar la meta de participación de mercado
st.header("Meta de participación de mercado")
st.metric(label="Objetivo", value=f"{participacion_objetivo:.2f}%")

# Visualización adicional
fig, ax = plt.subplots()
ax.bar(["Actual", "Objetivo"], [participacion_actual, participacion_objetivo], color=["blue", "green"])
ax.set_ylabel('Participación de mercado (%)')
ax.set_title('Participación de Mercado Actual vs. Objetivo')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Mostrar una descripción adicional
st.markdown("""
### Descripción
La participación de mercado representa la cuota de mercado que EcoTransit controla en relación con el total disponible en su industria. 
En este caso, se ha calculado la participación de mercado actual y se ha establecido una meta de incremento del 20% en los próximos dos años.
""")
