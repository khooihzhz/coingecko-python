# Python API wrapper for CoinGecko API
This CoinGecko Python library provides convenient access to CoinGecko API.
## Requirements

- Python 3.0+

## Installations
The recommended way to install coingecko API wrapper is via [pip](https://pypi.python.org/pypi/pip)
```sh
pip install --upgrade coingecko
```
## Quickstart
Before you start, visit [coingecko](https://www.coingecko.com/en/api/pricing) to obtain a demo/paid API key.
After that, you can start using the API by:
```python
import coingecko

# Demo API key
client = coingecko.CoinGeckoDemoClient(api_key=<insert_your_demo_api_key>)

# Paid API key
client = coingecko.CoinGeckoProClient(api_key=<insert_your_paid_api_key>)

# Test your API key with ping
response = client.ping.get()
```

## License
The library is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
