class card:
	def __init__ (self, symbol, suit):
		self.symbol = symbol
		self.suit = suit

	def display(self):
		if self.symbol == 1:
			print("A",self.suit, end = " / ")
		if (self.symbol > 1) and (self.symbol <= 10):
			print(self.symbol, self.suit, end = " / ")
		if self.symbol == 11:
			print ('J', self.suit, end = " / ")
		if self.symbol == 12:
			print('Q', self.suit, end = " / ")
		if self.symbol == 13:
			print('K', self.suit, end = " / ")


