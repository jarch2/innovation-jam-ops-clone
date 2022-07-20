import finnhub
import os
import pandas as pd


def finnhub_data(ticker, start, end):
    client = finnhub.Client(api_key=os.environ.get('FINNHUB_TOKEN'))
    news = client.company_news(ticker, _from=start, to=end)

    df = pd.DataFrame(columns=['datetime', 'headline', 'summary'])
    for item in news:
        sub_dict = {'datetime': [item['datetime']], 'headline': [item['headline']], 'summary': [item['summary']]}
        row = pd.DataFrame.from_dict(sub_dict)
        df = pd.concat([df, row], ignore_index=True)

    return df


