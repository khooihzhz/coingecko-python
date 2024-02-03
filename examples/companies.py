import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Companies Endpoints
## /companies/public_treasury/{coin_id}

response = client.companies.get_public_treasury(coin_id='bitcoin')
