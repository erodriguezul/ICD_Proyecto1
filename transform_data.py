import numpy as np
#Contiene funciones de tipos, estandarización de texto, imputaciones, eliminación de observaciones o variables


#elimina la columnas que se pase como array en el parámetro columnas
def drop_columns(df,columnas):
    df2 = df.drop(columns = columnas)
    return df2

#Separa "columna" en newcol1 y newcol2, con coma como separador por defecto
def split_column(df, columna, newcol1, newcol2, separador = ","):
    df[[newcol1,newcol2]] = df[columna].str.split(pat=separador,expand = True).astype(float)
    return df

#Selecciona las columnas con datos no numéricos, y las transforma a minúsculas
def data_to_lowercase(df):
    df_char = df.select_dtypes(exclude=np.number)
    encabezados_char = df_char.columns.values
    df_low = df.apply(lambda x: x.str.lower() if x.name in encabezados_char else x)
    return df_low

#Selecciona las columnas con datos no numéricos, y les quita los acentos
def data_sin_acentos(df):
    df_char = df.select_dtypes(exclude=np.number)
    encabezados_char = df_char.columns.values
    df_sin_acentos = df.apply(lambda x: x.replace("á","a").replace("é","e").replace("í","i").\
    replace("ó","o").replace("ú","u") if x.name in encabezados_char else x)
    return df_sin_acentos

#Cambia el tipo de dato de las columnas indicadas, por defecto, a tipo object
def change_type(df,columnas, tipo ="object"):
    new_col_type = dict()
    for x in columnas:
        new_col_type[x] = tipo 
    df2 = df.astype(new_col_type)
    return df2