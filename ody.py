import requests
import bs4

page = requests.get("https://www.oneplace.com/ministries/adventures-in-odyssey/")
od = bs4.BeautifulSoup(page.content, 'html.parser')

player = od.find(class_="player")
track = player.find(class_="overlay2")

print(track.getText())

