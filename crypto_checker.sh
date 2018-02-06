#!/bin/bash - 

set -o nounset                              # Treat unset variables as an error

curl -s https://api.coinmarketcap.com/v1/ticker/ | python $(dirname $0)/crypto_checker.py
