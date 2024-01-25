from coingecko.api.exchanges import Exchanges

class ProExchanges(Exchanges):
    def get_volume_chart_range(self, id: str, from_timestamp: str, to_timestamp: str) -> list:
        """📈 Get historical volume data (in BTC) of an exchange, by specifying a date range (up to 31 days per call)"""

        endpoint = f'exchanges/{id}/volume_chart/range'

        params = {
            'from': from_timestamp,
            'to': to_timestamp
        }

        return self.get_data(endpoint, params=params)
