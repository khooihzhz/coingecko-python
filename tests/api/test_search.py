import pytest

@pytest.mark.vcr

def test_get(client):
    response = client.search.get(query="bitcoin")

    assert "coins" in response.keys()

@pytest.mark.vcr
def test_get_trending(client):
    response = client.search.get_trending()

    assert "coins" in response.keys()

