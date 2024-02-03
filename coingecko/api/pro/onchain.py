from coingecko.api.base import CoinGeckoAPI
from typing import Union, List
from coingecko.api.utils import process_function_args

class Onchain(CoinGeckoAPI):
    @process_function_args
    def get_simple_token_price(self, network: str, addresses: Union[str, list]) -> dict:
        """Get current USD prices of multiple tokens on a network"""
        endpoint = f'onchain/simple/networks/{network}/token_price/{addresses}'

        params = {
            'network': network,
            'contract_addresses': addresses
        }

        return self.get_data(endpoint, params=params)

    def get_networks(self, page: int = 1) -> dict:
        """Get list of supported networks"""
        endpoint = 'onchain/networks'

        params = {
            'page': page
        }

        return self.get_data(endpoint, params=params)

    def get_dexes(self, network: str, page: int = 1) -> dict:
        """Get list of supported dexes on a network"""
        endpoint = f'onchain/networks/{network}/dexes'

        params = {
            'network': network,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_trending_pools(self, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get trending pools across all networks"""
        endpoint = 'onchain/networks/trending_pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_network_trending_pools(self, network: str, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get trending pools on a network"""
        endpoint = f'onchain/networks/{network}/trending_pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_network_pools_address(self, network: str, address: str, include: Union[str, List[str]] = None) -> dict:
        """Get specific pools on a network"""
        endpoint = f'onchain/networks/{network}/pools/{address}'

        params = {
            'include': include
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_network_pools_address_multi(self, network: str, addresses: Union[str, List[str]], include: Union[str, List[str]] = None) -> dict:
        """Get multiple pools on a network"""
        endpoint = f'onchain/networks/{network}/pools/multi/{addresses}'

        params = {
            'include': include
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_network_top_pools(self, network: str, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get top pools on a network"""
        endpoint = f'onchain/networks/{network}/pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)


    @process_function_args
    def get_network_dexes_top_pools(self, network: str, dex: str, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get top pools on a network's dex"""
        endpoint = f'onchain/networks/{network}/dexes/{dex}/pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_network_new_pools(self, network: str, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get latest pools on a network"""
        endpoint = f'onchain/networks/{network}/new_pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_new_pools(self, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get latest pools across all networks"""
        endpoint = 'onchain/networks/new_pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_search_pools(self, query: str = None, network: str = None, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Search for pools on a network"""
        endpoint = 'onchain/search/pools'

        params = {
            'query': query,
            'network': network,
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_tokens_top_pools(self, network: str, token_address: str, include: Union[str, List[str]] = None, page: int = 1) -> dict:
        """Get top pools for a token"""
        endpoint = f'onchain/networks/{network}/tokens/{token_address}/pools'

        params = {
            'include': include,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_tokens(self, network: str, address: str, include: Union[str, List[str]] = None) -> dict:
        """Get specific tokens on a network"""
        endpoint = f'onchain/networks/{network}/tokens/{address}'

        params = {
            'include': include
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_tokens_multi(self, network: str, addresses: Union[str, List[str]], include: Union[str, List[str]] = None) -> dict:
        """Get multiple tokens on a network"""
        endpoint = f'onchain/networks/{network}/tokens/multi/{addresses}'

        params = {
            'include': include
        }

        return self.get_data(endpoint, params=params)

    def get_tokens_info(self, network: str, address: str)-> dict:
        """Get specific tokens on a network"""
        endpoint = f'onchain/networks/{network}/tokens/{address}'

        return self.get_data(endpoint)

    def get_token_pools_info(self, network: str, pool_address: str) -> dict:
        """Get pool tokens info on a network"""
        endpoint = f'onchain/networks/{network}/pools/{pool_address}/info'

        return self.get_data(endpoint)

    @process_function_args
    def get_tokens_info_recently_updated(self, include: Union[str, List[str]] = None) -> dict:
        """Get most recently updated 100 tokens info across all networks"""
        endpoint = 'onchain/tokens/info_recently_updated'

        params = {
            'include': include
        }

        return self.get_data(endpoint, params=params)

    def get_ohlcv(self, network: str, pool_address: str, timeframe: str, aggregate: int = 1, before_timestamp: Union[int, str] = None,
                  limit: int = 100, currency: str = "usd", token: str = "base") -> dict:
        """Get OHLCV data of a pool, up to 6 months ago. Empty data if there is no earlier data available."""
        endpoint = f'onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}'

        params = {
            'aggregate': aggregate,
            'before_timestamp': before_timestamp,
            'limit': limit,
            'currency': currency,
            'token': token
        }

        return self.get_data(endpoint, params=params)

    def get_trades(self, network: str, pool_address: str, trade_volume_in_usd_greater_than: Union[int, str] = 0):
        """Get last 300 trades in past 24 hour of a pool"""
        endpoint = f'onchain/networks/{network}/pools/{pool_address}/trades'

        params = {
            'trade_volume_in_usd_greater_than': trade_volume_in_usd_greater_than
        }

        return self.get_data(endpoint, params=params)


