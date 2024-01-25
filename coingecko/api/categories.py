from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args

class Categories(CoinGeckoAPI):
    @process_function_args
    def get_list(self) -> list:
        """List all categories"""
        endpoint = 'coins/categories/list'

        return self.get_data(endpoint)

    @process_function_args
    def get(self, order: str = "market_cap_desc") -> list:
        """List all categories with market data"""
        endpoint = f'coins/categories'

        params = {
            'order': order
        }

        return self.get_data(endpoint, params=params)
