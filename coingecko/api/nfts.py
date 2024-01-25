from coingecko.api.base import CoinGeckoAPI
from coingecko.api.utils import process_function_args

class Nfts(CoinGeckoAPI):
    def get_list(self, order: str = None, asset_platform_id: str = None, per_page: int = 100, page: int = 1) -> list:
        """List all supported NFT ids, paginated by 100 items per page, paginated to 100 items"""
        endpoint = 'nfts/list'

        params = {
            'order': order,
            'asset_platform_id': asset_platform_id,
            'per_page': per_page,
            'page': page
        }

        return self.get_data(endpoint, params=params)

    def get_id(self, id: str) -> dict:
        """Get currnet data (name, price_floor, volume_24h) for an NFT collection"""
        endpoint = f'nfts/{id}'

        return self.get_data(endpoint)

    def get_by_contract_address(self, asset_platform_id: str, contract_address: str) -> dict:
        """Get currnet data (name, price_floor, volume_24h) for an NFT collection"""
        endpoint = f'nfts/{asset_platform_id}/contract/{contract_address}'

        return self.get_data(endpoint)
