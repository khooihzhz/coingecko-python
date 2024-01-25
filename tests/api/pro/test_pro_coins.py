import pytest

@pytest.mark.vcr
def test_get_list_new(client):
    response = client.coins.get_list_new()

    assert isinstance(response, list)

@pytest.mark.vcr
def test_get_top_gainers_losers(client):
    response = client.coins.get_top_gainers_losers(vs_currency="usd")

    assert "top_gainers" in response.keys()
    assert "top_losers" in response.keys()

@pytest.mark.vcr
def test_get_circulating_supply_chart(client):
    response = client.coins.get_circulating_supply_chart(id="bitcoin", days=1)

    assert "circulating_supply" in response.keys()

@pytest.mark.vcr
def test_get_circulating_supply_chart_range(client):
    response = client.coins.get_circulating_supply_chart_range(id="bitcoin", from_timestamp=1704119444, to_timestamp=1704724250)

    assert "circulating_supply" in response.keys()

@pytest.mark.vcr
def test_get_total_supply_chart(client):
    response = client.coins.get_total_supply_chart(id="bitcoin", days=1)

    assert "total_supply" in response.keys()

@pytest.mark.vcr
def test_get_total_supply_chart_range(client):
    response = client.coins.get_total_supply_chart_range(id="bitcoin", from_timestamp=1392577232, to_timestamp=1422577232)

    assert "total_supply" in response.keys()


@pytest.mark.vcr
def test_get_market_chart_5_minutely(client):
    response = client.coins.get_market_chart(id="bitcoin", vs_currency="usd", days=1, interval="5m")

    assert len(response["prices"]) > 0

@pytest.mark.vcr
def test_get_market_chart_range_5_minutely(client):
    response = client.coins.get_market_chart_range(id="bitcoin", vs_currency="usd", from_timestamp=1704119444, to_timestamp=1704724250, interval="5m")

    assert len(response["prices"]) > 0

@pytest.mark.vcr
def test_get_market_chart_by_contract_address_5_minutely(client):
    response = client.coins.get_market_chart_by_contract_address(id="ethereum", contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984", vs_currency="usd", days=1, interval="5m")

    assert len(response["prices"]) > 0


@pytest.mark.vcr
def test_get_market_chart_range_by_contract_address_5_minutely(client):
    response = client.coins.get_market_chart_range_by_contract_address(id="ethereum", contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984", vs_currency="usd", from_timestamp=1704119444, to_timestamp=1704724250, interval="5m")

    assert len(response["prices"]) > 0
