import requests
try:
 city = input("Enter the city name: ")
 lat = float(input("enter city latitude coordinates:"))
 lon = float(input("enter city longitude coordinates:"))
 API_KEY = "bbd41048b0fb5ea78eada4f1496fa5db"
 response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}",
                         timeout=5
                         )
 data = response.json()
 print("weather conditions:",data['weather'][0])
 print("temperature:",data['main']['temp'])
 print("Pressure:",data['main']['pressure'])
 print("humidity:",data['main']['humidity']) 
 print("minimum temperature:",data['main']['temp_min'])
 print("maximum temperature:",data['main']['temp_max'])
 print("Sea level:",data['main']['sea_level'])

except invalidCityError:
 print("invalid city Name Entered")
except KeyError:
 print("key not found")
except internetError:
 print("Request TimeOut")
except Exception as e:
 print(e)
 

 