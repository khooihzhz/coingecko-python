import coingecko

client = coingecko.CoinGeckoProClient(api_key='X_CG_PRO_API_KEY')

## Key Endpoints
response = client.key.get()

"""
Example Payload
{
    'plan': 'Analyst',
    'rate_limit_request_per_minute': 500,
    'monthly_call_credit': 1000,
    'current_total_monthly_calls': 5,
    'current_remaining_monthly_calls': 995
}
"""

