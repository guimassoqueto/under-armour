import re
from app.settings import AWIN_AFFID, AWIN_ID
from urllib.parse import quote


def get_image_url(small_image_url: str) -> str:
  return small_image_url.replace("520-520", "1080-auto").replace("width=520", "width=1080").replace("height=520", "height=auto")


def get_price(inner_text: str) -> str:
  raw_price = re.search(r"[\d,.]+", inner_text).group()
  price = raw_price.replace(".", "").replace(",", ".")
  return float(price)


def get_afiliate_link(item_url: str) -> str:
  """
  Return the afiliate url of the provided item.
  """
  if not AWIN_ID: raise Exception("You must provide the AWIN_ID")
  if not AWIN_AFFID: raise Exception("You must provide the AWIN_FFID")
  item_url_encoded=quote(item_url)
  awin_link = f"https://www.awin1.com/cread.php?awinmid={AWIN_ID}&awinaffid={AWIN_AFFID}&ued={item_url_encoded}"
  return awin_link


def encode_url(url: str) -> str:
  return quote(url)