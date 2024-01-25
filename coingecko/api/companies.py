from coingecko.api.base import CoinGeckoAPI

class Companies(CoinGeckoAPI):
    def get_public_trasuries(self, coin_id: str = "bitcoin") -> dict:
        """Get public companies bitcoin/ethereum holdings"""
        endpoint = f'companies/public_treasury/{coin_id}'

        return self.get_data(endpoint)
