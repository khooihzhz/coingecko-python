import pytest

@pytest.mark.vcr
def test_get(client):
    expected_keys = [
        'market',
        'symbol',
        'index_id',
        'price',
        'price_percentage_change_24h',
        'contract_type',
        'index',
        'basis',
        'spread',
        'funding_rate',
        'open_interest',
        'volume_24h',
        'last_traded_at',
        'expired_at'
    ]

    response = client.derivatives.get()

    assert all(key in response[0].keys() for key in expected_keys)

@pytest.mark.vcr
def test_get_exchanges(client):
    expected_keys = [
        'name',
        'id',
        'open_interest_btc',
        'trade_volume_24h_btc',
        'number_of_perpetual_pairs',
        'number_of_futures_pairs',
        'image',
        'country',
        'description',
        'url'
    ]

    response = client.derivatives.get_exchanges()

    assert all(key in response[0].keys() for key in expected_keys)

@pytest.mark.vcr
def test_get_exchanges_id(client):
    expected_keys = [
        'name',
        'open_interest_btc',
        'trade_volume_24h_btc',
        'number_of_perpetual_pairs',
        'number_of_futures_pairs',
        'image',
        'year_established',
        'country',
        'description',
        'url'
    ]

    response = client.derivatives.get_exchanges_id(id="bitmex")

    assert all(key in response.keys() for key in expected_keys)

@pytest.mark.vcr
def test_get_exchanges_list(client):
    expected_keys = [
        'name',
        'id'
    ]

    response = client.derivatives.get_exchanges_list()

    assert all(key in response[0].keys() for key in expected_keys)


