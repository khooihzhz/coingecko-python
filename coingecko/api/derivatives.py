from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args

class Derivatives(CoinGeckoAPI):
    def get(self) -> list:
        """List all derivative tickers"""
        endpoint = 'derivatives'

        return self.get_data(endpoint)

    def get_exchanges(self, order: str = None, per_page: int = None, page: int = None) -> list:
        """List all derivative exchanges"""
        endpoint = 'derivatives/exchanges'

        params = {
            'order': order,
            'per_page': per_page,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    def get_exchanges_id(self, id: str, include_tickers: str = None) -> dict:
        """Show derivative exchange data"""
        endpoint = f'derivatives/exchanges/{id}'

        params = {
            'include_tickers': include_tickers
        }

        return self.get_data(endpoint, params=params)

    def get_exchanges_list(self) -> list:
        """List all derivative exchanges name and identifier"""
        endpoint = 'derivatives/exchanges/list'

        return self.get_data(endpoint)
