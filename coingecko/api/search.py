from coingecko.api.base import CoinGeckoAPI

class Search(CoinGeckoAPI):
    def get(self, query: str) -> dict:
        """Search for coins, categories and markets on CoinGecko"""
        endpoint = 'search'

        params = {
            'query': query
        }

        return self.get_data(endpoint, params=params)

    def get_trending(self) -> dict:
        """Get trending search coins (Top-15) on CoinGecko in the Last 24 Hours"""
        endpoint = 'search/trending'

        return self.get_data(endpoint)
