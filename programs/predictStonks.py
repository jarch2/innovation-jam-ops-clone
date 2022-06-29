import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as web
from datetime import datetime as dt

ticker = "NCR"

start = dt(2010,1,1)
end = dt(2020,1,1)

ncr_hist = web.DataReader(ticker, 'yahoo', start, end)

print(ncr_hist.head())

data = ncr_hist[["Close"]]
data = data.rename(columns = {'Close':'Actual_Close'})
data["Target"] = ncr_hist.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[1] > x.iloc[0])["Close"]

data.head(5)