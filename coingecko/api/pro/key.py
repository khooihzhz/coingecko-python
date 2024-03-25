from coingecko.api.base import CoinGeckoAPI

class Key(CoinGeckoAPI):
    endpoint = 'key'

    def get(self) -> dict:
        """return API key plan details and credit balances"""
        return self.get_data(self.endpoint)
