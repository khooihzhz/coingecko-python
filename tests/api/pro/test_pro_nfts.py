import pytest

@pytest.mark.vcr
def test_get_markets(client):
    response = client.nfts.get_markets()

    assert len(response) > 0

@pytest.mark.vcr
def test_get_market_chart(client):
    response = client.nfts.get_market_chart(id="pudgy-penguins", days="1")

    assert "floor_price_usd" in response.keys()

@pytest.mark.vcr
def test_get_market_chart_by_contract_address(client):
    response = client.nfts.get_market_chart_by_contract_address(asset_platform_id="ethereum", contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8", days="1")

    assert "floor_price_usd" in response.keys()

@pytest.mark.vcr
def test_get_tickers(client):
    response = client.nfts.get_tickers(id="pudgy-penguins")

    assert "tickers" in response.keys()
