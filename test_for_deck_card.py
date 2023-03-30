from card import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", "A")
		
	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")
		
	def test_repr(self):
		"""repr should return a string of the form 'Value of """ 
		self.assertEqual(repr(self.card), "A of Hearts")
        
class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_init(self):
        """deck should have 52 cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards),52))
        
    def test_repr(self):
        """repr should return a string of the form 'Deck of 52 cards.' """
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")
        
    def test_count(self):
        """count should return a count of the number of cards """
        self.assertEqual(self.deck.count(),52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(),51)
    
    def test_deal_sufficient_cards(self):
        """_deal shlud deal the number of cards specified, """
        self.assertEqual(len(cards),10)
        self.assertEqual(self.deck.count(),42)
        
    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)
        
    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty"""
        self.deck._deal(self.deck.count())
        with  self.assertRaises(ValueError):
            self.deck._deal(1)
            
    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card,dealt_card)
        self.assertEqual(self.deck.count(), 51)
    
    def test_deal_hand(self):
        """deal_hand should deal the number os cards passed into """
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards),20)
        self.assertEqual(self.deck.count(), 32) 
        
    def test_shuffle_full_deck(self):
        """deal_hand should deal the number os cards passed into """
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52) 
        
    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError of ht edeck isnot full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()
            
if __name__ == '__main__':
    unittest.main()