import pytest

@pytest.mark.vcr
def test_get_simple_token_price(client):
    network = 'eth'
    contract_addresses = ['0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48']

    response = client.onchain.get_simple_token_price(network=network, addresses=contract_addresses)

    assert 'data' in response.keys()
    assert 'type' in response['data'].keys()
    assert 'token_prices' in response['data']['attributes'].keys()

@pytest.mark.vcr
def test_get_networks(client):
    response = client.onchain.get_networks()

    assert len(response['data']) > 0
    assert all(key in response['data'][0].keys() for key in ['id', 'type', 'attributes'])

@pytest.mark.vcr
def test_get_dexes(client):
    network = 'eth'
    response = client.onchain.get_dexes(network=network)

    assert len(response['data']) > 0
    assert all(key in response['data'][0].keys() for key in ['id', 'type', 'attributes'])

@pytest.mark.vcr
def test_get_trending_pools(client):
    include = ['base_token', 'quote_token']

    response = client.onchain.get_trending_pools(include=include)

    assert len(response['data']) > 0
    assert (all(key in response['data'][0].keys() for key in ['id', 'type', 'attributes']))
    assert len(response['included']) > 0

@pytest.mark.vcr
def test_get_network_trending_pools(client):
    network = 'eth'

    response = client.onchain.get_network_trending_pools(network=network)

    assert len(response['data']) > 0
    assert 'included' not in response.keys()

@pytest.mark.vcr
def test_get_network_pools_address(client):
    network = 'eth'
    address = '0x60594a405d53811d3bc4766596efd80fd545a270'

    response = client.onchain.get_network_pools_address(network=network, address=address)
    assert len(response['data']) > 0

@pytest.mark.vcr
def test_get_network_pools_address_multi(client):
    network = 'eth'
    addresses = ['0x60594a405d53811d3bc4766596efd80fd545a270', '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640']

    response = client.onchain.get_network_pools_address_multi(network=network, addresses=addresses)

    assert len(response['data']) > 0
    assert addresses[0] in response['data'][0]['id']

@pytest.mark.vcr
def test_get_network_top_pools(client):
    network = 'eth'

    response = client.onchain.get_network_top_pools(network=network)

    assert len(response['data']) > 0
    assert all(key in response['data'][0].keys() for key in ['id', 'type', 'attributes'])

@pytest.mark.vcr
def test_get_network_dexes_top_pools(client):
    network = 'eth'
    dex = 'sushiswap'

    response = client.onchain.get_network_dexes_top_pools(network=network, dex=dex)

    assert len(response['data']) > 0

@pytest.mark.vcr
def test_get_network_new_pools(client):
    network = 'eth'

    response = client.onchain.get_network_new_pools(network=network)

    assert len(response['data']) > 0
    assert all(key in response['data'][0].keys() for key in ['id', 'type', 'attributes'])

@pytest.mark.vcr
def test_get_new_pools(client):
    response = client.onchain.get_new_pools()

    assert len(response['data']) > 0

@pytest.mark.vcr
def test_get_search_pools(client):
    response = client.onchain.get_search_pools(query='ETH')

    assert len(response['data']) > 0
    assert 'eth' in response['data'][0]['id']

@pytest.mark.vcr
def test_get_tokens_top_pool(client):
    network = 'eth'
    token = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'

    response = client.onchain.get_tokens_top_pools(network=network, token_address=token)

    assert len(response['data']) > 0

@pytest.mark.vcr
def test_get_tokens(client):
    network = 'eth'
    address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

    response = client.onchain.get_tokens(network=network, address=address)

    assert address in response['data']['id']

@pytest.mark.vcr
def test_get_tokens_multi(client):
    network = 'eth'
    addresses = ['0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48']

    response = client.onchain.get_tokens_multi(network=network, addresses=addresses)

    assert addresses[0] in response['data'][0]['id']
    assert addresses[1] in response['data'][1]['id']

@pytest.mark.vcr
def test_get_tokens_info(client):
    network = 'eth'
    address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

    response = client.onchain.get_tokens_info(network=network, address=address)

    assert address in response['data']['id']
    assert response['data']['type'] == 'token'

@pytest.mark.vcr
def test_get_tokens_pools_info(client):
    network = 'eth'
    pool_address = '0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852'

    response = client.onchain.get_token_pools_info(network=network, pool_address=pool_address)

    assert len(response['data']) > 0
    assert response['data'][0]['type'] == 'token'

@pytest.mark.vcr
def test_get_tokens_info_recently_updated(client):
    response = client.onchain.get_tokens_info_recently_updated()

    assert len(response['data']) == 100

@pytest.mark.vcr
def test_get_ohlcv(client):
    network = 'eth'
    pool_address = '0x60594a405d53811d3bc4766596efd80fd545a270'
    timeframe = 'day'

    response = client.onchain.get_ohlcv(network=network, pool_address=pool_address, timeframe=timeframe)

    assert len(response['data']['attributes']['ohlcv_list']) > 0

@pytest.mark.vcr
def test_get_trades(client):
    network = 'eth'
    pool_address = '0x60594a405d53811d3bc4766596efd80fd545a270'

    response = client.onchain.get_trades(network=network, pool_address=pool_address)

    assert len(response['data']) > 0
