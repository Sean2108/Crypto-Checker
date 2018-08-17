import sys, json, requests
from os import path

def format_string(num):
    return str(round(num, 2))

def check_coin(coin_info):
    if coin_info['symbol'] in tracked_coins:
	currency_info = coin_info['quotes'][currency]
        print('{}: {}${} (1h change: {}%, 24h change: {}%)'
                .format(coin_info['name'], currency, format_string(currency_info['price']), format_string(currency_info['percent_change_1h']), currency_info['percent_change_24h']))

try:
    with open(path.join(path.dirname(path.realpath(__file__)), 'config.json'), 'r') as fp:
        config = json.load(fp)
except EnvironmentError:
    print('Config file not found')
    sys.exit()

try:
    tracked_coins = set(config['tracked_coins'])
    currency = config['currency']
except KeyError:
    print('Config.json should have \"tracked_coins\" and \"currency\" attributes')
    sys.exit()

r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert={}'.format(currency), timeout=10)

if r.status_code == 200:
    data = r.json()['data']
    for coin_index in data:
        check_coin(data[coin_index])
else:
    print('Error code {}: Unable to get information.'.format(r.status_code))
