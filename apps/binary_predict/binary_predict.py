from predict_buy_sell import pred_buy_sell
import argparse
import datetime as dt
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--ticker', type=str, required=True)
parser.add_argument('--precision', type=float, required=False)
parser.add_argument('--estimators', type=int, required=False)
parser.add_argument('-p', '--predictors', nargs='+', required=False)
parser.add_argument('--start_date', type=str, required=False)
parser.add_argument('--end_date', type=str, required=False)
parser.add_argument('--pred_days', type=int, required=False)
parser.add_argument('--samples_split', type=int, required=False)
args = parser.parse_args()

if args.precision is None:
    args.precision = 0.5
if args.pred_days is None:
    args.pred_days = 30

preds = pred_buy_sell(args.ticker, start_date=dt.datetime.strptime(args.start_date, '%Y-%m-%d'),
                      end_date=dt.datetime.strptime(args.end_date, '%Y-%m-%d'), predictors=args.predictors,
                      target_precision=args.precision, pred_days=args.pred_days)

plt.plot(preds['Predictions'])
plt.plot(preds['Target'])
plt.show()

true_p = 0
false_p = 0
for i in preds.index:
    if preds.loc[i, 'Predictions'] == 1 and preds.loc[i, 'Target'] == 1:
        true_p += 1
    if preds.loc[i, 'Predictions'] == 1 and preds.loc[i, 'Target'] == 0:
        false_p += 1

print('Precision of model test: ' + str(true_p / (true_p + false_p)))

