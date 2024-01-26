import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# Coins Endpoints
## /coins/list
response = client.coins.get_list(include_platform=True)

## /coins/markets multiple coin ids with pagination
response = client.coins.get_markets(vs_currency='usd', ids=['bitcoin', 'ethereum'], per_page=1, page=1)

## /coins/{id} with localization, tickers and market_data
response = client.coins.get_id(id='bitcoin', localization=True, tickers=True, market_data=True)

## /coins/{id}/tickers
response = client.coins.get_tickers(id='bitcoin', exchange_ids=['binance', 'kraken'])

## /coins/{id}/history
response = client.coins.get_history(id='bitcoin', date='30-12-2017')

## /coins/{id}/market_chart
response = client.coins.get_market_chart(id='bitcoin', vs_currency='usd', days=1)

## /coins/{id}/market_chart/range
response = client.coins.get_market_chart_range(id='bitcoin', vs_currency='usd', from_timestamp=1392577232, to_timestamp=1422577232)

## /coins/{id}/ohlc
response = client.coins.get_ohlc(id='bitcoin', vs_currency='usd', days=1)

# Get Coins by contract addresses
## /coins/{id}/contract/{contract_address}
response = client.coins.get_coin_by_contract_address(id='ethereum', contract_address='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984')

## /coins/{id}/contract/{contract_address}/market_chart/
response = client.coins.get_coin_by_contract_address_market_chart(id='ethereum', contract_address='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', vs_currency='usd', days=1)

## /coins/{id}/contract/{contract_address}/market_chart/range
response = client.coins.get_coin_by_contract_address_market_chart_range(id='ethereum', contract_address='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', vs_currency='usd', from_timestamp=1392577232, to_timestamp=1422577232)

