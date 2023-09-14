from asyncio import Semaphore
from app.infra.playwright.playwright import Playwright
from app.infra.psycopg.postgres import insert_products
from app.infra.selectolax.parser import ItemsCount, Selectolax
from app.settings import UNDER_ARMOUR_OFFERS_URL
from app.logging.logger import getLogger
import math

logger = getLogger("app.py")


async def get_urls():
  try:
    content = await Playwright.get_content(UNDER_ARMOUR_OFFERS_URL)
    items_count = ItemsCount.get(content)
    page_total = math.ceil(items_count / 20) + 1 # 20 representa quantos item por vez sao mostrados por pagina
    urls = [f"{UNDER_ARMOUR_OFFERS_URL}&page={i}" for i in range(1, page_total)]
    return urls

  except Exception as e:
    raise(e)
  

async def scrap_data(url: str, concurrency_limit: Semaphore):
  async with concurrency_limit:
    try:
      content = await Playwright.get_content(url)
      selectolax = Selectolax(content)
      products = selectolax.get_products()
      await insert_products(products)

    except Exception as e:
      logger.error(e)
      raise e
