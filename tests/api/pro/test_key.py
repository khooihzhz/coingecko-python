import pytest

@pytest.mark.vcr
def test_get(client):
    response = client.key.get()

    assert 'plan' in response.keys()
    assert 'rate_limit_request_per_minute' in response.keys()

