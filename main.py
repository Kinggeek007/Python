import requests
import mysql.connector


api_key = "b8837b5152dcef4e61819348f3b3a615"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input( "Enter city name : ")
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
response = requests.get(complete_url)
if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   weather_report = data['weather']
   wind_report = data['wind']
   
   print(f"{city_name:-^35}")
   print(f"City ID: {data['id']}")   
   sql = "INSERT INTO weather (id)" 
   Val =data['id']
   print(f"Temperature: {temperature}") 
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {weather_report[0]['description']}")
   print(f"Wind Speed: {wind_report['speed']}")
   print(f"Time Zone: {data['timezone']}")
else:
   # showing the error message
   print("Error in the HTTP request")

mydb = mysql.connector.connect(
  host="db",
  user="app",
  password="password",
  database="app"
)
mycursor = mydb.cursor()
sql = "INSERT INTO weather (id, description, temperture, wind_speed, date) VALUES (%s, %s, %s, %s, %s)"
val = [ "(data['id'] , weather_report, temperature, wind_report, data['timezone'])" ]