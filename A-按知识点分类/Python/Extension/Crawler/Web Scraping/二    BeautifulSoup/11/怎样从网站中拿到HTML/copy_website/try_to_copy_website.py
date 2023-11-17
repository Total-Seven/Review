from rich import print
import requests

url = "https://subslikescript.com/movie/Cascade-12180508"
res = requests.get(url)
content = res.text

with open('copy.html', 'w', encoding='utf-8') as html:
    html.write(content)

print("successful~")
