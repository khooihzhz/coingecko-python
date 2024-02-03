import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Derivatives Endpoints
## /derivatives
response = client.derivatives.get()

## /derivatives/exchanges
response = client.derivatives.get_exchanges()

## /derivatives/exchanges/{id}
response = client.derivatives.get_exchanges_id(id='bitmex')

## /derivatives/exchanges/list
response = client.derivatives.get_exchanges_list()


