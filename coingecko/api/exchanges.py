from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args

class Exchanges(CoinGeckoAPI):
    @process_function_args
    def get(self, per_page: int = None, page: str = None) -> list:
        """List all exchanges"""
        endpoint = 'exchanges'

        params = {
            'per_page': per_page,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    def get_list(self) -> list:
        """List all supported markets id and name (no pagination required)"""
        endpoint = 'exchanges/list'

        return self.get_data(endpoint)

    def get_id(self, id: str) -> dict:
        """Get exchange volume in BTC and Top 100 Tickers only"""
        endpoint = f'exchanges/{id}'

        return self.get_data(endpoint)

    def get_tickers(self, id: str, coin_ids: str = None, include_exchange_logo: bool = False,
                    page: int = None, depth: bool = False, order: str = "trust_score_desc") -> dict:
        """Get exchange tickers (paginated, 100 tickers per page)"""
        endpoint = f'exchanges/{id}/tickers'

        params = {
            'coin_ids': coin_ids,
            'include_exchange_logo': include_exchange_logo,
            'page': page,
            'depth': depth,
            'order': order
        }

        return self.get_data(endpoint, params=params)

    def get_volume_chart(self, id: str, days: str) -> list:
        """Get 24 hour rolling trading volume data (in BTC) for a given exchange"""
        endpoint = f'exchanges/{id}/volume_chart'

        params = {
            'days': days
        }

        return self.get_data(endpoint, params=params)



