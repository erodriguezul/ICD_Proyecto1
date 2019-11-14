#Módulo para estandarización de nombres de variables.

#Función para formatear nombres de variables: en minúsculas, con guión bajo en lugar de espacios, eliminamos puntos, comas y acentos
def clean_format(cadena):
    nueva_cadena = cadena.lower().replace(".","").replace(",","").\
    replace("á","a").replace("é","e").replace("í","i").\
    replace("ó","o").replace("ú","u").replace(" ","_")
    return nueva_cadena

#Función para formatear un arreglo con los encabezados de las columnas
def clean_array(array):
    new_head = []
    for i in range(0,len(array)):
        nomcol = array[i]
        newcol = clean_format(nomcol)
        new_head.append(newcol)
    return new_head

# Función para formatear los nombres de todas las columnas que conforman al dataframe
def clean_column_headers(df):
    encabezados = df.columns.values
    new_column_headers = clean_array(encabezados)
    for i in range(0,len(df.columns)):
        df.rename(columns =  {encabezados[i]: new_column_headers[i]}, inplace = True)
    return df
    