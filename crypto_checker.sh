#!/bin/bash - 

set -o nounset                              # Treat unset variables as an error
wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    curl -s https://api.coinmarketcap.com/v1/ticker/ | python $(dirname $0)/crypto_checker.py
fi
