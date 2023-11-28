from rich.console import Console
from rich.table import Table
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

webSite = "https://www.adamchoi.co.uk/overs/detailed"

""" 开始 """
driver = webdriver.Edge()
driver.get(webSite)
driver.maximize_window()
time.sleep(2)

""" 按下all_match按钮 """

all_Btn = driver.find_element("xpath",
                              "//label[@analytics-event='All matches']")
time.sleep(1)
all_Btn.click()

""" 下拉框选择选项 """
select = Select(driver.find_element(By.ID, "country"))

for i, item in enumerate(select.options):
    Console().print(f"--- Country{i}:", item.text)
    select.select_by_index(i)
    time.sleep(2)
    tr_list = driver.find_elements("xpath", "//tr")

    date = home_team = score = away_team = []

    for tr in tr_list:
        date.append(tr.find_element('xpath', "./td[1]").text)
        home_team.append(tr.find_element('xpath', "./td[2]").text)
        score.append(tr.find_element('xpath', "./td[3]").text)
        away_team.append(tr.find_element('xpath', "./td[4]").text)

    """ 保存为CSV """
    dic = {"date": date, "home_team": home_team,
           "score": score, "away_team": away_team}
    df = pd.DataFrame.from_dict(dic)
    df.to_csv(f"{item.text}.csv", index=False)

    time.sleep(1)

    """ 保存为HTML """
    c = Console(record=True)
    table = Table(title=f"{item.text}")
    table.add_column("date", max_width=50, style="cyan")
    table.add_column("home_team", max_width=70, style="magenta")
    table.add_column("score", max_width=30, style="cyan")
    table.add_column("away_team", max_width=50, style="magenta")
    for date, home_team, score, away_team in zip(date, home_team, score, away_team):
        table.add_row(date, home_team, score, away_team)

    c.print(table)
    c.save_html(f"{table.title}.html")

    time.sleep(1)

""" 结束 """
time.sleep(100)
# driver.quit()
