from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
html_file = response.text

# with open(html_file, encoding="utf8") as f:
#     content = f.read()

soup = BeautifulSoup(html_file, "html.parser")
article_tag = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links =[]
for tag in article_tag:
    text = tag.getText()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
upvote_points = [int(points.split()[0]) for points in article_upvotes]


print(article_texts)
print(article_links)
print(article_upvotes)
print(upvote_points)

print(max(upvote_points))
max_upvote_index = upvote_points.index(max(upvote_points))

print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])

# all_a = soup.find_all("a")
# for tag in all_a:
#     print(tag.string)
#     print(tag.get("href"))



















# with open("website.html", encoding="utf8") as f:
#     contents = f.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.string)
#     print(tag.get("href"))