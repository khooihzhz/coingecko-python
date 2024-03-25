from coingecko.api import CoinGeckoClient
from coingecko.api.pro.coins import ProCoins
from coingecko.api.pro.global_data import ProGlobalData
from coingecko.api.pro.exchanges import ProExchanges
from coingecko.api.pro.nfts import ProNfts
from coingecko.api.pro.token_lists import TokenLists
from coingecko.api.pro.onchain import Onchain
from coingecko.api.pro.key import Key

class CoinGeckoProClient(CoinGeckoClient):
    def __init__(self, api_key: str):
        super().__init__(api_key=api_key, pro = True)
        self._coins = None
        self._global_data = None
        self._nfts = None
        self._exchanges = None
        self._token_lists = None
        self._onchain = None
        self._key = None

    @property
    def coins(self):
        if self._coins is None:
            self._coins = ProCoins(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._coins

    @property
    def global_data(self):
        if self._global_data is None:
            self._global_data = ProGlobalData(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._global_data

    @property
    def exchanges(self):
        if self._exchanges is None:
            self._exchanges = ProExchanges(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._exchanges

    @property
    def nfts(self):
        if self._nfts is None:
            self._nfts = ProNfts(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._nfts

    @property
    def token_lists(self):
        if self._token_lists is None:
            self._token_lists = TokenLists(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._token_lists

    @property
    def onchain(self):
        if self._onchain is None:
            self._onchain = Onchain(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._onchain

    @property
    def key(self):
        if self._key is None:
            self._key = Key(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._key
