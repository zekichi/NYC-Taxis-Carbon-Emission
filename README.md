
# Analítica Latam

En Analítica Latam nos especializamos en el analísis detallado, lo cuál nos permite evaluar la factibilidad financiera de proyectos, crear objetivos para un crecimiento y analizar a nuestra competencia. 
Comprometidos con la preservación del medio ambiente y el desarrollo sostenible.

Nos enfocamos en la impletementación de tecnologías avanzadas y modelos predictivos para la toma de decisiones informadas y atratégicas. Con un trabajo en equipo transparente y con un comunicación efectiva. Llevandolo a cabo con herramientas de visualización de datos para presentar información y análisis complejos de manera clara.

El equipo esta conformao por profesionales capacitados y especializados en áreas claves:
- 2 Data Analysts: Expertos en el análisis de datos, capaces de extraer insights significativos a partir de conjuntos de datos complejos.
- 2 Data Engineers: Especialistas en la gestión y procesamiento de grandes volúmenes de datos.
- 1 Machine Learning Specialist: Profesional dedicado al desarrollo e implementación de modelos de machine learning avanzados.


## Proyecto EcoTransit

EcoTransit es una empresa especializada en transporte público, ofresiendo servicios de corta a larga distancia en automóviles. Comprometidos a brindar un servicio seguro, de confianza y sostenible.

Se tiene en mente el ingresar al mercado de la ciudad de Nueva York para finales del 2024. Considerando regularizacines, que declaran que todos los taxis públicos deben ser 100% eléctricos para el 2025, sumando la necesidad de portar la etiqueta "cero emisiones", tanto para comerciales como para pick-up. Demostrando asi la capacdad de adaptación de EcoTransit.

## Objetivo General

Conducir un exhaustivo análisis de viabilidad para EcoTransit, con el propósito de adquirir perspectivas fundamentadas y establecer una presencia sólida en el mercado del transporte público de la ciudad de Nueva York. Este enfoque garantizará la rentabilidad y sostenibilidad a largo plazo de la empresa, mediante la identificación de oportunidades estratégicas y la implementación de medidas efectivas para satisfacer las demandas del mercado y superar los desafíos competitivos.

### Objetivos 
1. Identificar las necesidades del mercado: Hora de mayor uso, promedio de pasajeros por viaje, distacia promedio ve los viajes, duración de los viajes, ingresos según jornada laboral.
2. Estudiar la la disponibilidad y la ubicación de cargadores y supercargadores gratuitos o de pago por la ciudad.
3.  Analizar caracteristicas de los vehiculos actuales en el mercado para conseguir un ranking de de los mejores vahiculos para el mercado, considerando autonomía y tiempo de recarga.
4.  Realizar un modelo de regresión lineal para proyectar la utilidad esperada en años proximos y determinar la tasa de retorno de inversión, lo que lograra obtener el tiempo que tomará recuperar la inversión. (información crucial para inversionistas)

## KPIs

Los KPI son las herramientas que utiliamos para poder realizar una medición del progreso hacias las metas específicas, y nos ayudan a clarar las áresa a mejorar.

### **Disminución del costo operativo promedio por Vehículo** 

**Definición:**
El costo promedio operativo se toma como todo lo necesario para que un vehpiculo o una flota pueda operar por un periodo de tiempo determinado. Esto engloba cuestiones tales como: mantenimiento - recarga de baterías - seguro - impuestos - depreciación - etc.

**Meta:**
Disminución de un 10% en el primer año del costo operativo promedio con respecto al año 2023.

**Calculo y descripción:**
Identificaremos la opción mas rentable en términos de costo de adquisición, mantenimiento y carga entre las diferentes opciones de vehículo eléctricos disponibles en el mercado actual. Con este análisis sabremos cuál es el vehículo más óptimo en cuanto a costo operativo y utilidad. Para esto, se comparan diferentes costos para los diferentes vehículos eléctricos.



### **Tasa de retorno de la Inversión(ROI)**

**Definición:**
Esta tasa mide la rentabilidad de una inversión en relación a su costo inicial. Esto es clave para evaluar la eficiencia de la inversión y determinar si se justifica el costo inicial.

**Meta:**
Alcanzar un 15% de la tasa de inversión para el segundo año de la implementación de vehículos eléctricos.

**Cálculo y Descripción:**
Para lograr esto, se divide el beneficio neto obtenido de la inversión (ganancias generadas menos costos totales) entre el costo inicial, en porcentajes. Esto nos permítira ver que retorno económico esta generando al inversión en vehículos electricos en comparación con el costo inicial, determinar asi su rentabilidad a futuro.

### **Incremento en la Participación en el Mercado**

**Definición:**
Esto se refiere a la cuota del mercado que una empresa controla en relación al total del mercado disponible. Para una empresa de transporte, es sería el porcentaje de clientes que elige utilizar sus servicios en comparación con la competencia.

**Meta:**
Incrementar en un 20% la participación en el mercado, en los proximos 2 años.

**Calculo y Descrición:**
Esto se calcula dividiendo el número de viajes realizados de la empresa entre el total de viajes realizados en el mercado en un periodo determinado, en porcentaje.

## Solución

Para conserguir los objetivos propuestos y llegar a una solución, dividiremos este proyecto en 3 sprints. 
Esto lo dividimos en tareas y creamos un diagrama de [Gantt](https://equintana779s-team.monday.com/boards/6599101702) para un flujo de trabajo optimo. 


## Stack Tecnológico

El conjunto de herramientas que utilizaremos para este proyecto sera:

1. **Web Scrapping:**
    - **Herramientas Utilizadas**: Python, BeautifulSoup, urlparse.
    - **Próposito:**: Realizar el proceso de extracción de datos de la pagina TLC Trip Record Data.

2. **Manipulación y Procesamiento de Datos:**
    - **Herramientas Utilizadas:** Apache PySpark.
    - **Propósito:** Manipular eficientemente grandes volúmenes de datos y entrenar modelos de análisis.

3. **Automatización de Tareas:**
    - **Herramientas Utilizadas:** Apache Airflow.
    - **Próposito:** Automatizar tanto el proceso de web scraping como la carga de datos.

4. **Creación de Servicios Web y Exposición de Resultados:**
    - **Herramientas Utiliadas:** FastAPI.
    - **Próposito:** Construir APIs RESTful de alto rendimiento para la exposición de los resultados del análisis.

5. **Visualización de Datos:**
    - **Herramientas Utilizadas:** Streamlit.
    - **Próposito:** Consumir los datos almacenados en el almacén de datos y visualizarlos en un dashboard interactivo y dinámico.

<h2>Análisis de viabilidad.</h2>




1. **Identificación de las necesidades del mercado**

En Nueva York, existen diferentes tipos de taxis:

**Yellow Taxicabs:**

Son los taxis amarillos que tienen derecho a recoger pasajeros que los detengan en la calle en cualquier parte de la ciudad. 

Por ley, hay 13,587 taxis en la Ciudad de Nueva York, y cada taxi debe tener un medallón adherido a él. Estos medallones son subastados por la Ciudad y son transferibles en el mercado abierto por corredores con licencia.

Suponiendo que todos los 13587 taxis trabajaron los 29 días del mes de febrero del 2024 cada taxi pudo haber recorrido 854.6 Mi en ese mes, lo que equivale a 29.4 Mi por día.  
 


