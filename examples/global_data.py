import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

## Global Endpoints

## /global
response = client.global_data.get()

## /global/decentralized_finance_defi
response = client.global_data.get_defi()
