from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args


class AssetPlatform(CoinGeckoAPI):
    def get(self, filter: str = None) -> list:
        """List all asset platforms"""
        endpoint = 'asset_platforms'

        params = {
            'filter': filter
        }

        return self.get_data(endpoint, params=params)

