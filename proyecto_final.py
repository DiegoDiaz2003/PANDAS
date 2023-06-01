# -*- coding: utf-8 -*-
"""proyecto final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-t-sWMI78q9X5590yfdZVbXaEzXofmDz
"""

!pip install prophet

import pandas as pd
from prophet.plot import plot_plotly, plot_components_plotly
from fbprophet import Prophet

df = pd.read_csv('/content/Cambio de Dolar.csv')
df.dropna(inplace= True)
df.reset_index(drop=True, inplace=True)

df.info()

df.head()

#se elimino las columnas que no son necesarias usando el drop

df.drop(["UNIDAD","VIGENCIAHASTA"], axis = 'columns', inplace=True)

df.dtypes

df = df.dropna()

df = df.rename(columns={"VALOR":"y","VIGENCIADESDE":"ds"})

df=df[["y","ds"]]
df.head()

df.columns = ['y','ds']

df['ds'] = pd.to_datetime(df['ds'])
df.tail()

#df["ds"] = pd.to_datetime(df["ds"])

df['y'] = pd.to_numeric(df['y'], errors='coerce')

df.plot(x='ds',y='y',figsize=(18,6))

len(df)

train = df.iloc[:len(df)-365]
test = df.iloc[len(df)-365:]

df.tail

m = Prophet()
m.fit(train)
future = m.make_future_dataframe(periods=365) 
forecast = m.predict(future)

forecast.tail()

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

test.tail()