import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Search Endpoints
## /search
response = client.search.get(query='bitcoin')

## /search/trending
response = client.search.get_trending()
