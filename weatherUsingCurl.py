import os
import json

reportFileName = "report.txt"

city = input("Enter the city to check temperature: ")

os.system('curl -o report.txt -s "http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=5c89bf395effa277f54aaad228fb81e3&units=metric"')

with open(reportFileName) as fileObject:
	data = fileObject.readline()
	dictionary = json.loads(data)
	tempDict = dictionary['main']
	temperature = tempDict['temp']
	print("Temperature of " + city + " is: " + str(temperature) + "°C" )