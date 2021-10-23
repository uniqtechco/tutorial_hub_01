'''
chained pipeline for loading time series data
🐼 ⏱ in 🐍

1- read csv
2- use Date column as index
3- parse Date column as dates, as opposed to numbers or strings
4- drop target column, the column we are trying to predict

display the first few rows of the dataframe

'''

import pandas as pd

df = pd.read_csv(
    "../foldername/filename.csv",
    index_col='Date',
    parse_dates=['Date'],
).drop('target_col', axis=1)

df.head()
