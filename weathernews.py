import requests
import bs4

page = requests.get("https://www.weather.gov/news/")
news = bs4.BeautifulSoup(page.content, 'html.parser')
news_items = news.find_all(class_="newsst01")

output = "\nNews:\n----------"

for i in news_items:
    link = i.select('a')[0]['href']
    output = output + "\n- " + i.getText() + link

print(output)

