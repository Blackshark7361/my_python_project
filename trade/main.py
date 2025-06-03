import requests
import unittest

API_BASE_URL = "https://api.huobi.pro"

class HuobiClient:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()['data']
        else:
            return None

    def get_market_data(self, symbol):
        api_uri = f"{API_BASE_URL}/market/history/kline?symbol={symbol}&period=1day&size=200"
        response = requests.get(api_uri)
        return self._handle_response(response)


class HuobiClientTests(unittest.TestCase):
    def setUp(self):
        api_key = 'fr'
        secret_key = 'b'
        self.huobi_client = HuobiClient(api_key, secret_key)

    def test_get_market_data(self):
        market_data = self.huobi_client.get_market_data('trxusdt')
        self.assertIsNotNone(market_data)
        self.assertTrue(any('high' in price for price in market_data))


if __name__ == '__main__':
    unittest.main()

client = HuobiClient('frbghq7rnm-e48184b0-74b2728b-43013', 'b572a2ed-8ac75c6b-b5f625e0-b6ff6')
print(client.get_market_data('trxusdt'))
