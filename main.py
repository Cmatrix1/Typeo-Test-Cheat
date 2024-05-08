from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://typeo.top/test/#")
    page.wait_for_timeout(2000)
    page.query_selector(".start_competition").click()
    page.query_selector("a.btn-info:nth-child(2)").click()

    page.wait_for_timeout(4000)
    type_text = page.query_selector("#text_holder").text_content()

    page.keyboard.type(type_text, delay=20)

    page.wait_for_timeout(10_000)
    page.screenshot(path='cheat.png')
    browser.close()
