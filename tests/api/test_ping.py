import pytest

@pytest.mark.vcr
def test_get(client):
    response = client.ping.get()
    assert response.keys() == {'gecko_says'}
