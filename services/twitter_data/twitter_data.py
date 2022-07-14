import requests
import pandas as pd

def get_data(tweet):
    data = {'id': [tweet['id_str']],'created_at': [tweet['created_at']],'text': [tweet['full_text']]}
    return data

def process_data(query, num_tweets=100, exclude='retweets'):
    api = 'https://api.twitter.com/1.1/tweets/search/recent'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIPfegEAAAAALBnvPnmI2g37qbBSehLdBEdn%2FdQ%3DwJa0b3oQOQZ4ghX89ovypydWNNkKIdHem0AqO1nRq2Su4RSKPJ'
    params = {'q': query,
              'tweet_mode': 'extended',
              'lang': 'en',
              'count': str(num_tweets),
              'exclude': exclude,}

    tweets = requests.get(api,
                          params=params,
                          headers={'authorization': 'Bearer ' + BEARER_TOKEN})

    df = pd.DataFrame()

    for tweet in tweets.json()['statuses']:
        row = pd.DataFrame.from_dict(get_data(tweet))
        df = pd.concat([df, row])

    drop = []
    for i, tweet in enumerate(df['text']):
        while '@' in tweet:
            stem = tweet[:tweet.find('@')]
            post = tweet[tweet.find('@')+1:]
            if post.find(' ') == -1:
                post = ''
            else:
                post = post[post.find(' ') + 1:]
            tweet = stem + post

        while 'http' in tweet:
            stem = tweet[:tweet.find('http')]
            post = tweet[tweet.find('http') + 4:]
            if post.find(' ') == -1:
                post = ''
            else:
                post = post[post.find(' ') + 1:]
            tweet = stem + post

        while 's:/' in tweet:
            stem = tweet[:tweet.find('s:/')]
            post = tweet[tweet.find('s:/') + 3:]
            if post.find(' ') == -1:
                post = ''
            else:
                post = post[post.find(' ') + 1:]
            tweet = stem + post

        if tweet.count('#') > 8:
            drop.append(i)

        df['text'].iloc[i] = tweet

    df = df.drop(df.index[drop])

    return df


