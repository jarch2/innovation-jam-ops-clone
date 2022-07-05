from services import predict_buy_sell
import argparse
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--ticker', type=str, required=True)
parser.add_argument('--precision', type=float, required=False)
parser.add_argument('--estimators', type=int, required=False)
parser.add_argument('-p', '--predictors', nargs='+', required=False)
args = parser.parse_args()

preds = predict_buy_sell.pred_buy_sell(args.ticker)

plt.plot(preds['Predictions'])
plt.plot(preds['Target'])
plt.show()

