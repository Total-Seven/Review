from rich import print
from selenium import webdriver

""" 开始 """
driver = webdriver.Edge()

webSite = "https://www.adamchoi.co.uk/overs/detailed"


""" 结束 """
driver.quit()
