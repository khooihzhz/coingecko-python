import pytest

@pytest.mark.vcr
def test_get_list(client):
    expected_keys = [
        'id',
        'contract_address',
        'name',
        'asset_platform_id',
        'symbol'
    ]

    response = client.nfts.get_list()

    assert all(key in response[0].keys() for key in expected_keys)

@pytest.mark.vcr
def test_get_id(client):
    response = client.nfts.get_id(id="pudgy-penguins")

    assert "id" in response.keys()

@pytest.mark.vcr
def test_get_by_contract_address(client):
    response = client.nfts.get_by_contract_address(asset_platform_id="ethereum", contract_address="0xBd3531dA5CF5857e7CfAA92426877b022e612cf8")

    assert "id" in response.keys()
