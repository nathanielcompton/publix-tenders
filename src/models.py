import requests
import re
from bs4 import BeautifulSoup, Comment

from settings import TENDIES_URL, ONSALE_STRING


class Tendies():

	def are_on_sale(self) -> bool:
		res = requests.get(TENDIES_URL)
		soup = BeautifulSoup(res.text, "html.parser")
		# comments = list of stringified code comments from the soup
		comments = str(soup.find_all(string=lambda text: isinstance(text, Comment)))
		if re.search(ONSALE_STRING, comments):
			return True
		return False
