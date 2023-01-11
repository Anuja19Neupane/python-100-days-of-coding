import requests

OWM_Endpoints="https://api.openweathermap.org/data/2.5/weather"
api_key="7e036e7c939749a6cad393eeeaa801ce"


weather_params={
    "lat":26.664639,
    "lon":87.271782,
    "appid":api_key,
    }

response=requests.get(OWM_Endpoints,params=weather_params)
print(response.text)
print(response.url)