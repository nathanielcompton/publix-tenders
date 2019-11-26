import re
import requests
from bs4 import BeautifulSoup, Comment

from settings import TENDERS_SALE_URL, ONSALE_STRING

class Tenders:

	def scrape_tendies_meme_site() -> bool:
		res = requests.get(TENDERS_SALE_URL)
		soup = BeautifulSoup(res.text, "html.parser")
		# comments = list of stringified code comments from the soup
		comments = str(soup.find_all(string=lambda text: isinstance(text, Comment)))
		if re.search(ONSALE_STRING, comments):
			return True
		return False
