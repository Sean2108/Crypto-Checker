import sys, json, requests
from os import path

def format_string(num):
    return str(round(num, 2))

def check_coin(coin_info):
    if coin_info['symbol'] in tracked_coins:
	currency_info = coin_info['quotes'][currency]
        print(coin_info['name'] + ': $' + format_string(currency_info['price']) + \
              " (1h change: " + format_string(currency_info['percent_change_1h']) + \
              "%, 24h change: " + format_string(currency_info['percent_change_24h']) + "%)")

with open(path.join(path.dirname(path.realpath(__file__)), 'config.json'), 'r') as fp:
    config = json.load(fp)

tracked_coins = set(config['tracked_coins'])
currency = config['currency']

r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert={}'.format(currency), timeout=10)

if r.status_code == 200:
    data = r.json()['data']
    for coin_index in data:
        check_coin(data[coin_index])
else:
    print('Unable to get information.')
