![PyPI](https://img.shields.io/pypi/v/coingecko?label=coingecko-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/coingecko)
# Python API wrapper for CoinGecko API
This CoinGecko Python library provides convenient access to CoinGecko API.
## Requirements

- Python 3.0+
- [requests](https://pypi.org/project/requests/)

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

## Documentation
For the list of endpoints and information, visit [CoinGecko API Documentation](https://docs.coingecko.com/)

## Examples
The default values and parameter namings for each endpoints follows the official [documentation](https://docs.coingecko.com/).
#### Making your first API Call, PING!
```python
response = client.ping.get()
# -> {'gecko_says': '(V3) To the Moon!'}
```

#### Just want to get price? Simple!
```python
# /simple/price - one coin_id/currency
response = client.simple.get_price(ids='bitcoin', vs_currencies='usd')
# -> {'bitcoin': {'usd': 40067}}
```

#### Use List from Python instead of comma separated strings!
```python
# /simple/price - multiple coin_ids (pass in a list of strings)
response = client.simple.get_price(ids=['bitcoin', 'ethereum'], vs_currencies=['usd', 'myr'])
# -> {'bitcoin': {'usd': 40067, 'myr': 189478}, 'ethereum': {'usd': 2223.37, 'myr': 10514.34}}
```

#### Use booleans instead of string for "true"/"false"
```python
# /simple/price - pass in booleans instead of string
response = client.simple.get_price(ids='bitcoin', vs_currencies='usd', include_24hr_vol=True)
# -> {'bitcoin': {'usd': 40067, 'usd_24h_vol': 16742608673.077057}}
```

#### For precisions, use Integer/Strings
```python
# simple/price - precision accepts integer/string
response = client.simple.get_price(ids='bitcoin', vs_currencies='usd', precision=2)
# -> {'bitcoin': {'usd': 40066.81}}

response = client.simple.get_price(ids='bitcoin', vs_currencies='usd', precision="2")
# {'bitcoin': {'usd': 40066.81}}
```

#### Need more examples?
Check out [here](https://github.com/khooihzhz/coingecko-python/tree/master/examples)!


## License
The library is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
