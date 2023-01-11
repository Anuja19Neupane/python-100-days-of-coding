from bs4 import BeautifulSoup
import lxml

with open("day_45/website.html", encoding="utf-8") as file:
    contents=file.read( )


soup=BeautifulSoup(contents,"lxml") 
print(soup.title)
print(soup.a)# it will give the first anchor tag it will find in our html 
print(soup.li)# it will give the first list it will find in our html  

# hamile yo process bata first matra pauxum 
# but we want all of them suppose all the anchor tag,all lists

all_list=soup.find_all(name="li")
print(all_list)

for list in all_list:
    print(list.getText())

heading=soup.find(name="h3",class_="heading")
print(heading.getText())
company_url=soup.select_one(selector="p a") # paragraph ma vako anchor tag
print(company_url)