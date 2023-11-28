import re
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.douyin.com/search/搜索')
        await asyncio.sleep(3)
        # 在输入框中输入“python”
        await page.fill('input', 'python')
        # 点击搜索按钮
        await page.click('.rB8dMXOc')  # 搜索按钮
        await asyncio.sleep(3)

        titles = await page.query_selector_all('.vNyPlf_m')
        for i in range(len(titles)):
            title = await titles[i].evaluate('(element) => element.textContent')
            print("标题："+title.replace("...展开", ""))
        await browser.close()

main()
