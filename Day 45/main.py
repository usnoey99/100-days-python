from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all("tr", class_="athing")

article_data = []

for article in articles:
    title_tag = article.find("span", class_="titleline").find("a")
    title = title_tag.getText()
    link = title_tag.get("href")

    score_tag = article.find_next_sibling().find("span", class_="score")

    score = int(score_tag.getText().split()[0]) if score_tag else "0 points"

    article_data.append({
        "title": title,
        "link": link,
        "score": score
    })

print(article_data)

highest_score = max(item["score"] for item in article_data)
print(highest_score)
popular_article = max(article_data, key=lambda x:x["score"])
print(popular_article)