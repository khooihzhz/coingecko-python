import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Exchanges Endpoints
## /exchanges
response = client.exchanges.get()

## /exchanges/list
response = client.exchanges.get_list()

## /exchanges/{id}
response = client.exchanges.get_id(id='binance')

## /exchanges/{id}/tickers
response = client.exchanges.get_tickers(id='binance')

## /exchanges/{id}/volume_chart
response = client.exchanges.get_volume_chart(id='binance', days='1')


