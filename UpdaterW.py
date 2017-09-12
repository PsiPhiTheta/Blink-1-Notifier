# v1.0

import time

while True:
	weather = "cloudy" # add string to import weather from webAPI
	
	if weather = "cloudy"
		colour = "FFFF00" #sunny
	elif weather = "raining"
		colour = "0000FF" #raining
	elif weather = "cloudy"
		colour = "A4A4A4" #cloudy
	elif weather = "snowing"
		colour = "FFFFFF" #snowing
	else 
		colour = "000000" #error
	
	sink = open('Blink1W.txt', 'w')
	f.write(colour)
	f.close()

	time.sleep(60) #60s delay
