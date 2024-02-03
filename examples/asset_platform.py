import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

## Asset Platform endpoints
## /asset_platforms
response = client.asset_platform.get()

## filter nfts
response = client.asset_platform.get(filter='nft')
