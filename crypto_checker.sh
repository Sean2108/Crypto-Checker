#!/bin/bash - 
#===============================================================================
#
#          FILE: eth_checker.sh
# 
#         USAGE: ./eth_checker.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 02/06/2018 18:03
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

curl -s https://api.coinmarketcap.com/v1/ticker/ | python $(dirname $0)/crypto_checker.py
