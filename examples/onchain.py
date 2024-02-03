import coingecko

client = coingecko.CoinGeckoProClient(api_key='YOUR_API_KEY')

## GeckoTerminal API Endpoints: https://www.geckoterminal.com/dex-api

## /simple/networks/{network}/token_price/{addresses}
network = 'eth'
contract_addresses=['0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48']
response = client.onchain.get_simple_token_price(network=network, addresses=contract_addresses)

## /networks
response = client.onchain.get_networks()

## /networks/{network}/dexes
network = 'eth'
response = client.onchain.get_dexes(network=network)

## /networks/trending_pools
include = ['base_token', 'quote_token']
response = client.onchain.get_trending_pools(include=include, page=2)

## /networks/{network}/trending_pools
network = 'eth'
response = client.onchain.get_network_trending_pools(network=network)

## /networks/{network}/pools/{address}
network = 'eth'
address = '0x60594a405d53811d3bc4766596efd80fd545a270'
response = client.onchain.get_network_pools_address(network=network, address=address)

## /networks/{network}/pools/multi/{addresses}
network = 'eth'
addresses = ['0x60594a405d53811d3bc4766596efd80fd545a270', '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640']
response = client.onchain.get_network_pools_address_multi(network=network, addresses=addresses)

## /networks/{network}/pools
network = 'eth'
response - client.onchain.get_network_top_pools(network=network)

## /networks/{network}/dexes/{dex}/pools
network = 'eth'
dex = 'uniswap'
response = client.onchain.get_network_dexes_top_pools(network=network, dex=dex)

## /networks/{network}/new_pools
network = 'eth'
response = client.onchain.get_network_new_pools(network=network)

# /networks/new_pools
response = client.onchain.get_new_pools()

## /search/pools
query = 'uniswap'
response = client.onchain.get_search_pools(query=query)

## /networks/{network}/tokens/{token_address}/pools
network = 'eth'
token_address = '0x6b175474e89094c44da98b954eedeac495271d0f'

response = client.onchain.get_tokens_top_pools(network=network, token_address=token_address)

## /networks/{network}/tokens/{address}
network = 'eth'
address = '0x6b175474e89094c44da98b954eedeac495271d0f'

response = client.onchain.get_tokens(network=network, address=address)

## /networks/{network}/tokens/multi/{addresses}
network = 'eth'
addresses = ['0x6b175474e89094c44da98b954eedeac495271d0f', '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599']

response = client.onchain.get_tokens_multi(network=network, addresses=addresses)

## /networks/{network}/tokens/{address}/info
network = 'eth'
address = '0x6b175474e89094c44da98b954eedeac495271d0f'

response = client.onchain.get_tokens_info(network=network, address=address)


## /networks/{network}/pools/{pool_address}/info
network = 'eth'
pool_address = '0x60594a405d53811d3bc4766596efd80fd545a270'

response = client.onchain.get_token_pools_info(network=network, pool_address=pool_address)

## /tokens/info_recently_updated
response = client.onchain.get_tokens_info_recently_updated(network=network, address=address)

## /networks/{network}/pools/{pool_address}/ohlcv/{timeframe}
network = 'eth'
pool_address = '0x60594a405d53811d3bc4766596efd80fd545a270'
timeframe = 'day'

response = client.onchain.get_ohlcv(network=network, pool_address=pool_address, timeframe=timeframe)

## /networks/{network}/pools/{pool_address}/trades
network = 'eth'
pool_address = '0x60594a405d53811d3bc4766596efd80fd545a270'

response = client.onchain.get_trades(network=network, pool_address=pool_address)

