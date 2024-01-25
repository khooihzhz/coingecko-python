from .ping import Ping
from .simple import Simple
from .coins import Coins
from .asset_platform import AssetPlatform
from .categories import Categories
from .exchanges import Exchanges
from .derivatives import Derivatives
from .nfts import Nfts
from .exchange_rates import ExchangeRates
from .global_data import GlobalData
from .search import Search
from .companies import Companies
import requests

class CoinGeckoClient:
    def __init__(self, api_key: str, pro: bool = False):
        self.api_key = api_key
        self.pro = pro
        self.session = requests.Session()
        self._ping = None
        self._simple = None
        self._coins = None
        self._asset_platform = None
        self._categories = None
        self._exchanges = None
        self._derivatives = None
        self._nfts = None
        self._exchange_rates = None
        self._global_data = None
        self._search = None
        self._companies = None

    @property
    def ping(self):
        if self._ping is None:
            self._ping = Ping(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._ping

    @property
    def simple(self):
        if self._simple is None:
            self._simple = Simple(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._simple

    @property
    def coins(self):
        if self._coins is None:
            self._coins = Coins(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._coins

    @property
    def asset_platform(self):
        if self._asset_platform is None:
            self._asset_platform = AssetPlatform(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._asset_platform

    @property
    def categories(self):
        if self._categories is None:
            self._categories = Categories(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._categories

    @property
    def exchanges(self):
        if self._exchanges is None:
            self._exchanges = Exchanges(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._exchanges

    @property
    def derivatives(self):
        if self._derivatives is None:
            self._derivatives = Derivatives(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._derivatives

    @property
    def nfts(self):
        if self._nfts is None:
            self._nfts = Nfts(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._nfts

    @property
    def exchange_rates(self):
        if self._exchange_rates is None:
            self._exchange_rates = ExchangeRates(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._exchange_rates

    @property
    def global_data(self):
        if self._global_data is None:
            self._global_data = GlobalData(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._global_data

    @property
    def search(self):
        if self._search is None:
            self._search = Search(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._search

    @property
    def companies(self):
        if self._companies is None:
            self._companies = Companies(api_key=self.api_key, pro=self.pro, session=self.session)
        return self._companies
