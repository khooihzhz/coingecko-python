import pytest

EXPECTED_KEYS = ["id", "name", "shortname", "chain_identifier", "native_coin_id"]

@pytest.mark.vcr
def test_get(client):
    response = client.asset_platform.get()

    assert len(response) > 0
    assert all(key in response[0].keys() for key in EXPECTED_KEYS)

@pytest.mark.vcr
def test_get_with_params(client):
    response = client.asset_platform.get(filter='nft')

    assert len(response) > 0
    assert all(key in response[0].keys() for key in EXPECTED_KEYS)

