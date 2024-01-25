import pytest

@pytest.mark.vcr
def test_get(client):
    response = client.global_data.get()

    assert "data" in response.keys()

@pytest.mark.vcr
def test_get_defi(client):
    response = client.global_data.get_defi()

    assert "data" in response.keys()
