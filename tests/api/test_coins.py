import pytest

@pytest.mark.vcr
def test_get_list(client):
    response = client.coins.get_list()

    assert response is not None
    assert "platforms" not in response[0].keys()

@pytest.mark.vcr
def test_get_list_with_include_platform(client):
    response = client.coins.get_list(include_platform=True)

    assert response is not None
    assert "platforms" in response[0].keys()

@pytest.mark.vcr
def test_get_market(client):
    response = client.coins.get_markets(vs_currency='usd')

    assert len(response) == 100

@pytest.mark.vcr
def test_get_market_with_ids(client):
    response = client.coins.get_markets(vs_currency='usd', ids=['bitcoin', 'ethereum'], per_page=1, page=1)

    assert len(response) == 1
    assert response[0]["id"] == "bitcoin"

    response = client.coins.get_markets(vs_currency='usd', ids=['bitcoin', 'ethereum'], per_page=1, page=2)

    assert len(response) == 1
    assert response[0]["id"] == "ethereum"

@pytest.mark.vcr
def test_get_id(client):
    response = client.coins.get_id(id='bitcoin')

    assert "id" in response.keys()
    assert response["id"] == "bitcoin"

@pytest.mark.vcr
def test_get_tickers(client):
    response = client.coins.get_tickers(id='bitcoin')

    assert response["name"] == "Bitcoin"

@pytest.mark.vcr
def test_get_tickers_with_exchange_ids(client):
    response = client.coins.get_tickers(id='bitcoin', exchange_ids=['binance', 'coinbase-pro'])

    assert response["tickers"][0]["market"]["identifier"] == "binance"

@pytest.mark.vcr
def test_get_history(client):
    response = client.coins.get_history(id='bitcoin', date='30-12-2017')

    assert response["id"] == "bitcoin"

@pytest.mark.vcr
def test_get_market_chart(client):
    response = client.coins.get_market_chart(id='bitcoin', vs_currency='usd', days=1)

    assert len(response["prices"]) > 0

@pytest.mark.vcr
def test_get_market_chart_range(client):
    response = client.coins.get_market_chart_range(id='bitcoin', vs_currency='usd', from_timestamp=1392577232, to_timestamp=1422577232)

    assert len(response["prices"]) > 0

@pytest.mark.vcr
def test_get_ohlc(client):
    response = client.coins.get_ohlc(id='bitcoin', vs_currency='usd', days=1)

    assert len(response) > 0

@pytest.mark.vcr
def test_get_coin_by_contract_address(client):
    response = client.coins.get_coin_by_contract_address(id='ethereum', contract_address='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984')

    assert response["id"] == "uniswap"
    assert response["symbol"] == "uni"
    assert response["contract_address"] == "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"

@pytest.mark.vcr
def test_get_market_chart_by_contract_address(client):
    response = client.coins.get_market_chart_by_contract_address(id='ethereum', contract_address='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', vs_currency='usd', days=1)

    assert len(response["prices"]) > 0

@pytest.mark.vcr
def test_get_market_chart_range_by_contract_address(client):
    response = client.coins.get_market_chart_range_by_contract_address(id='ethereum', contract_address='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984', vs_currency='usd', from_timestamp=1704119444, to_timestamp=1704724250)

    assert len(response["prices"]) > 0
