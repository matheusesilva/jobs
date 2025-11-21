from playwright.sync_api import sync_playwright

def handler(event, context):
    url = event.get("url", "https://example.com")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()

        page.goto(url, wait_until="networkidle", timeout=30000)
        title = page.title()
        content = page.content()

        browser.close()

    return {
        "statusCode": 200,
        "body": {
            "url": url,
            "title": title,
            "content_length": len(content)
        }
    }

