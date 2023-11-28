from rich import inspect
from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
sub = 'movies'
website = f'{root}/{sub}'

res = requests.get(website)
text = res.text

soup = BeautifulSoup(text, 'lxml')
pagination = soup.find('ul', class_='pagination')
last_page = pagination.find_all('li')[-2].text

"""
https://xxx.com/yyy?page=1
···························
https://xxx.com/yyy?page=1791
"""

links = {}
for i in range(1, int(last_page)+1)[:2]:
    website = f'{root}/{sub}?page={i}'
    res = requests.get(website)
    text = res.text

    box = soup.find('article', class_='main-article')
    a_list = box.find_all('a', href=True)

    for a in a_list:
        link = f"{root}/{a['href']}"
        title = a.li.get_text()
        links[f'{title}'] = link

inspect(links)


"""
[]运算符可以访问元素的属性
.运算符可以访问子元素

"""
