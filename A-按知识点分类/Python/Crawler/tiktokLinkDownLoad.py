import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# 文件名不能包含字符
path = './dance'
# 创建文件夹 path = './xxxxx'
# os.mkdir(path)
# #文件名不能包含字符

def  create_dir(path):
    os.mkdir(path)
    print(path, '文件夹创建完毕')

def  uncreate_dir():
    print("视频将下载至：", path)
    print("...")
    print("开始下载！")
# 保存本地 并且关闭浏览器
def  save_locla(path,title,sourec_res,driver):
    with open(path + '/' + f'{title}' + '.mp4', 'wb')as f:
        f.write(sourec_res.content)
        print("下载完成！")
    driver.quit()

url = "https://v.douyin.com/MrdPEss/"

def _downloadmovie(driverPath, url, ):
    uncreate_dir() if os.path.exists(path) else create_dir(path)
    # 创建浏览器对象
    # driver = webdriver.Edge(executable_path=driverPath)
    driver = webdriver.Edge()
    # 打开网页
    driver.get(url)
    driver.maximize_window()
    # 获取源码
    html = driver.page_source
    # 创建soup对象
    soup = BeautifulSoup(html, 'html.parser')
    # 定位视频链接 title.string -> video
    title = soup.title.string
    video = soup.video
    # 构造链接
    source = 'https:' + video.source['src']
    # 通过requests访问链接 下载
    sourec_res = requests.get(source)
    # 保存本地
    save_locla(path, title, sourec_res, driver)

# _downloadmovie('E:\charomedirver\msedgedriver.exe',"https://v.douyin.com/MMEaJsM/") # https://v.douyin.com/ie7W5VgB# /

_downloadmovie("E:\Python3.11\msedgedriver.exe","https://v.douyin.com/ie7W5VgB/") # https://v.douyin.com/ie7W5VgB/
# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
