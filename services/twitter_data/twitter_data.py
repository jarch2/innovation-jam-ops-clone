import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFreegEAAAAAYOb3ENNoedusfDhKH5c1BTvnVwg%3DUVKL7IBTqEKehk0oIk7m7rvTqtkT5WC9wUgTC5mWcxVXRcTJYC'
tweets = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=tesla', headers={'authorization': 'Bearer ' + BEARER_TOKEN})

print(tweets.json())