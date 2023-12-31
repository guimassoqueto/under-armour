from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
  """
  Item represents how the item is structured in database. It is a business rule.

  There is 3 another columns id, created_at, and updated_at, but it is omited here, 
  because the database handles them.
  """

  url: str
  afiliate_url: Optional[str]
  title: str
  category: str
  image_url: str
  reviews: int
  free_shipping: bool
  price: float
  previous_price: float
  discount: int

  @classmethod
  def get_field_names(cls,alias=False):
    return list(cls.model_json_schema(alias).get("properties").keys())
    