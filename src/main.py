from utils import scrape_tendies_meme_site
from settings import ONSALE_YES, ONSALE_NO

def check_on_sale() -> str:
	if scrape_tendies_meme_site():
		return ONSALE_YES
	return ONSALE_NO

if __name__ == '__main__':
	print(check_on_sale())
