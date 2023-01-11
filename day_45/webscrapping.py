from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
yc_web_page=(response.text)

soup=BeautifulSoup(yc_web_page,"html.parser")
artile_tag=soup.find(name="a") 
article_text=artile_tag.getText()

  