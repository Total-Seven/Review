import asyncio
from playwright.async_api import async_playwright


async def extract_image_info():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_viewport_size({"width": 800, "height": 600})
        # 訪問網頁
        await page.goto("http://www.vcg.com/")
        # 輸入關鍵字並點擊搜索按鈕
        await page.fill('input', '美食')
        await page.click('._3Kq4A')   # ❗❗❗
        await asyncio.sleep(6)  # ❓❓❓
        # 獲取所有 .imgWaper 元素的標題和圖片鏈接
        image_info_list = await page.evaluate(''' ()=>{
            const imgWaperElements = document.querySelectorAll('.imgWaper')
            const infoList = []
            imgWaperElements.forEach(e =>{
                const title = e.getAttribute('title')
                const src = e.querySelector('img').getAttribute('data-src')
                infoList.push({title,src})
            })
            return infoList
        }''')
        # 輸出標題和圖片鏈接
        for info in image_info_list:
            print(f"標題:{info['title']},鏈接:{info['src']}")

        await browser.close()

asyncio.run(extract_image_info())
