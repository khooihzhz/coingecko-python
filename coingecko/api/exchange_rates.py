from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args

class ExchangeRates(CoinGeckoAPI):
    def get(self) -> dict:
        """Get BTC-to-Currency exchange rates"""
        endpoint = 'exchange_rates'

        return self.get_data(endpoint)
