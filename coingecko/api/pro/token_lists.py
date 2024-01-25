from coingecko.api.base import CoinGeckoAPI

class TokenLists(CoinGeckoAPI):
    def get_all(self, asset_platform_id: str) -> dict:
        """🪙 Get full list of tokens of a blockchain network (asset platform) that is supported by Ethereum token list standard."""

        endpoint = f'token_lists/{asset_platform_id}/all.json'

        return self.get_data(endpoint)
