from coingecko.api import CoinGeckoClient

class CoinGeckoDemoClient(CoinGeckoClient):
    def __init__(self, api_key: str):
        super().__init__(api_key=api_key, pro = False)
