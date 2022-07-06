from services import pred_buy_sell
import argparse
import datetime as dt
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--ticker', type=str, required=True)
parser.add_argument('--precision', type=float, required=False)
parser.add_argument('--estimators', type=int, required=False)
parser.add_argument('-p', '--predictors', nargs='+', required=False)
parser.add_argument('--start_date', type=dt.datetime, required=False)
parser.add_argument('--end_date', type=dt.datetime, required=False)
parser.add_argument('--pred_days', type=int, required=False)
parser.add_argument('--samples_split', type=int, required=False)
args = parser.parse_args()

preds = pred_buy_sell(args.ticker)

plt.plot(preds['Predictions'])
plt.plot(preds['Target'])
plt.show()

