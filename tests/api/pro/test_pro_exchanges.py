import pytest

@pytest.mark.vcr
def test_get_volume_chart_range(client):
    response = client.exchanges.get_volume_chart_range(id="binance", from_timestamp=1673222400, to_timestamp=1675814400)

    assert len(response) > 0
