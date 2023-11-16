import asyncio
from playwright.async_api import async_playwright
#
import os
import re
import aiohttp


def sanitize_filename(filename):
    """
    清理文件名以确保它们是有效的文件夹名称。
    """
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def create_dir(keyword):
    # 创建关键词对应的文件夹
    folder_name = sanitize_filename(keyword)
    os.makedirs(folder_name, exist_ok=True)
    return folder_name


async def create_page(playwright):
    browser = await playwright.chromium.launch(headless=False)  # ❓❓❓
    context = await browser.new_context()
    page = await context.new_page()
    return browser, page


async def page_initial(page, url, w=800, h=600):
    await page.set_viewport_size({"width": w, "height": h})
    await page.goto(url)


async def search(page, keyword):
    await page.fill('input', keyword)
    await page.click('._3Kq4A')   # ❗❗❗
    await asyncio.sleep(6)  # ❓❓❓


async def close_popup(page):
    # 关闭弹窗
    close_button = await page.query_selector('.passport-close')
    if close_button:
        await close_button.click()


def getAll_image(page):
    return page.evaluate(''' ()=>{
        const imgWaperElements = document.querySelectorAll('.imgWaper')
        const infoList = []
        imgWaperElements.forEach(e =>{
            const title = e.getAttribute('title')
            const src = e.querySelector('img').getAttribute('data-src')
            infoList.push({title,src})
        })
        return infoList
    }''')


def print_info(info_list):
    for info in info_list:
        print(f"標題:{info['title']},鏈接:{info['src']}")


async def save_to_dir(info_list, folder_name):
    async with aiohttp.ClientSession() as session:
        for index, info in enumerate(info_list):
            async with session.get(f"http:{info['src']}") as resp:
                if resp.status == 200:
                    image_data = await resp.read()
                    file_name = f"{folder_name}/{sanitize_filename(info['title'])}.jpg"
                    with open(file_name, "wb") as f:
                        f.write(image_data)


async def next_page(page):
    # ❗❗❗
    next_button = await page.query_selector('.paginationRightButton')
    if next_button:
        await next_button.click()
        await asyncio.sleep(3)
        return True
    else:
        return False


async def extract_image_info(keyword, max_pages):
    async with async_playwright() as p:
        # 创建文件夹
        folder_name = create_dir(keyword)
        # 创建网页
        browser, page = await create_page(p)
        # 訪問網頁
        await page_initial(page, "http://www.vcg.com/")
        # 輸入關鍵字並點擊搜索按鈕
        await search(page, keyword)

        for page_num in range(max_pages):
            # 关闭弹窗
            await close_popup(page)

            # 獲取所有 .imgWaper 元素的標題和圖片鏈接
            image_info_list = await getAll_image(page)

            # 下载图片并保存到文件夹
            await save_to_dir(image_info_list, folder_name)
            # 下一页
            exist_next = await next_page(page)
            if not exist_next:
                break

        await browser.close()

asyncio.run(extract_image_info("街舞", 2))
