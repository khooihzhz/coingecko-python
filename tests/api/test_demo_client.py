import pytest
import coingecko
from coingecko.api.error import GeckoAPIUnauthorized

@pytest.mark.vcr
def test_demo_client_with_random_api_key():
    with pytest.raises(GeckoAPIUnauthorized):
        client = coingecko.CoinGeckoDemoClient(api_key="random-key")
        response = client.ping.get()

