import requests
from bs4 import BeautifulSoup


URL="https://www.timeout.com/film/best-movies-of-all-time"

response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")

all_movies=soup.find_all(name="h3",class_="_h3_cuogz_1")
movies_titles=[movie.getText() for movie in all_movies]
movies=movies_titles[::-1]#To reverse the order of a list of movie titles
print(movies_titles)

     

with open("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

print(response.status_code)







# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# # Make a request to the website
# response = requests.get(URL)

# # Check the status code to make sure the request was successful
# if response.status_code == 200:
#   # Parse the HTML content
#   soup = BeautifulSoup(response.text, "html.parser")

#   # Find all the movies in the HTML
#   all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

#   # Extract the movie titles from the found elements
#   movies_titles = [movie.get_text() for movie in all_movies]

#   # Print the movie titles
#   print(movies_titles)
# else:
#   print(f"Request to {URL} failed with status code {response.status_code}")