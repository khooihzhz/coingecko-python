from coingecko.api.coins import Coins
from typing import Union

class ProCoins(Coins):
    def get_list_new(self) -> list:
        """🪙 Get the latest 200 coins (id & activated time) that recently listed on CoinGecko.com."""
        endpoint = 'coins/list/new'

        return self.get_data(endpoint)

    def get_top_gainers_losers(self, vs_currency: str, duration: str = "24h", top_coins: Union[int, str] = 1000) -> dict:
        """📈 get the top 30 coins with largest price gain and loss by a specific time duration"""
        endpoint = 'coins/top_gainers_losers'

        params = {
            'vs_currency': vs_currency,
            'duration': duration,
            'top_coins': top_coins
        }

        return self.get_data(endpoint, params=params)

    def get_circulating_supply_chart(self, id: str, days: Union[str, int], interval: str = None) -> dict:
        """📈 Get historical circulating supply of a coin, by number of days away from now."""
        endpoint = f'coins/{id}/circulating_supply_chart'

        params = {
            'days': days,
            'interval': interval
        }

        return self.get_data(endpoint, params=params)

    def get_circulating_supply_chart_range(self, id: str, from_timestamp: Union[str, int], to_timestamp: Union[str, int]) -> dict:
        """📈 Get historical circulating supply of a coin, within a range of timestamp."""
        endpoint = f'coins/{id}/circulating_supply_chart/range'

        params = {
            'from': from_timestamp,
            'to': to_timestamp
        }

        return self.get_data(endpoint, params=params)

    def get_total_supply_chart(self, id: str, days: Union[str, int], interval: str = None) -> dict:
        """📈 Get historical total supply of a coin, by number of days away from now."""
        endpoint = f'coins/{id}/total_supply_chart'

        params = {
            'days': days,
            'interval': interval
        }

        return self.get_data(endpoint, params=params)

    def get_total_supply_chart_range(self, id: str, from_timestamp: Union[str, int], to_timestamp: Union[str, int]) -> dict:
        """📈 Get historical total supply of a coin, within a range of timestamp."""
        endpoint = f'coins/{id}/total_supply_chart/range'

        params = {
            'from': from_timestamp,
            'to': to_timestamp
        }

        return self.get_data(endpoint, params=params)
