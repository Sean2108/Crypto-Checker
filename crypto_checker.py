import sys, json

tracked_coins = [coin.rstrip() for coin in open(sys.path[0] + '/tracked_crypto.txt')]

for coin_info in json.load(sys.stdin):
    if coin_info['symbol'] in tracked_coins:
        print(coin_info['symbol'] + ': ' + coin_info['price_usd'])
