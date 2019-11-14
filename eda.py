#Cargará la fuente de datos
import pandas as np
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

###################EDA#########################################

#Funcion para obtener el número de observaciones y variables
def shape(df):
    df.shape
    print("Numero de observaciones: ",df.shape[0])
    print("Numero de variables: ", df.shape[1])
    return 
#Función que te da el número de observaciones unicas por variable
def uniques_df(df):
    print("El número de observaciones únicas por variable es: ")
    q = df.nunique()
    return q

#Tipos de variables del dataframe
def types(df):
    print("Los tipos de variables del dataframe son: ")
    y = df.dtypes
    return y

#Número de datos que pertenecen a cada una de las Alcaldías
def count_group(df,group):
    x = df.groupby([group])[group].count().sort_values(ascending = False)
    print("El número de datos por grupo es: ")
    return x

#Lista las columnas que tenemos después de los arreglos a las variables
def list_cols(df):
    cols = df.columns.tolist()
    print("Las columnas que tenemos despues de los ajustes son: ")
    return cols

# Con esto se obtiene: número de observaciones, mean, desviación estándar, cuartiles, valor máx y valor mín
def describe_df(df):
    x = df.describe().transpose()
    print("El resumen estadítio por variables es: ")
    return x

##Top 5 de observaciones repetidas por variable para las variables numpericas
#Definimos una función para hacer el conteo por cada columna de dataframe def_num
def duplicate_obs(df):
    top5 = []
    for i in df:
        ddf = df.pivot_table(index = df[i],aggfunc = 'size')
        ddf5 = ddf.nlargest(5)
        top5.append(ddf5)
    print("El top 5 de los datos más repetidos para cada una de las variables de dataframe es: ")
    return top5

#Número de observaciones con valores faltantes
def null_dat(df):
    x = df.isnull().sum()
    print("El número de observaciones con valores faltantes por cada variable del dataframe es: ")
    return x

#Transformar el tipo de variable a object
def transf(df,col,tipo):
    df = df.astype({col:tipo})
    print("Los nuevos tipos de vairiable del dataframe es:")
    return df.dtypes

#Función que te da el número de observaciones unicas por variable categorica
def uniques_df_cat(df):
    print("El número de observaciones únicas por variable es: ")
    q = df.nunique(axis = 0)
    return q


#Numero de cateogrias por variable
def num_categ(df):
    x = df.nunique(axis = 0)
    print("El número de categorias por variable es: ")
    return x

#Proporcion de observaciones por categoria
#Primero calculamos cuantos hay de cada categoria por variable
def prop_obs(df):
    prop = []
    for i in df:
        propdf = 100*df[i].value_counts()/len(df[i])
        prop.append(propdf)
    print("La proporción de observaciones por variable es: ")         
    return prop

#Moda de cada una de las variables cateogricas
def mode(df):
    x = df.mode()
    print("La moda para cada variable categórica es: ")
    return x

#Agrupa y hace un conteo
def group_count(df,x,y,z):
    x = df.groupby([x, y]).size().reset_index(name = z)
    print("El conteo del dataframe agrupado queda: ")
    return x
############################GEDA######################################################################################

#Catplot
def catplot(df,x,y,hue):
    g = sns.catplot(x=x, y=y, hue=hue, data=df, saturation=.8, kind="bar", ci=None, aspect=1.7, height = 8 ,legend = 'true')
    plt.subplots_adjust(top=0.93)
    g.fig.suptitle('Gráfica de '+ x +' por delegación para cada indice_des',fontsize=15)
    return g

#Histograma para cada variable categorica
def barplot(df,x):
    x = df[x].value_counts().plot(kind ='bar', color = 'g')
    return x
