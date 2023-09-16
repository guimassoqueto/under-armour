from dotenv import load_dotenv
from os import getenv
load_dotenv()


POSTGRES_DB = getenv("POSTGRES_DB", "postgres")
POSTGRES_HOST = getenv("POSTGRES_HOST", "localhost")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "password")
POSTGRES_PORT = getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = getenv("POSTGRES_USER", "postgres")
TABLE_NAME = getenv("TABLE_NAME", "sports")

MAX_CONCURRENCY = int(getenv("MAX_CONCURRENCY", 8))

UNDER_ARMOUR_OFFERS_URL = "https://www.underarmour.com.br/calcados/outlet?initialMap=productclusterids&initialQuery=386&map=category-2,productclusternames"

AWIN_ID=getenv("AWIN_ID", "")
AWIN_AFFID=getenv("AWIN_AFFID", "")