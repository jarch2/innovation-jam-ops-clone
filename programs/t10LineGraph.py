
import top_stocks
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

fileName = "../data//pricedata_reshaped.csv"
data = pd.read_csv(fileName)

dates = [date for date in data['date']]
datetimes = []
for date in dates:
    datetimes.append(dt.strptime(date, '%Y-%m-%d'))

filteredStocks = top_stocks.topStocks("..//data//meta.csv",10)
for i in range(10):
    plt.plot(datetimes, data[filteredStocks['ticker'][filteredStocks.index[i]]])

plt.show()
