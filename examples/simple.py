import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Simple Endpoints

## Simple Price with 1 coins
response = client.simple.price(ids='bitcoin', vs_currencies='usd')

## Simple Price with 1 coins and include market_cap, 24hr_vol, and 24hr_change
response = client.simple.price(ids='bitcoin', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)

## Simple Price with multiple coins & currencies
response = client.simple.price(ids=['bitcoin', 'ethereum'], vs_currencies=['usd', 'eur'])

## Simple Token Price with contract_addresses
response = client.simple.token_price(id='ethereum', contract_addresses='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', vs_currencies='usd')

## Simple Token Price with contract_addresses and include_market_cap, 24hr_vol, and 24hr_change
response = client.simple.token_price(id='ethereum', contract_addresses='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)

## Simple Token Price with multiple contract_addresses and vs_currencies
contract_addresses = ['0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', '0xdac17f958d2ee523a2206206994597c13d831ec7']
response = client.simple.token_price(id='ethereum', contract_addresses=contract_addresses, vs_currencies=['usd', 'eur'])

## Simple Supported_vs_Currencies
response = client.simple.supported_vs_currencies()
