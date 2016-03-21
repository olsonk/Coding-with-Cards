import random
import time

# create Players
class Player(object):
	def __init__(self, num, name):
		self.num = num
		self.name = name
		self.points = 0

# make the deck of cards
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card(object):
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		if self.suit == "Clubs" or self.suit == "Spades":
			self.color = "black"
		else:
			self.color = "red"
		if self.value == "Jack" or self.value == "Queen" or self.value == "King" or self.value == "Ace":
			self.isFace = True
		else:
			self.isFace = False
		self.name = str(self.value + " of " + self.suit)

deck = []
discardPile = []

for suit in suits:
	for value in values:
		deck.append(Card(value, suit))

# Start the game
print "----Find the Queen!----"
print "Welcome! Player 1, please enter your name:"
name = raw_input()
player1 = Player(1, name)
print "Player 2, please enter your name:"
name = raw_input()
player2 = Player(2, name)
		
random.shuffle(deck)
"""
def cardManager(pickedCard):
	discardPile = []
	discardPile.append(deck.pop(pickedCard))
	return discardPile
"""
"""
The game begins...
Pick a red card, and you get a point. If that red card is a face card, you get another point!
If that red face card happens to be the King of Hearts, though, you lose all points!
If it's the Queen of Diamonds, though, you get get an EXTRA 5 points!
If a red Ace is pulled, the other team gets a point too.
Keep picking card until you get a black card.
If that black card was the Ace of Spades, your opponent scores 5 points and starts their turn.
If it was the 2 of Clubs, all the cards get shuffled back into the deck and you continue playing!
"""
usedCards = []
def playGame(player, opponent):
	time.sleep(1)
	print "%s's turn! ------------------------------ Score: %s: %d   %s: %d" % (player.name, player.name, player.points, opponent.name, opponent.points)
	nextCard = raw_input("Type 'pick' to choose your next card! > ")
	while nextCard != "pick":
		nextCard = raw_input("Whoops! Try again: type 'pick' to choose your next card! > ")
	pickedCard = deck.pop()
	usedCards.append(pickedCard)
	print "You picked the %s." % pickedCard.name

	while pickedCard.color == "red":
		player.points += 1
		time.sleep(2)
		print "Red Card! %s got a point! You have %d points!" % (player.name, player.points)
		if pickedCard.isFace:
			player.points +=1
			time.sleep(2)
			print "Face card! You got a point! You have %d points!" % player.points
			if pickedCard.name == "King of Hearts":
				player.points = 0
				time.sleep(2)
				print "Bummer...the King of Hearts. Back to 0 points."
			if pickedCard.name == "Queen of Diamonds":
				player.points += 5
				time.sleep(2)
				print "Sweet! The Queen of Diamonds! Plus 5 points! You have %d points!" % player.points
			if pickedCard.value == "Ace":
				opponent.points += 1
				time.sleep(2)
				print "That Ace was good for you, AND the other team! They just got a point and have %d points!" % opponent.points
		nextCard = raw_input("Type 'pick' to choose your next card! > ")
		while nextCard != "pick":
			nextCard = raw_input("Whoops! Try again: type 'pick' to choose your next card! > ")
		try:
			pickedCard = deck.pop()
			usedCards.append(pickedCard)
		except:
			print "You've run out of cards!"
		print "You picked the %s." % pickedCard.name
	if pickedCard.name == "Ace of Spades":
		opponent.points += 5
		time.sleep(2)
		print "Bummer! The Ace of Spades! The other team just got 5 points...They have a total of %d points." % opponent.points

	if pickedCard.name == "2 of Clubs":
		time.sleep(2)
		random.shuffle(deck)
		print "The 2 of Clubs! Time to shuffle the deck again..."
	return usedCards

while len(usedCards) < 52:
	playGame(player1, player2)
	print len(usedCards)
	playGame(player2, player1)
	print len(usedCards)
	
print "You went through the whole deck! Game over! %s had %d points. %s had %d points." % (player1.name, player1.points, player2.name, player2.points)
if player1.points > player2.points:
	time.sleep(2)
	print "%s wins!" % player1.name
elif player2.points > player1.points:
	time.sleep(2)
	print "%s wins!" % player2.name
else:
	print "Tie game!"