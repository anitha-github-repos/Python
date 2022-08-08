import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

html_page = response.text

soup = BeautifulSoup(html_page, "html.parser")
all_h3_tags = soup.find_all(name="h3", class_="title")
top_100_movies = []
for h3 in all_h3_tags:
    movie = h3.getText()
    top_100_movies.append(movie)

print(all_h3_tags)
print(top_100_movies)
top_100_movies.reverse()

print(top_100_movies)
with open("movies.txt", "w", encoding="utf8") as file:
    for movie in top_100_movies:
        file.write(movie)
        file.write("\n")



