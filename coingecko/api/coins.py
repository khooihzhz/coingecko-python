from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args
from typing import List, Union

class Coins(CoinGeckoAPI):
    @process_function_args
    def get_list(self, include_platform: bool = False) -> list:
        """List all supported coins id, name and symbol (no pagination required)"""
        endpoint = 'coins/list'

        params = {
            'include_platform': include_platform
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_markets(self, vs_currency: str, ids: Union[str, List[str]] = None,
                        category: str = None, order: str = "market_cap_desc", per_page: int = 100,
                        page: int = 1, sparkline: bool = False, price_change_percentage: str = None,
                        locale: str = "en", precision: Union[str, int] = None) -> list:
        """List all supported coins price, market cap, volume, and market related data"""
        endpoint = 'coins/markets'

        params = {
            'vs_currency': vs_currency,
            'ids': ids,
            'category': category,
            'order': order,
            'per_page': per_page,
            'page': page,
            'sparkline': sparkline,
            'price_change_percentage': price_change_percentage,
            'locale': locale,
            'precision': precision,
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_id(self, id: str, localization: bool = True, tickers: bool = True,
                      include_exchange_logo: bool = False, market_data: bool = True,
                      community_data: bool = True, developer_data: bool = True,
                      description_data: bool = True, sparkline: bool = False) -> dict:
        """Get current data (name, price, market, ... including exchange tickers) for a coin"""
        endpoint = f'coins/{id}'

        params = {
            'localization': localization,
            'tickers': tickers,
            'include_exchange_logo': include_exchange_logo,
            'market_data': market_data,
            'community_data': community_data,
            'developer_data': developer_data,
            'description_data': description_data,
            'sparkline': sparkline
        }


        return self.get_data(endpoint, params=params)

    # Note: To handle pagination later
    @process_function_args
    def get_tickers(self, id: str, exchange_ids: Union[str, List[str]] = None,
                        include_exchange_logo: bool = False, page: int = None,
                        order: str = "trust_score_desc", depth: bool = False) -> dict:
        """Get coin tickers (paginated to 100 items)"""
        endpoint = f'coins/{id}/tickers'

        params = {
            'exchange_ids': exchange_ids,
            'include_exchange_logo': include_exchange_logo,
            'page': page,
            'order': order,
            'depth': depth
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_history(self, id: str, date: str, localization: bool = None) -> dict:
        """Get historical data (name, price, market, stats) at a given date for a coin"""
        endpoint = f'coins/{id}/history'

        params = {
            'date': date,
            'localization': localization
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_market_chart(self, id: str, vs_currency: str, days: Union[str, int],
                             interval: str = None, precision: Union[str, int] = None) -> dict:
        """Get historical market data include price, market cap, and 24h volume (granularity auto)"""
        endpoint = f'coins/{id}/market_chart'

        params = {
            'vs_currency': vs_currency,
            'days': days,
            'interval': interval,
            'precision': precision
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_market_chart_range(self, id: str, vs_currency: str, from_timestamp: Union[str, int],
                                   to_timestamp: Union[str, int], interval: str = None, precision: Union[str, int] = None) -> dict:
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)"""
        endpoint = f'coins/{id}/market_chart/range'

        params = {
            'vs_currency': vs_currency,
            'from': from_timestamp,
            'to': to_timestamp,
            'interval': interval,
            'precision': precision
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_ohlc(self, id: str, vs_currency: str, days: Union[str, int],
                     interval: str = None, precision: Union[str, int] = None) -> dict:
        """Get coin's OHLC (candlestick) data"""
        endpoint = f'coins/{id}/ohlc'

        params = {
            'vs_currency': vs_currency,
            'days': days,
            'interval': interval
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_coin_by_contract_address(self, id: str, contract_address: str) -> dict:
        """Get coin info from contract address"""
        endpoint = f'coins/{id}/contract/{contract_address}'

        return self.get_data(endpoint)

    @process_function_args
    def get_market_chart_by_contract_address(self, id: str, contract_address: str, vs_currency: str,
                                                 days: Union[str, int], interval: str = None,
                                                 precision: [str, int] = None) -> dict:
        """Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address"""
        endpoint = f'coins/{id}/contract/{contract_address}/market_chart'

        params = {
            'vs_currency': vs_currency,
            'days': days,
            'interval': interval,
            'precision': precision
        }

        return self.get_data(endpoint, params=params)

    @process_function_args
    def get_market_chart_range_by_contract_address(self, id: str, contract_address: str, vs_currency: str,
                                                       from_timestamp: Union[str, int], to_timestamp: Union[str, int],
                                                       interval: str = None,
                                                       precision: Union[str, int] = None) -> dict:
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address"""
        endpoint = f'coins/{id}/contract/{contract_address}/market_chart/range'

        params = {
            'vs_currency': vs_currency,
            'from': from_timestamp,
            'to': to_timestamp,
            'interval': interval,
            'precision': precision
        }

        return self.get_data(endpoint, params=params)
