import sys, json, requests
from os import path

def get_format_params(name, currency, currency_info):
    format_string = lambda num: str(round(num, 2))
    return [name, currency, format_string(currency_info['price']), format_string(currency_info['percent_change_1h']), format_string(currency_info['percent_change_24h'])]

def get_config(filename):
    try:
        with open(path.join(path.dirname(path.realpath(__file__)), filename), 'r') as fp:
            config = json.load(fp)
        return config['tracked_coins'], config['currency']
    except EnvironmentError:
        sys.stderr.write('Config file not found\n')
    except KeyError:
        sys.stderr.write('Config.json should have \"tracked_coins\" and \"currency\" attributes\n')
    return None, None

def main():
    tracked_coins, currency = get_config('config.json')
    if not tracked_coins or not currency:
        return
    r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert={}'.format(currency), timeout=10)

    if r.status_code == 200:
        coin_dict = dict([(coin_info['symbol'], get_format_params(coin_info['name'], currency, coin_info['quotes'][currency])) for coin_info in r.json()['data'].values()])
        for coin in tracked_coins:
            if coin["ticker"] not in coin_dict:
                print('{} not found in config file.'.format(coin_symbol))
                continue
            if "notes" in coin:
                print('{}: {}${} (1h change: {}%, 24h change: {}%, notes: {})'.format(*coin_dict[coin["ticker"]], coin["notes"]))
            else:
                print('{}: {}${} (1h change: {}%, 24h change: {}%)'.format(*coin_dict[coin["ticker"]]))
    else:
        print('Error code {}: Unable to get information.'.format(str(r.status_code)))

if __name__ == '__main__':
    main()
