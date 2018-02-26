import pyowm
import os

api_key = os.environ['OPENWEATHER_API_KEY']
owm_city = os.environ ['CITY_NAME']

owm = pyowm.OWM(api_key)

obs = owm.weather_at_place(owm_city)
w = obs.get_weather()
l = obs.get_location()
desc = w.get_detailed_status()
temp = w.get_temperature('fahrenheit')
humi = w.get_humidity() 

print "source=openweathermap, city=\""+l.get_name()+"\", description=\""+desc+"\", temp="+str(temp['temp'])+", humidity="+str(humi)

