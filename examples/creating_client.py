import coingecko
import os

# Demo API
api_key = os.environ.get('X_CG_DEMO_API_KEY')
client = coingecko.CoinGeckoDemoClient(api_key=api_key)

# Paid API
api_key = os.environ.get('X_CG_PRO_API_KEY')
client = coingecko.CoinGeckoProClient(api_key=api_key)

# Ping!
response = client.ping.get()
