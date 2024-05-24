## EDA del dataset Electric and Alternative Fuel Chargin Station.csv

Durante el proceso de selección de características para nuestro análisis, se llevaron a cabo decisiones estratégicas para centrar el estudio en información clave y relevante, eliminando aquellas columnas que presentaban ambigüedad, inespecificidad o aportaban poca relevancia al objetivo del análisis. La elección de las columnas seleccionadas se basó en la necesidad de optimizar y garantizar la interpretación significativa de los resultados obtenidos.

La atención se centró en aquellas variables que ofrecen una visión más detallada y esclarecedora de la distribución de estaciones de carga, sus características específicas y su impacto potencial en la adopción de vehículos con combustibles alternativos.



#### Dominio de Vehículos Eléctricos (ELEC):

Representa la mayoría de las estaciones de carga, con un impresionante 86.5%.
La alta proporción sugiere un crecimiento y aceptación significativos de los vehículos eléctricos en la zona cubierta por los datos.
Presencia de Combustibles Alternativos:

E85 (etanol) contribuye con un 6.4%, lo que indica cierto grado de diversidad en los combustibles alternativos utilizados en las estaciones de carga.
Propano (LPG) y Gas Natural Comprimido (CNG) tienen participaciones similares de alrededor del 2.7% y 2.3%, respectivamente.
Biodiesel (BD) y GNL:

Biodiesel (BD) representa el 1.7%, mientras que Gas Natural Licuado (LNG) y Hidrógeno (HY) tienen participaciones más bajas de aproximadamente el 0.2% cada uno.
Estas opciones menos comunes sugieren una infraestructura en desarrollo para vehículos que utilizan estos combustibles.
Enfoque Sostenible y Ambiental:

La predominancia de opciones eléctricas y etanol puede indicar una creciente preferencia por vehículos más sostenibles y amigables con el medio ambiente.
En conjunto, la distribución de tipos de combustibles sugiere una tendencia hacia la electrificación, pero también se observa una diversidad que puede ser relevante para la transición hacia fuentes de energía más limpias y sostenibles.

![Distribución de combustible por tipo de código](src\Distribución_combustible_x_codigo.png)

Las ciudades de Los Ángeles y San Diego, en California, junto con Montreal, en Canadá, se destacan por tener el mayor número de estaciones de energía alternativa.


#### Ciudades con más estaciones de servicio de combustible alternativo

![Top 20 ciudades con mas estaciones de servicio de combustible alternativo](src\top_20_cities.png)

California lidera con amplia ventaja en la adopción de fuentes de energía alternativas, seguido por el estado de Nueva York.


#### Estados con mayor número de estaciones de servicio

![20 principales entidades (estados) por cantidad de estaciones](src\top25_states.png)

El gráfico evidencia que California es el líder indiscutible en la adopción de estaciones de carga eléctrica para vehículos.


#### Top 20 estados con mayor número de estaciones de carga eléctrica

![Top 20 estados con más estaciones de carga electrica](src\top20_estados_estaciones_carga.png)

El gráfico evidencia que California es el líder indiscutible en la adopción de estaciones de carga eléctrica para vehículos.


#### Top 20 estados por tipos de combustible excluyendo estaciones de carga

![Top 20 estados de estaciones sin incluir estaciones de carga](src\top20_estaciones_sin incluir_elect.png)

El análisis de la distribución porcentual de los diferentes tipos de combustibles en las estaciones de carga es el siguiente:

ELEC (Electricidad): 86.51%

Electricidad es la fuente de energía dominante en las estaciones de carga, representando más del 86% del total.
Este alto porcentaje sugiere una adopción significativa de vehículos eléctricos en comparación con otros tipos de combustibles alternativos.
E85 (85% de etanol): 6.40%

Aunque en menor proporción que la electricidad, el E85 tiene una presencia considerable.
Puede indicar cierto interés en los biocombustibles, aunque no tan prevalente como la electricidad.
LPG (Gas Licuado de Petróleo): 2.65%

El Gas Licuado de Petróleo ocupa un espacio significativo, pero menos común que los dos anteriores.
Es probable que exista una demanda para vehículos que utilicen gas licuado como fuente de energía.
CNG (Gas Natural Comprimido): 2.32%

El Gas Natural Comprimido tiene una representación similar al LPG.
Puede indicar una infraestructura creciente para vehículos que utilizan gas natural.
BD (Biodiesel): 1.73%

El Biodiesel tiene una presencia menor en comparación con otras fuentes de energía.
Puede haber una adopción limitada de vehículos que utilizan biodiesel en comparación con otras tecnologías.
LNG (Gas Natural Licuado): 0.22%

El Gas Natural Licuado tiene una presencia mínima en las estaciones de carga.
Puede sugerir una adopción limitada de vehículos que utilizan gas natural licuado.
HY (Hidrógeno): 0.17%

El hidrógeno tiene la menor representación entre los tipos de combustibles.
La infraestructura para vehículos de hidrógeno puede estar en las etapas iniciales de desarrollo.


#### Progreso del número de estaciones a lo largo del tiempo.

![Progreso de estaciones a lo largo del tiempo](src/num_estaciones_x_anio.png)

El análisis del conteo de estaciones de carga por año desde 2010 muestra un claro aumento en la implementación de estaciones de carga para vehículos eléctricos. Aquí hay algunas observaciones clave:

Crecimiento Sostenido: A lo largo de los años, se observa un crecimiento sostenido en el número de estaciones de carga desde 2010 hasta 2022.

Aceleración en los Últimos Años: Se destaca un aumento significativo a partir de 2019, con un fuerte crecimiento en 2020 y 2021. Este aumento puede indicar un interés creciente en la infraestructura de carga para vehículos eléctricos.

2021 como un Año de Auge: El año 2021 muestra un aumento drástico, más que duplicando la cantidad de estaciones de carga en comparación con el año anterior (2020).

Posible Influencia de Políticas y Mercado: El aumento en la adopción de estaciones de carga puede estar relacionado con políticas gubernamentales, incentivos y la creciente demanda del mercado de vehículos eléctricos


#### Conteo de cada categoría en 'NG Vehicle Class

![conteo de cada categoría en 'NG Vehicle Class](src\distribucion_de_NG_X_categoria.png)

La categoría de vehículos que más utiliza gas natural es la de "heavy-duty", con una proporción aproximada de 6 a 1 en comparación con otras categorías.



## EDA del dataset Vehicle Fuel Economy Data.csv

### Año de fabricación vs emisiones de CO2

![Año de fabricación vs emisiones de CO2](src\anio_fab_vs_emisiones.png)

Existe una variabilidad considerable en las emisiones de CO2 entre los vehículos de un mismo año. Esto se evidencia por la dispersión vertical de los puntos para cada año. Algunos vehículos emiten significativamente más CO2 que otros dentro del mismo año de fabricación.

Distribución de Datos: Los datos no están uniformemente distribuidos a lo largo de los años. Parece haber años con mayor concentración de datos, lo cual podría reflejar una mayor cantidad de modelos de vehículos lanzados o una mejor recolección de datos en ciertos años.


### Emisiones de CO2 por año según tipo de combustible

![emisiones de co2 por tipo de combustible y año](src\co2_x_año_y_tipo.png)

El tipo 2 de combustible hace referencia al E85, por lo tanto se entiende que sea más bajo pero no totalmente en 0, ya que promedia tanto electicos como hibridos.


### Costo por tipo de combustible

![costo_tipo](src\costo_por_tipo_combustible.png)

Aquí apreciamos que el costo de gas es más elevado que los otros tipos de combustible, siendo el electrico el más económico.


### Media de emisiones de CO2 por fabricante

![emisiones de co2 por fabricante](src\co2_x_fabricante.png)

Observamos que los vehiculos de alta gama tienen un nivel mayor de emmisiones de CO2


### Fabricates con consumo más eficiente de combustible

![eficientes](src\fabricantes_eficientes.png)

La marca Kandi produce los vehiculos más eficientes con respecto al consumo de combustible


### Relación del costo del combustible por año

![costo del combustible por año](src\costo_x_año_combustible.png)

El pico que se observa en la gráfica despues del año 2000 es producido por la guerra en Irak y el ataque a las torres gemelas.


### Emisiones por clase de vehiculos

![emisiones por tipo de vehiculo](src\emisiones_x_tipo_de_vehiculo.png)

Aqui apreciamos las emisiones según el tipo del vehiculo.


### Costo del combustible por tipo y año

![costo combustible](src\costo_combustible_portipo_año.png)

El tipo 1 de combustible hace referencia a combustibles ecológicos y el tipo 2 es combustible fosil como la gasolina, en este caso desde el 2010 ha disminuido progresivamente los combustibles ecológicos.


### Evolución del uso de vehiculos eléctricos

![evolución del uso de vehiculos electricos](src\evolucion_vehiculos_electricos.png)

Desde el año 2010 hasta la fecha el uso del vehiculos eléctricos no ha dejado de incrementar.


### Rendimiento en ciudad y autopista por fabricante

| Manufacturer                    | UCity     | UHighway  |
|--------------------------------|-----------|-----------|
| Kandi                          | 181.200   | 145.200   |
| Lucid                          | 163.995   | 164.588   |
| Tesla                          | 143.994   | 139.850   |
| Polestar                       | 117.544   | 109.122   |
| CODA Automotive                | 110.300   | 97.000    |
| ...                            | ...       | ...       |
| Laforza Automobile Inc         | 12.000    | 18.000    |
| Superior Coaches Div E.p. Dutton| 12.000    | 15.000    |
| S and S Coach Company E.p. Dutton| 11.000  | 15.000    |
| Bugatti                        | 9.925     | 17.431    |
| Vector                         | 9.444     | 16.667    |


### Rendimiento por tipo de cobustibe en autopista y ciudad

![autopista](src\rendimiento_autopista.png)
![city](src\rendimiento_city.png)


### Comparación de rendimiento entre ciudad y autopista de vehiculos con Scharger

![comparación del rendimiento](src\rendimiento_scharger.png)

Apreciamos que el rendimiento en autopista es superior al rendimiento en ciudad.