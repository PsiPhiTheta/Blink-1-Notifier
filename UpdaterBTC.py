# v1.0

import time
import re

BTCprice_old = 4290

while True:
		https://api.coinmarketcap.com/v1/ticker/bitcoin/
	BTCprice = re.findall(r'price_usd": "(.*?)", st)
	
	if BTCprice > BTCprice_old
		colour = "00FF00"
	else
		colour = "FF0000"
	
	BTCprice_old = BTCprice
	
	sink = open('Blink1BTC.txt', 'w')
	f.write(colour)
	f.close()

	time.sleep(60) #60s delay
