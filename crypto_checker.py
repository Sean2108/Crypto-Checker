import sys, json, requests
from os import path

def get_format_params(name, currency, currency_info):
    format_string = lambda num: str(round(num, 2))
    return [name, currency, format_string(currency_info['price']), format_string(currency_info['percent_change_1h']), currency_info['percent_change_24h']]

def get_config(filename):
    try:
        with open(path.join(path.dirname(path.realpath(__file__)), filename), 'r') as fp:
            config = json.load(fp)
        tracked_coins = set(config['tracked_coins'])
        currency = config['currency']
        return tracked_coins, currency
    except EnvironmentError:
        sys.stderr.write('Config file not found\n')
        sys.exit()
    except KeyError:
        sys.stderr.write('Config.json should have \"tracked_coins\" and \"currency\" attributes\n')
        sys.exit()

def main():
    tracked_coins, currency = get_config('config.json')
    r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert={}'.format(currency), timeout=10)

    if r.status_code == 200:
        data = r.json()['data']
        coin_dict = dict([(coin_info['symbol'], get_format_params(coin_info['name'], currency, coin_info['quotes'][currency])) for coin_info in r.json()['data'].values()])
        for coin_symbol in tracked_coins:
            print('{}: {}${} (1h change: {}%, 24h change: {}%)'.format(*coin_dict[coin_symbol]))
    else:
        print('Error code {}: Unable to get information.'.format(r.status_code))

if __name__ == '__main__':
    main()
