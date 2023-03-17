from random import shuffle

class Card:
	suits=["Hearts","Diamonds","Clubs","Spades"]
	values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	total_cards=52

	def __init__(self):
		for suit in suits:
			for val in values:
				deck_of_cards=Card(suit,val)

	def __rep__(self):
		return f"Deck of {amount} cards"

	def _deal(self,num):
		if self.count() > 0:
			if self.count>=num:
				total_cards-=num
				deck_of_cards[num:]
				return deck_of_cards[:-num]
			else:
				deck_of_cards[:-self.count()]
				return deck_of_cards[:-num]
		else:
			return ValueError ("Only full deck can be shuffled")

	def count(self):
		return total_cards

	def shuffle(self):
		if self.count()==52:
			return shuffle(deck_of_cards)
		else:
			return ValueErro ("Only full deck can be shuffeled")

	def deal_card(self,1):
		return self._deal(1)

	def deal_hand(self,num):
		return self._deal(num)
