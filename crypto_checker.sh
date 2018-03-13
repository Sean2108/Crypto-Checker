#!/bin/bash - 

set -o nounset                              # Treat unset variables as an error

timeout 5 bash -c "curl -s https://api.coinmarketcap.com/v1/ticker/ | python $(dirname $0)/crypto_checker.py"
