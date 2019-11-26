import os

TENDERS_SALE_URL = os.getenv(
    "TENDERS_SALE_URL", "http://arepublixchickentendersubsonsale.com/"
)
ONSALE_STRING = os.getenv(
    "ONSALE_STRING", "onsale:yes"
)

ONSALE_YES = "Oh yeah they are!"
ONSALE_NO = "Sorry, not today!"
