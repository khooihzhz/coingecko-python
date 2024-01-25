import pytest
import coingecko
import os

@pytest.fixture
def client():
    api_key = os.environ.get('X_CG_PRO_API_KEY')
    if not api_key:
        raise Exception('Please set X_CG_PRO_API_KEY in your environment')
    return coingecko.CoinGeckoProClient(api_key=api_key)

@pytest.fixture
def vcr_config():
    return {"filter_headers": [("X-CG-PRO-API-KEY"),]}
