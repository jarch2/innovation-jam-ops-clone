import sys
import predict_buy_sell
import argparse
import datetime as dt
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-ticker', type=str, required=True)
parser.add_argument('-tp', type=float, required=False)
args = parser.parse_args()

preds = predict_buy_sell.pred_buy_sell(args.ticker, dt.datetime(2000,1,1), dt.datetime(2015,1,1), 120, target_precision=args.tp)


plt.plot(preds['Predictions'])
plt.plot(preds['Target'])
plt.show()