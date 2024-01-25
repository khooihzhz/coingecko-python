import pytest

@pytest.mark.vcr
def test_get_public_trasuries(client):
    response = client.companies.get_public_trasuries(coin_id='ethereum')

    assert "companies" in response.keys()
    assert "total_holdings" in response.keys()
