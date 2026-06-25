import requests
city = input("Enter the city name: ")
API_KEY = "bbd41048b0fb5ea78eada4f1496fa5db"
response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={bbd41048b0fb5ea78eada4f1496fa5db}")
data = response.json()
print(data) 

