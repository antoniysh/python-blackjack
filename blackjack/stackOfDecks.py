from card import card
from cardDeck import cardDeck
import random

class stackOfDecks:
	stack = []
	d = cardDeck()
	def __init__(self):
		i = 0
		while i <= 5:
			for j in self.d.deck:
				self.stack.append(j)

			i += 1


	def stackDisplay(self):
		for i in self.stack:
			i.display()

	def stackShuffle(self):
		random.shuffle(self.stack)


