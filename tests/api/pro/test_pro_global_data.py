import pytest

@pytest.mark.vcr
def test_get_market_cap_chart(client):
    response = client.global_data.get_market_cap_chart(days=1)

    assert "market_cap_chart" in response.keys()
