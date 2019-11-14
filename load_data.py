import pandas as pd

def leedatos(archivo,sep=";"):
    data = pd.read_csv(archivo,sep)
    return data
