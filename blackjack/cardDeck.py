from card import card
import random

class cardDeck(card):
	deck = []

	def __init__(self):
		i = 0
		while i <= 3:
			j = 1
			while j <= 13:
				if i == 0 :
					self.deck.append(card(j,'♣'))
				if i == 1 :
					self.deck.append(card(j,'♦'))
				if i == 2 :
					self.deck.append(card(j,'♥'))
				if i == 3 :
					self.deck.append(card(j,'♠'))
				j += 1
			i += 1


	def deckDisplay(self):
		for i in self.deck:
			i.display()

	def deckShuffle(self):
		random.shuffle(self.deck)