  # API is like food menu
  #API (appplication programming interface)
  #  API acts as a communication layer , that allows different systems to talk to each other without having to understand exactly what each other does.
import requests
# request le hami lai kunei link ma jana dinxa


response=requests.get(url="http://api.open-notify.org/iss-now.json")
##print(response.status_code)
# status_code le code matra dinxa
# 1-- huda hold on
# 2-- huda here you go
# 3-- go away
# 4-- you screwed up
# 5-- i screwed up
response.raise_for_status()
# raise_for_status Raises HTTPError, if one occurred.

data=response.json()
# JSON) is a standardized format commonly used to transfer data as text that can be sent over a network. 
# It's used by lots of APIs and Databases

longitude=data["iss_position"]["longitude"]

latitude=data["iss_position"]["latitude"]

iss_position=(longitude,latitude)
print(iss_position)
