from coingecko.api.nfts import Nfts
from typing import Union

class ProNfts(Nfts):
    def get_markets(self, asset_platform_id: str = None, order: str = "market_cap_usd_desc", per_page: int = 100, page: int = 1) -> list:
        """🖼️ Get the list of all supported NFT floor price, market cap, volume and market related data on CoinGecko"""
        endpoint = 'nfts/markets'

        params = {
            'asset_platform_id': asset_platform_id,
            'order': order,
            'per_page': per_page,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    def get_market_chart(self, id: str, days: Union[str, int]) -> list:
        """📈 Get historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now."""

        endpoint = f'nfts/{id}/market_chart'

        params = {
            'days': days
        }

        return self.get_data(endpoint, params=params)

    def get_market_chart_by_contract_address(self, asset_platform_id: str, contract_address: str, days: Union[str, int]) -> dict:
        """📈  Get historical market data of a NFT collection using contract address, including floor price, market cap, and 24h volume, by number of days away from now."""

        endpoint = f'nfts/{asset_platform_id}/contract/{contract_address}/market_chart'

        params = {
            'days': days
        }

        return self.get_data(endpoint, params=params)

    def get_tickers(self, id: str) -> dict:
        """🖼️ Get the latest floor price and 24h volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and Looksrare."""

        endpoint = f'nfts/{id}/tickers'

        return self.get_data(endpoint)


