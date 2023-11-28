from rich.console import Console
from rich.table import Table
from rich import inspect
from bs4 import BeautifulSoup
import requests

c = Console(record=True)
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
    print(f"-----{i}-----   :   ", website)
    res = requests.get(website)
    text = res.text
    soup = BeautifulSoup(text, 'lxml')
    box = soup.find('article', class_='main-article')
    a_list = box.find_all('a', href=True)

    for a in a_list:
        link = f"{root}/{a['href']}"
        title = a.li.get_text()
        links[f'{title}'] = link

""" 保存为txt文件 """
with open('movies_list.txt', "w", encoding='utf-8') as f:
    for key, value in links.items():
        f.write(f"---{key}------{value}\n")

""" 制作表格 """
table = Table(title=f"Movies Link Table({2})")
table.add_column("Movie Name", max_width=50, style="cyan")
table.add_column("Link", justify="left", max_width=100, style="magenta")
for key, value in links.items():
    table.add_row(key, value)
c.print(table)
c.save_html(f"{table.title}.html")
"""
[]运算符可以访问元素的属性
.运算符可以访问子元素

"""
