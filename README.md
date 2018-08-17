# Crypto-Checker
Python script to check price for selected portfolio from CoinMarketCap. Requires requests.

To use, edit config.json so that it contains the symbols of the coins in your portfolio in 'tracked_coins' (eg. BTC, ETH), and your desired currency in 'currency'.

Valid fiat currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"
 
Valid cryptocurrency values include: "BTC", "ETH" "XRP", "LTC", "BCH"

Then, place the 3 files in the same directory and add the following line to your .bashrc:

```shell
python path/to/crypto_checker.py
```

On terminal startup, the prices of each cryptocurrency in your portfolio will be listed in your desired currency.
