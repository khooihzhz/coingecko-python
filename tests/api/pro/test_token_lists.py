import pytest

@pytest.mark.vcr
def test_get_all(client):
    response = client.token_lists.get_all(asset_platform_id="ethereum")

    assert response["name"] == "CoinGecko"
    assert len(response["tokens"]) > 0
