from bs4 import BeautifulSoup
from rich import print
import requests

url = "https://subslikescript.com/movie/Titanic-120338#google_vignette"
res = requests.get(url)
content = res.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()  # ❗❗❗ get_text()
print(title)

transcript = box.find(
    'div', class_='full-script').get_text(strip=True, separator=" ")

print(transcript)
