import pytest

@pytest.mark.vcr
def test_get(client):
    response = client.exchange_rates.get()

    assert "rates" in response.keys()
