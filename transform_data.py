import numpy as np

# Contiene funciones de tipos, estandarización de texto, imputaciones, eliminación de observaciones o variables


# Elimina la columnas que se pase como array en el parámetro columnas
def drop_columns(df,columnas):
    df2 = df.drop(columns = columnas)
    return df2

# Separa "columna" en newcol1 y newcol2, con coma como separador por defecto
def split_column(df, columna, newcol1, newcol2, separador = ","):
    df[[newcol1,newcol2]] = df[columna].str.split(pat=separador,expand = True).astype(float)
    return df

# Selecciona las columnas con datos no numéricos, y las transforma a minúsculas
def data_to_lowercase(df):
    df_char = df.select_dtypes(exclude=[np.number, np.datetime64])
    encabezados_char = df_char.columns.values
    df_low = df.apply(lambda x: x.str.lower() if x.name in encabezados_char else x)
    return df_low

# Quita los acentos y cambia la letra ñ por ni
def data_sin_acentos(df):
    df = df.replace({"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", "ñ":"ni"}, regex=True)
    return df

# Cambia el tipo de dato de las columnas indicadas, por defecto, a tipo object
def change_type(df,columnas, tipo ="object"):
    new_col_type = dict()
    for x in columnas:
        new_col_type[x] = tipo
    df2 = df.astype(new_col_type)
    return df2

# Cambiar blancos por valores nulos de todas las columnas
def nulos(df):
    df = df.replace(r'^\s*$', np.nan, regex=True)
    return df

# Cambiar fechas en formato valor de excel a datetime
def xldate_to_datetime(xldate):
    import datetime

    temp = datetime.datetime(1899, 12, 30)
    delta = datetime.timedelta(days=xldate)
    return temp + delta
