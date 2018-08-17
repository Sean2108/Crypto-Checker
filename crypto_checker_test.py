import sys
from crypto_checker import get_format_params, get_config
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

class CryptoCheckerTest(unittest.TestCase):

    def setUp(self):
        self.response = {
            "data": {
                "1": {
                    "id": 1, 
                    "name": "Bitcoin", 
                    "symbol": "BTC", 
                    "website_slug": "bitcoin", 
                    "rank": 1, 
                    "circulating_supply": 17008162.0, 
                    "total_supply": 17008162.0, 
                    "max_supply": 21000000.0, 
                    "quotes": {
                        "USD": {
                            "price": 9024.09, 
                            "volume_24h": 8765400000.0, 
                            "market_cap": 153483184623.0, 
                            "percent_change_1h": -2.31, 
                            "percent_change_24h": -4.18, 
                            "percent_change_7d": -0.47
                        }
                    }, 
                    "last_updated": 1525137271
                }, 
                "1027": {
                    "id": 1027, 
                    "name": "Ethereum", 
                    "symbol": "ETH", 
                    "website_slug": "ethereum", 
                    "rank": 2, 
                    "circulating_supply": 99151888.0, 
                    "total_supply": 99151888.0, 
                    "max_supply": None, 
                    "quotes": {
                        "USD": {
                            "price": 642.399, 
                            "volume_24h": 2871290000.0, 
                            "market_cap": 63695073558.0, 
                            "percent_change_1h": -3.75, 
                            "percent_change_24h": -7.01, 
                            "percent_change_7d": -2.32
                        }
                    }, 
                    "last_updated": 1525137260
                } 
            },
            "metadata": {
                "timestamp": 1525137187, 
                "num_cryptocurrencies": 1602, 
                "error": None
            }
        }

    def test_get_format_params_should_return_correct_format(self):
        bitcoin_vals = self.response['data']['1']
        result = get_format_params(bitcoin_vals['name'], 'USD', bitcoin_vals['quotes']['USD'])
        self.assertEqual(result, ['Bitcoin', 'USD', '9024.09', '-2.31', '-4.18'])
        
    def test_get_config_finds_file(self):
        coins, currency = get_config('config.json')
        self.assertTrue(coins)
        self.assertTrue(currency)

    def test_get_config_wrong_file_returns_none(self):
        coins, currency = get_config('does_not_exist.json')
        self.assertFalse(coins)
        self.assertFalse(currency)

if __name__ == '__main__':
    unittest.main()
