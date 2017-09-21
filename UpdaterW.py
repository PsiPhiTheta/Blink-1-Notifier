# v1.1

import time
import requests
import re

while True: 
	try:
		url = 'http://api.openweathermap.org/data/2.5/weather?q=Manchester,uk&appid=cb2a89a6a3e47be6888477a8053edeef'
		response = requests.get(url)
		data = response.json()
	
		weather = str(data['weather']) 
	
		debug = open('Blink1Wdebug.txt', 'w')
		debug.write(weather)
		debug.close()
	
		weather = weather.replace("'","") 
		weather = weather.replace(",","") 
		weather = weather.replace(":","") 
		weather = weather.replace("[","") 
		weather = weather.replace("{","") 
		weather = weather.replace("]","") 
		weather = weather.replace("}","") 
		weather = weather.replace(" ","") 
		
		weather_desk = re.search("main(.+?)description", weather)
		
		if weather_desk:
			weather_desk = weather_desk.group(1)
		
		if weather_desk == "Clear":
			colour = "#FFFF00" #sunny
		elif weather_desk == "Drizzle":
			colour = "#0000FF" #raining
		elif weather_desk == "Rain":
			colour = "#0000FF" #raining
		elif weather_desk == "Clouds":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Mist":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Smoke":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Atmosphere":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Fog":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Haze":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Thunderstorm":
			colour = "#A4A4A4" #cloudy
		elif weather_desk == "Snow": 
			colour = "#FFFFFF" #snowing 
		else:
			colour = "#000000" #other 
		
		sink = open('Blink1W.txt', 'w')
		sink.write(colour)
		sink.close()
	
	except:
		err = open('Blink1Wdebug.txt', 'w')
		err.write("err")
		err.close()
	
	time.sleep(60) 
