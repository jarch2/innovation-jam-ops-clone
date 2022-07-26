import pandas as pd
import pandas_datareader as web
from datetime import datetime as dt
from datetime import timedelta
from datetime import date
from sklearn.ensemble import RandomForestClassifier
from finnhub_data import finnhub_data
from sentiment import avg_sentiment


def pred_buy_sell(ticker, start_date=dt(2000,1,1), end_date=dt(2020,1,1), pred_days=30, predictors=['Close', 'High', 'Low', 'Open', 'Volume'],
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
    elif 'Weekly Average' in predictors or 'Weekly Sentiment' in predictors:
        cut_off = 7
        
    if 'S&P500' in predictors:
        stock['S&P500'] = web.DataReader('^GSPC', 'yahoo', start_date, end_date)['Close']

    if 'Sentiment' in predictors or 'Weekly Sentiment' in predictors:
        stock['Sentiment'] = ''
        news = finnhub_data(ticker, start_date, end_date, 3)

        for date in stock.index:
            daily = news.copy().loc[news['date'] == date.date()]
            if daily.empty:
                stock.loc[date, 'Sentiment'] = 0.1
            else:
                stock.loc[date, 'Sentiment'] = avg_sentiment(daily['headline'].tolist())

    if 'Weekly Sentiment' in predictors:
        stock['Weekly Sentiment'] = stock['Sentiment'].rolling(7).mean()

    stock_prev = stock.copy()
    stock_prev = stock_prev.shift(1)

    data = data.join(stock_prev[predictors]).iloc[cut_off:]

    # Model

    model = RandomForestClassifier(n_estimators=estimators, min_samples_split=samples_split, random_state=1)

    train = data.iloc[:-pred_days]
    test = data.iloc[-pred_days:]

    model.fit(train[predictors], train['Target'])

    preds = (model.predict_proba(test[predictors]))[:, 1]
    preds = pd.Series(preds, index=test.index)
    preds[preds >= target_precision] = 1
    preds[preds < target_precision] = 0

    combined = pd.concat({'Target': test['Target'], 'Predictions': preds}, axis=1)

    return combined


if __name__ == '__main__':
    print(pred_buy_sell('AAPL', start_date=dt(2020,1,1), end_date=dt(2022,7,30), pred_days=1, predictors=['Close', 'High', 'Low', 'Open', 'Volume'],
                  estimators=100, samples_split=10, target_precision=0.5).head())
