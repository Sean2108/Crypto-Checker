import sys, json

tracked_coins = [coin.rstrip() for coin in open(sys.path[0] + '/tracked_crypto.txt')]

for coin_info in json.load(sys.stdin):
    if coin_info['symbol'] in tracked_coins:
        print(coin_info['name'] + ': ' + coin_info['price_usd'] + \
              " (1h change: " + coin_info['percent_change_1h'] + \
              "%, 24h change: " + coin_info['percent_change_24h'] + "%)")
