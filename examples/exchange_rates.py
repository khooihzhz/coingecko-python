import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Exchange Rates Endpoints
## /exchange_rates
response = client.exchange_rates.get()

