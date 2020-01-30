# Introducción a Ciencia de Datos

## Proyecto 1

**Equipo:**

Diego Michell Villa Lizárraga - *191343* \
Elizabeth Rodriguez Sanchez - *191430*

## Requerimientos

El primer paso para poder ejecutar este pipeline es instalar todos los requerimientos que se encuentran en el documento requirements.txt

```shell
pip install -r requirements.txt
```

En este punto ya deberíamos de tener todas las librerías requeridas para poder ejecutar las funciones de nuestro pipeline.


## Scripts

El pipeline cuenta con 5 scripts:

+ load_data.py
+ clean_data.py
+ transform_data.py
+ eda.py
+ maestro.py

### Descripción de cada script

`load_data.py` \
En este script se encuentra la función para importar datos.

`clean_data.py` \
En este script se encuentra la función para limpiar encabezados de columnas.

`transform_data.py` \
En este script se encuentran las funciones para transformar los datos transform_data.

`EDA.py` \
Contiene funciones que nos ayudan a ejecutar el EDA.

`maestro.py`
Este script es el que ejecuta todas las funciones de los demás.


## Ejecución

Es importante tomar en cuenta que los 5 scripts y el archivo interrupcion-legal-del-embarazo.csv deben de estar en la misma carpeta. \

El único script que ejecutaremos será el `maestro.py`, desde la terminal ejecutamos:

```shell
python3 maestro.py
```
Una vez que haya terminado la ejecución de nuestro pipeline, obtendremos un reporte csv con el con el nombre de `results.csv` con los resultados de magic loop.

Además, se agregó un html con el detalle de lo que cada script realiza y la interpretación del EDA con el nombre de **reporte_final_EDA.**
