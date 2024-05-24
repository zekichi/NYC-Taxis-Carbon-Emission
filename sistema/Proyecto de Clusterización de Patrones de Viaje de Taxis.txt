# Proyecto de Clusterización de Patrones de Viaje de Taxis


## Descripción del Modelo


El modelo implementado es un modelo de **clusterización** aplicado a los datos de viajes de taxis. La clusterización es una técnica de aprendizaje no supervisado que agrupa datos en subconjuntos (clusters) de manera que los datos dentro de cada cluster son más similares entre sí que con los de otros clusters. Para este proyecto, utilizamos el algoritmo **K-Means**, uno de los métodos de clusterización más populares y eficaces.


**Pasos para construir el modelo:**


1. **Recolección y Preparación de Datos**:
   - Se obtuvieron datos de viajes de taxis, incluyendo duración del viaje, distancia, ID de ubicación de origen y destino, hora de recogida, cantidad de pasajeros, entre otros.
   - Los datos fueron limpiados y preprocesados para eliminar valores atípicos y manejar datos faltantes.


2. **Selección de Características**:
   - Se seleccionaron características relevantes como la duración del viaje, distancia, ID de ubicación de origen y destino, y la cantidad de pasajeros.


3. **Escalado de Datos**:
   - Los datos fueron escalados para asegurar que todas las características contribuyan de manera equitativa al modelo. Esto es importante porque el algoritmo K-Means es sensible a la escala de los datos.


4. **Aplicación del Algoritmo K-Means**:
   - Se aplicó el algoritmo K-Means para agrupar los viajes en diferentes clusters. El número de clusters se determinó utilizando el método del codo y la silueta para encontrar el número óptimo de clusters.


5. **Evaluación y Visualización**:
   - Los clusters resultantes se evaluaron y visualizaron para entender las características y patrones de cada grupo.


## Aplicaciones del Modelo para el Cliente


El modelo de clusterización ofrece varias ventajas y aplicaciones prácticas que pueden ser sumamente beneficiosas para la empresa del cliente:


1. **Optimización de Rutas y Logística**:
   - **Identificación de Puntos Calientes**: Los clusters pueden ayudar a identificar áreas con alta demanda de taxis, permitiendo una mejor distribución de los vehículos.
   - **Mejora en la Planificación de Rutas**: Conocer los patrones de viaje permite optimizar las rutas para reducir tiempos de espera y mejorar la eficiencia del servicio.


2. **Análisis de la Demanda**:
   - **Predicción de Picos de Demanda**: Analizar los patrones de uso en diferentes horas del día y días de la semana puede ayudar a predecir picos de demanda y ajustar la disponibilidad de taxis en consecuencia.
   - **Segmentación de Clientes**: Identificar diferentes segmentos de usuarios (por ejemplo, viajeros frecuentes vs. esporádicos) y personalizar las ofertas y servicios según sus necesidades.


3. **Marketing y Estrategias Comerciales**:
   - **Campañas Dirigidas**: Utilizar la información de los clusters para diseñar campañas de marketing específicas para diferentes grupos de usuarios.
   - **Programas de Fidelización**: Crear programas de fidelización basados en los patrones de uso identificados en los clusters.


4. **Mejora en la Experiencia del Cliente**:
   - **Servicios Personalizados**: Ofrecer servicios personalizados basados en los hábitos y preferencias de los clientes, como recomendaciones de rutas o descuentos específicos.
   - **Reducción de Tiempos de Espera**: Utilizar la información para reducir los tiempos de espera al posicionar taxis en lugares estratégicos según la demanda histórica.


5. **Análisis de Eficiencia Operacional**:
   - **Identificación de Ineficiencias**: Detectar patrones de viajes que indican ineficiencias, como viajes muy cortos o tiempos de espera prolongados.
   - **Optimización de Recursos**: Asignar recursos de manera más eficiente basándose en los patrones de uso y la demanda identificada.


## Ejemplos Prácticos de Uso


1. **Gestión de Flota**:
   - Una empresa puede utilizar los datos de clusterización para decidir dónde posicionar su flota de taxis durante diferentes momentos del día, maximizando la cobertura y minimizando el tiempo de espera para los clientes.


2. **Promociones y Descuentos**:
   - Basado en los clusters, una empresa puede lanzar promociones específicas para viajes en ciertas horas o rutas que históricamente tienen menor demanda, incentivando su uso y equilibrando la carga de trabajo.


3. **Mejora del Servicio en Áreas Clave**:
   - Identificar áreas con alta frecuencia de viajes puede ayudar a la empresa a mejorar la infraestructura de servicio en esas áreas, como estaciones de carga para vehículos eléctricos o áreas de espera para pasajeros.


4. **Previsión de Demanda en Eventos Especiales**:
   - Durante eventos especiales o días festivos, el análisis de clusters puede predecir la demanda adicional y permitir a la empresa prepararse adecuadamente, evitando escasez de taxis y mejorando la satisfacción del cliente.


5. **Evaluación de Nuevas Rutas**:
   - Si la empresa está considerando expandir sus servicios a nuevas áreas, los datos de clusterización pueden ofrecer insights sobre las áreas más prometedoras para la expansión basada en patrones de viaje similares en otras regiones.


## Conclusión


El modelo de clusterización proporciona una herramienta poderosa para entender y optimizar los patrones de viaje en el negocio de taxis. Al implementar este modelo, la empresa puede mejorar su eficiencia operativa, ofrecer servicios personalizados, y aumentar la satisfacción del cliente, lo que se traduce en un mayor valor agregado y competitividad en el mercado.


















# Instrucciones para el Usuario Final


## Requisitos del Sistema


- **Sistema Operativo**: Debian 12 o superior
- **Python**: Versión 3.7 o superior
- **Dependencias**: Listadas en el archivo `requirements.txt`


## Instalación


### Clonar el Repositorio


Primero, clona el repositorio del proyecto en tu máquina local:




git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio




## Entorno Virtual


Crea un entorno virtual para evitar conflictos de dependencias:


python3 -m venv env
source env/bin/activate


## Instalar las dependencias 


Instala las dependencias con este comando:


pip install -r requirements.txt


## Configuración de la Base de Datos


En el diccionario deberás ajustar los parámetros de configuración de tu base de datos de MySQL.


## Ejecución de la Aplicación


Para ejecutar la aplicación asegúrate de estar en el directorio raíz del proyecto y activa el entorno virtual, luego ejecuta:


streamlit run app.py


Esto iniciará la aplicación y abrirá una nueva pestaña en tú navegador predeterminado.




## Solución de Problemas


### Problemas Comunes


#### Problemas de Conexión a la Base de Datos:


- Verifica que el archivo `db_config.json` contiene la información correcta.
- Asegúrate de que la base de datos esté en funcionamiento y accesible.


#### Errores de Dependencias:


- Asegúrate de haber ejecutado `pip install -r requirements.txt` en el entorno virtual correcto.


#### Problemas de Carga en Streamlit:


- Asegúrate de estar ejecutando `streamlit run app.py` en el directorio correcto y con el entorno virtual activado.


### Contacto de Soporte


Si encuentras algún problema que no puedes resolver, por favor contacta al equipo de soporte técnico:


- **Correo Electrónico**: antomore353@hotmail.com
- **Teléfono**: +???????????