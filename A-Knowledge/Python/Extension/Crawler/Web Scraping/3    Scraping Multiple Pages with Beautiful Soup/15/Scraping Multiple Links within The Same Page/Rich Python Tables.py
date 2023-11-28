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
box = soup.find('article', class_='main-article')
a_list = box.find_all('a', href=True)
links = {}
for a in a_list:
    link = f"{root}/{a['href']}"
    title = a.li.get_text()
    links[f'{title}'] = link

table = Table(title="Movies Link Table")
table.add_column("Movie Name", style="cyan")
table.add_column("Link", justify="left", min_width=88, style="magenta")
for key, value in links.items():
    table.add_row(key, value)
c.print(table)
with open('movies_list.txt', "w", encoding='utf-8') as f:
    for key, value in links.items():
        f.write(f"---{key}------{value}\n")
c.save_html(f"{table.title}.html")
