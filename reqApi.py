import requests	
city = input("Enter the city to check Temperature: ")
getReq = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5c89bf395effa277f54aaad228fb81e3&units=metric')
getReq_dict = getReq.json()
print("Temperature is: " + str(getReq_dict['main']['temp']) + "°C")
print("Humidity is: " + str(getReq_dict['main']['humidity']) + "%")