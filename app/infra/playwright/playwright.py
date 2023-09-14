from playwright.async_api import async_playwright
from app.helpers.random_header import header

class Playwright:
  @staticmethod
  async def get_content(url: str) -> str:
    """
    Get the web page full content, dynamic or not.
    """
    async with async_playwright() as pw:
      browser = await pw.chromium.launch(headless=False)
      page = await browser.new_page()
      await page.set_extra_http_headers(header())
      await page.set_viewport_size({ "width": 1920, "height": 1080 })
      await page.goto(url)
      await page.wait_for_selector('.underarmourbr-search-page-0-x-list-item:nth-child(20)', timeout=120000)
      html_content =  await page.content()
      return html_content
