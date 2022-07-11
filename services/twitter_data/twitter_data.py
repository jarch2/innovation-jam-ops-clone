import requests

# Joe bearer_token
#BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFreegEAAAAAYOb3ENNoedusfDhKH5c1BTvnVwg%3DUVKL7IBTqEKehk0oIk7m7rvTqtkT5WC9wUgTC5mWcxVXRcTJYC'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIPfegEAAAAALBnvPnmI2g37qbBSehLdBEdn%2FdQ%3DwJa0b3oQOQZ4ghX89ovypydWNNkKIdHem0AqO1nRq2Su4RSKPJ'
tweets = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=tesla', headers={'authorization': 'Bearer ' + BEARER_TOKEN})

params = {'q': 'tesla' 'tweet_mode': 'extended'}
requests.get('https://api.twitter.com/1.1/search/tweets.json')
params = params, headers = {'authorization': 'Bearer ' +BEARER_TOKEN}


response.jason()
/search/tweets.json?q=tesla&tweet_mode=extended

print(tweets.json())