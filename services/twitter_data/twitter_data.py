import requests
import pandas as pd
import flair

# Joe bearer_token
#BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFreegEAAAAAYOb3ENNoedusfDhKH5c1BTvnVwg%3DUVKL7IBTqEKehk0oIk7m7rvTqtkT5WC9wUgTC5mWcxVXRcTJYC'

api = 'https://api.twitter.com/1.1/tweets/search/recent'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIPfegEAAAAALBnvPnmI2g37qbBSehLdBEdn%2FdQ%3DwJa0b3oQOQZ4ghX89ovypydWNNkKIdHem0AqO1nRq2Su4RSKPJ'

tweet_mode = '/search/tweets.json?q=tesla&tweet_mode=extended'

params = {'q': 'tesla', 'tweet_mode': 'extended', 'lang': 'en', 'count': '100'}
tweets = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=tesla', params=params, headers={'authorization': 'Bearer ' +BEARER_TOKEN})

def get_data(tweet):
    data = {'id': [tweet['id_str']],'created_at': [tweet['created_at']],'text': [tweet['full_text']]}
    return data

df = pd.DataFrame()

for tweet in tweets.json()['statuses']:
    row = pd.DataFrame.from_dict(get_data(tweet))
    df = pd.concat([df, row])
cc
print(df.head())