from card import card
from cardDeck import cardDeck
from stackOfDecks import stackOfDecks
import os
import time
clear = lambda: os.system('cls')



def draw(count,deck):
	i = 0
	results = []
	while i < count:
		temp = deck.stack.pop(0)
		results.append(temp)
		i += 1
	return results




def evalCards(player):
	score = 0
	for i in player:
		if (i.symbol == 11) or (i.symbol == 12) or (i.symbol == 13):
			score += 10
		if (i.symbol > 1) and (i.symbol <= 10):
			score += i.symbol
	for i in player:
		if (i.symbol == 1) and (score <= 10):
			score += 10
		if (i.symbol == 1) and (score > 10):
			score += 1
	return score



def displayCards(player):
	for i in player:
		i.display()




def getCardsBack(x1,x2,deck):
	deck.stack.extend(x1)
	deck.stack.extend(x2)
	x1.clear()
	x2.clear()



#SETTING UP DECKS AND COUNTER
clear()
print("WELCOME TO BLACKJACK!")
print('6 DECKS')
print("PAYS 2:1")
print("DEALER DRAWS UNDER 17")
print("HIT/STAY commands are written in lower case!")
time.sleep(5)
clear()
c = stackOfDecks()
c.stackShuffle()

player = []
dealer = []
playerCash = 1000
while 1:
	print('CASH: ', playerCash)
	print('BET:', end = " ")
	bet = input()
	bet = int(bet)
	if playerCash == 0:
		print("PLAYER IS BROKE!")
		print("GAME OVER")
		time.sleep(5)
		exit(0)
		
	player.extend(draw(2,c))
	dealer.extend(draw(2,c))
	print('PLAYER: ', end = " ")
	displayCards(player)
	print("  SCORE:",evalCards(player))
	print()
	print("DEALER: ", end = ' ')
	print("X", end = ' / ')
	dealer[1].display()
	print()
	#displayCards(dealer)
	if evalCards(player) == 21:
		print('PLAYER HAS BLACKJACK!')
		time.sleep(5)
		playerCash = playerCash + bet
		clear()
		getCardsBack(player, dealer, c)
		continue
	print("HIT/STAY?")
	cmmd = input()
	while 1:
		if cmmd == 'hit':
			player.extend(draw(1,c))
			print('PLAYER:', end = ' ')
			displayCards(player)
			print("  SCORE:",evalCards(player))
			if evalCards(player) > 21:
				print("PLAYER BUST!")
				print("DEALER WON!")
				time.sleep(5)
				clear()
				playerCash = playerCash - bet
				getCardsBack(player, dealer, c)
				break
				#playerCash = playerCash - bet
			print("hit/stay?")
			cmmd = input()
		if cmmd == 'stay':
			print ("DEALER:",end = ' ')
			displayCards(dealer)
			print("  SCORE:", evalCards(dealer))
			print()
			while evalCards(dealer) < 17:
				dealer.extend(draw(1,c))
				print('DEALER: ', end = ' ')
				displayCards(dealer)
				print("  SCORE:",evalCards(dealer))
				print()
			if evalCards(dealer) > 21:
				print("DEALER BUST!")
				print("PLAYER WON!")
				time.sleep(5)
				clear()
				playerCash = playerCash + bet
				getCardsBack(player, dealer, c)
				break
			if (evalCards(dealer) > evalCards(player)) and evalCards(dealer) < 22:
				print("DEALER WON!")
				playerCash = playerCash - bet
				getCardsBack(player, dealer, c)
				time.sleep(5)
				clear()
				break
			if (evalCards(dealer) < evalCards(player)) and evalCards(player) < 22:
				print('PLAYER WON!')
				playerCash = playerCash + bet
				getCardsBack(player, dealer, c)
				time.sleep(5)
				clear()
				break
			if (evalCards(player) == evalCards(dealer)) and evalCards(player) < 22:
				print('TIE!')
				getCardsBack(player, dealer, c)
				time.sleep(5)
				clear()
				break