Trains Random Forest Classifier on single stock
Runs with command line inputs

Required:
* --ticker (string, ticker of the stock being predicted)

Optional:
* --estimators (int, number of decision trees in random forest)
* --precision (float, target precision of the model)
* --predictors (list of strings)
* --start_date (datetime, mm/dd/yyyy, start of the prediction)
* --end_date (datetime, mm/dd/yyyy, end of the prediction)
* --pred_days (int, amount of days predicted using the training)
* --samples_split (int, higher minimum sample split for faster performance lower precision)