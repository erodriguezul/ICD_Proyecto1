#Cargará la fuente de datos
import pandas as np
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

###################EDA#########################################

# Para cada una de las columnas del dataframe de tipo 'object' imprime el conjunto de posibles valores
def categorias(df):
    columnas_cat = df.select_dtypes(include=object).columns.values
    for x in columnas_cat:
        print('Categorías para',x,': ',df[x].unique(),'\n')
    return

##
def proporcion_nas(df):
    return df.isna().sum()/df.shape[0]

################Miguel######################


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


#Proporcion de observaciones por categoria
#Primero calculamos cuantos hay de cada categoria por variable
def prop_obs(df):
    prop = []
    for i in df:
        propdf = 100*df[i].value_counts()/len(df[i])
        prop.append(propdf)
    print("La proporción de observaciones por variable es: ")         
    return prop


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
