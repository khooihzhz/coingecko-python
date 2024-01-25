import pytest

@pytest.mark.vcr
def test_get_list(client):
    response = client.categories.get_list()

    assert len(response) > 0
    assert "name" in response[0].keys()
    assert "category_id" in response[0].keys()

EXPECTED_KEYS = ["id", "name", "market_cap", "market_cap_change_24h", "content", "top_3_coins", "volume_24h", "updated_at"]

@pytest.mark.vcr
def test_get(client):
    response = client.categories.get()

    assert all(key in response[0].keys() for key in EXPECTED_KEYS)

