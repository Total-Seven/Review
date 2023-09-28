import requests
from bs4 import BeautifulSoup

url = 'https://code.stemstar.com'
# url = 'https://jm.onlystem.com' # ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
# url = 'http://122.144.216.175:83' # TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

title = soup.find('title')
h1 = soup.find('h1')
p = soup.find('p')
img = soup.find('img')


print(r.status_code)
print(r.encoding)
print(r.content)
print(r.json)
print(r.text)
print(img)
