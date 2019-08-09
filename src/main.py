from models import Tendies


if __name__ == '__main__':
	tendies = Tendies()
	if tendies.are_on_sale():
		print("YEAH!")
	else:
		print("NOOO!")
