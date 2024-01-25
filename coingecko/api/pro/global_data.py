from coingecko.api.global_data import GlobalData
from typing import Union


class ProGlobalData(GlobalData):
    def get_market_cap_chart(self, days: Union[str, int], vs_currency: str = 'usd') -> dict:
        """📈 Get historical global market cap and volume data, by number of days away from now."""
        endpoint = 'global/market_cap_chart'

        params = {
            'vs_currency': vs_currency,
            'days': days
        }

        return self.get_data(endpoint, params=params)
