import pytest

@pytest.mark.vcr
def test_get(client):
    expected_keys = [
        'id',
        'name',
        'year_established',
        'country',
        'description',
        'url',
        'image',
        'has_trading_incentive',
        'trust_score',
        'trust_score_rank',
        'trade_volume_24h_btc',
        'trade_volume_24h_btc_normalized'
    ]

    response = client.exchanges.get()

    assert all(key in response[0].keys() for key in expected_keys)

@pytest.mark.vcr
def test_get_list(client):
    expected_keys = [
        'id',
        'name'
    ]

    response = client.exchanges.get_list()

    assert all(key in response[0].keys() for key in expected_keys)

@pytest.mark.vcr
def test_get_id(client):
    response = client.exchanges.get_id('binance')

    assert response['name'] == 'Binance'

@pytest.mark.vcr
def test_get_tickers(client):
    response = client.exchanges.get_tickers('binance')

    assert response['name'] == 'Binance'
    assert 'tickers' in response.keys()

@pytest.mark.vcr
def test_get_volume_chart(client):
    response = client.exchanges.get_volume_chart('binance', '1')

    assert len(response) > 0
