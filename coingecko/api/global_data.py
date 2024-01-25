from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args

class GlobalData(CoinGeckoAPI):
    def get(self) -> dict:
        """Get cryptocurrency global data"""
        endpoint = 'global'

        return self.get_data(endpoint)

    def get_defi(self) -> dict:
        """Get cryptocurrency global decentralized finance(defi) data"""
        endpoint = 'global/decentralized_finance_defi'

        return self.get_data(endpoint)
