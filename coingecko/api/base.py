import requests
import logging
from coingecko.api.error import CoinGeckoAPIErrorHandler

class CoinGeckoAPI:
    __PRO_API_BASE_URL = 'https://pro-api.coingecko.com/api/v3'
    __API_BASE_URL = 'https://api.coingecko.com/api/v3'

    def __init__(self, api_key: str, pro: bool = False, session: requests.Session = None):
        if not api_key:
            raise ValueError("API key is required.")

        self.api_key = api_key
        self.base_url = self.__PRO_API_BASE_URL if pro else self.__API_BASE_URL
        self.api_key_header = 'x-cg-pro-api-key' if pro else 'x-cg-demo-api-key'
        self.session = session or requests.Session()

    def get_data(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        headers = {'Content-Type': 'application/json', f'{self.api_key_header}': self.api_key, 'User-Agent': 'coingecko/python'}

        response = self.session.get(url, headers=headers, params=params)
        logging.info(f"GET {url} : {response.status_code}")

        if response.status_code == 200:
            return response.json()
        else:
            CoinGeckoAPIErrorHandler.handle_response(response)
