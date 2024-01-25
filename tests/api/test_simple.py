import pytest

@pytest.mark.vcr
def test_get_price(client):
    response = client.simple.get_price(ids='bitcoin', vs_currencies='usd')

    assert 'bitcoin' in response.keys()

@pytest.mark.vcr
def test_get_price_with_precision(client):
    response = client.simple.get_price(ids='bitcoin', vs_currencies='usd', precision=2)

    assert 'bitcoin' in response.keys()

@pytest.mark.vcr
def test_get_token_price(client):
    response = client.simple.get_token_price(id='ethereum', contract_addresses='0xdac17f958d2ee523a2206206994597c13d831ec7', vs_currencies='usd')

    assert '0xdac17f958d2ee523a2206206994597c13d831ec7' in response.keys()

@pytest.mark.vcr
def test_get_supported_vs_currencies(client):
    response = client.simple.get_supported_vs_currencies()

    assert len(response) > 0
