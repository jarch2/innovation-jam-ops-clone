import pandas as pd
import matplotlib.pyplot as plt

import pandas_datareader as web
from datetime import datetime as dt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score


def pred_buy_sell(ticker, start_date, end_date, pred_days, predictors=['Close', 'High', 'Low', 'Open', 'Volume'],
                  estimators=100, samples_split=10, target_precision=0.5):

    # Preprocessing Data

    stock = web.DataReader(ticker, 'yahoo', start_date, end_date)

    data = stock[['Close']]
    data = data.rename(columns={'Close': 'Actual_Close'})
    data['Target'] = stock.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])['Close']

    # Processing extra predictors

    cut_off = 1

    if 'Weekly Average' in predictors:
        stock['Weekly Average'] = stock['Close'].rolling(7).mean()

    if 'Quarterly Average' in predictors:
        stock['Quarterly Average'] = stock['Close'].rolling(91).mean()

    if 'Yearly Average' in predictors:
        stock['Yearly Average'] = stock['Close'].rolling(365).mean()

    if 'Yearly Average' in predictors:
        cut_off = 365
    elif 'Quarterly Average' in predictors:
        cut_off = 91
    elif 'Weekly Average' in predictors:
        cut_off = 7

    stock_prev = stock.copy()
    stock_prev = stock_prev.shift(1)

    data = data.join(stock_prev[predictors]).iloc[cut_off:]

    # Model

    model = RandomForestClassifier(n_estimators=estimators, min_samples_split=samples_split, random_state=1)

    train = data.iloc[:-pred_days]
    test = data.iloc[-pred_days:]

    model.fit(train[predictors], train['Target'])

    preds = model.predict_proba(test[predictors])[:, 1]
    preds = pd.Series(preds, index=test.index)
    preds[preds >= target_precision] = 1
    preds[preds < target_precision] = 0

    return preds





