import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

# NFTs Endpoints
## /nfts/list
response = client.nfts.get_list()

## /nfts/{id}
response = client.nfts.get_id(id='pudgy-penguins')

## /nfts/{asset_platform}/contract/{contract_address}
response = client.nfts.get_by_contract_address(asset_platform='ethereum', contract_address='0xBd3531dA5CF5857e7CfAA92426877b022e612cf8')

## --- PRO ONLY ENDPOINTS ---
## /nfts/markets
response = client.nfts.get_markets()

## /nfts/{id}/market_chart
response = client.nfts.get_market_chart(id="pudgy-penguins", days="1")

## /nfts/{asset_platform_id}/contract/{contract_address}/market_chart
response = client.nfts.get_market_chart_by_contract_address(asset_platform_id="ethereum", contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8", days="1")

## /nfts/{id}/tickers
response = client.nfts.get_tickers(id="pudgy-penguins")

