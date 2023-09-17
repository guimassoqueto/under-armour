from selectolax.parser import HTMLParser
from app.logging.logger import getLogger
from app.infra.selectolax.helpers import get_image_url, get_price, encode_url
from app.domain.model import Item
from urllib.parse import urljoin
import re


logger = getLogger("parser.py")


class Selectolax:
  base_url = "https://www.underarmour.com.br/"
  def __init__(self, html_content: str) -> None:
    self.html_content = html_content
    self.parser = HTMLParser(self.html_content)

  def get_products(self) -> list[dict]:
    logger.info("Parsing products...")
    items = self.parser.css('div.underarmourbr-search-page-0-x-list-item')
    products = []
    for item in items:
      try:
        title = item.css_first('h2').text().strip()
        if not re.search('tênis', title, re.IGNORECASE): continue

        price = get_price(item.css_first(".underarmourbr-search-page-0-x-sellingPriceValue").text())
        previous_price = get_price(item.css_first(".underarmourbr-search-page-0-x-listPriceValue").text())
        discount = round((1 - (price / previous_price)) * 100)
        if discount < 40: continue

        url = urljoin(self.base_url, item.css_first('a.productLink').attrs["href"])
        #afiliate_url = get_afiliate_link(url)
        category = f"Under Armour Outlet {title}"
        image_url = get_image_url(item.css_first("img.underarmourbr-search-page-0-x-image").attrs["src"])

        item = Item(
          url=url,
          afiliate_url=encode_url(url),
          title=title,
          category=category,
          image_url=image_url,
          price=price,
          previous_price=previous_price,
          discount=discount,
          reviews=0,
          free_shipping=False
        )
        products.append(item.model_dump())
      except Exception as e:
        continue
    logger.info("Products parsed")
    return products
  

class ItemsCount:
  @staticmethod
  def get(content: str) -> int:
    parser = HTMLParser(content)
    inner_html = parser.css_first("span.vtex-search-result-3-x-showingProductsCount").text()
    inner_html_match = re.search(r"\d+$", inner_html)
    items_count = inner_html_match.group()
    return int(items_count)
