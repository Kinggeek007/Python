
import mysql.connector
import requests

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
   print(f"Temperature: {temperature}") 
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {weather_report[0]['description']}")
   print(f"Wind Speed: {wind_report['speed']}")
   print(f"Time Zone: {data['timezone']}")
else:
   print("Error in the HTTP request")

cnx = mysql.connector.connect(
  host="db",
  user="app", 
  password="password",
  database="app"
)
mycursor = cnx.cursor()
add_weather = ("INSERT INTO weather "
                "( description, temperature, wind_speed, date)" 
                "VALUES ( %(description)s, %(temperature)s, %(wind_speed)s, CURRENT_DATE() ); "
                )

data_weather = {
  'description' : ({weather_report[0]['description']}),
  'temperature' : ({temperature}) ,
  'wind_speed' : ({weather_report['wind']['speed']})
}
mycursor.execute(add_weather, data_weather)
cnx.commit()

mycursor.close()
cnx.close()