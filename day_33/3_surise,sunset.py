import requests
from datetime import datetime


my_lat=26.664639
my_long=87.271782

# value is pasted from internet

parameter={
    "lat":my_lat,
    "lng":my_long,
    "formatted":0,
    # formatted 0 huda 24 hour format ma print hudaina   , 1 huda 2022-12-18 15:00:02.603810 yesto print hunxa

    # lat is lattitude 
    #lng is longitude
}
response=requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()
data=response.json()
##print(data)
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]

print(sunrise)

time_now=datetime.now()
print(time_now)