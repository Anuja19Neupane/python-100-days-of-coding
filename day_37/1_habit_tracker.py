# yo link bata excess hunxa
# https://pixe.la/v1/users/giby/graphs/graph1.html

import requests
from datetime import datetime

USERNAME="giby"
TOKEN="gdsyhek5277"
GRAPH_ID="graph1"

pixel_endpoint="https://pixe.la/v1/users"


user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",


}

##response=requests.post(url=pixel_endpoint,json=user_params)
##print(response.text)
# The post() method is used when you want to send some data to the server.

graph_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"cycling graph",
    "unit":"km",
    "type":"float",
    "color":"momiji",

}

headers={
    "X-USER-TOKEN":TOKEN
}  

response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response.text) 




pixel_creation_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many kilometers did you cycle today?"), # hamile diney data

}


#response=requests.post(url=pixel_creation_endpoint,json=pixel_data  ,headers=headers)
#print(response.text)


update_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"4.5"
}

#response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
#print(response.text)


delete_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)
