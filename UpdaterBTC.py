# v1.1

import time
import requests

BTCprice_old = 4290.00

while True: 
	try:
		url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
		response = requests.get(url)
		data = response.json()
		
		BTCprice = float(data[0]['price_usd'])
		
		if (BTCprice > BTCprice_old):
			colour = "#00FF00"
		else:
			colour = "#FF0000"
		
		BTCprice_old = BTCprice
		
		sink = open('Blink1BTC.txt', 'w')
		sink.write(colour)
		sink.close()

	except:
		err = open('Blink1BTCdebug.txt', 'w')
		err.write("err")
		err.close()
		
	time.sleep(300) #5min delay
