from coingecko.api.base import CoinGeckoAPI
from typing import List, Union
from coingecko.api.utils import process_function_args

class Simple(CoinGeckoAPI):
    @process_function_args
    def get_price(self, ids: Union[str, List[str]], vs_currencies: Union[str, List[str]],
                         include_market_cap: bool = False,
                         include_24hr_vol: bool = False, include_24hr_change: bool = False,
                         include_last_updated_at: bool = False, precision: Union[str, int] = None) -> dict:
        """Get current price of any cryptocurrency in any other currency that you need."""
        endpoint = 'simple/price'

        params = {
            'ids': ids,
            'vs_currencies': vs_currencies,
            'include_market_cap': include_market_cap,
            'include_24hr_vol': include_24hr_vol,
            'include_24hr_change': include_24hr_change,
            'include_last_updated_at': include_last_updated_at,
            'precision': precision
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_token_price(self, id: str, contract_addresses: Union[str, List[str]], vs_currencies: Union[str, List[str]],
                                  include_market_cap: bool = False,
                                  include_24hr_vol: bool = False, include_24hr_change: bool = False,
                                  include_last_updated_at: bool = False, precision: Union[str, int] = None) -> dict:
        """Get current price of tokens for a given platform in any other currency that you need."""
        endpoint = f'simple/token_price/{id}'

        params = {
            'contract_addresses': contract_addresses,
            'vs_currencies': vs_currencies,
            'include_market_cap': include_market_cap,
            'include_24hr_vol': include_24hr_vol,
            'include_24hr_change': include_24hr_change,
            'include_last_updated_at': include_last_updated_at,
            'precision': precision
        }

        return self.get_data(endpoint, params=params)


    def get_supported_vs_currencies(self) -> list:
        """Get list of supported_vs_currencies."""
        endpoint = 'simple/supported_vs_currencies'

        return self.get_data(endpoint)

