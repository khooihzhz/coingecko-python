from coingecko.api.base import CoinGeckoAPI

class Ping(CoinGeckoAPI):
    """ Check API server status """
    def get(self):
        endpoint = 'ping'

        return self.get_data(endpoint)
