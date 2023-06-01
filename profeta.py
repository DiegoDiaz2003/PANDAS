import pandas as pd
from prophet import Prophet
from matplotlib import pyplot
import numpy as np
from pandas.core.arrays import datetimes


df = pd.read_csv("Cambio de Dolar.csv")


df

df.info()

#df = df.astype ({"VIGENCIADESDE": "datetime64"})
#df = df.astype ({"VIGENCIAHASTA": "datetime64"})

df.dtypes
type(df.head)

df.drop(["UNIDAD","VIGENCIAHASTA"], axis = 'columns', inplace=True)

df = df.rename(columns={"VALOR":"ds","VIGENCIADESDE":"y"})
df.columns


type(df.columns)



print(df.head())

