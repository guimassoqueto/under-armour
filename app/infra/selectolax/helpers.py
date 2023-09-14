import re


def get_image_url(small_image_url: str) -> str:
  return small_image_url.replace("520-520", "1080-auto").replace("width=520", "width=1080").replace("height=520", "height=1080")


def get_price(inner_text: str) -> str:
  raw_price = re.search(r"[\d,.]+", inner_text).group()
  price = raw_price.replace(".", "").replace(",", ".")
  return float(price)