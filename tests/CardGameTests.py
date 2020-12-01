"""
Module for testing various aspects of the Cuttle project
"""
import os, sys
import unittest

# I don't exactly understand this, but it allows me to import from the parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.CardGame import *

class TestCard(unittest.TestCase):

    def test__init__(self):

        # Simple test
        card = Card(1, 1)
        self.assertEqual(card.value, 1, "Card value should be 1")
        self.assertEqual(card.suit, 1, "Suit value should be 1")

        # Illegal card values
        with self.assertRaises(ValueError):
            card = Card(-1, 1)
        with self.assertRaises(ValueError):
            card = Card(3, -10)
        with self.assertRaises(ValueError):
            card = Card(15, 0)
        with self.assertRaises(ValueError):
            card = Card(10, 4)
        with self.assertRaises(ValueError):
            card = Card(14, 4)
        
        # Illegal argument types
        with self.assertRaises(TypeError):
            card = Card("Jack", 2)
        with self.assertRaises(TypeError):
            card = Card(1.2, 2)
        with self.assertRaises(TypeError):
            card = Card(2, 200.1)
        with self.assertRaises(TypeError):
            card = Card(1, "Hearts")
        

    
    def test__str__(self):

        # Ace and Clubs
        card = Card(1, 3)
        strCard = str(card)
        self.assertEqual(strCard, "Ace of Spades")

        # Jack and Diamonds
        card = Card(11, 1)
        strCard = str(card)
        self.assertEqual(strCard, "Jack of Diamonds")

        # Queen and Hearts
        card = Card(12, 2)
        strCard = str(card)
        self.assertEqual(strCard, "Queen of Hearts")

        # King and Clubs
        card = Card(13, 0)
        strCard = str(card)
        self.assertEqual(strCard, "King of Clubs")

        # Ten and Diamonds
        card = Card(10, 1)
        strCard = str(card)
        self.assertEqual(strCard, "10 of Diamonds")

    def test__eq__(self):

        # Different cards
        card1 = Card(1, 1)
        card2 = Card(2, 2)
        self.assertFalse(card1 == card2)

        # Same cards
        card1 = Card(12, 0)
        card2 = Card(12, 0)
        self.assertTrue(card1 == card2)

        # Same suit different values
        card1 = Card(11, 3)
        card2 = Card(5, 3)
        self.assertFalse(card1 == card2)

        # Same value different suit
        card1 = Card(4, 1)
        card2 = Card(4, 2)
        self.assertFalse(card1 == card2)

        # Exactly the same card object (aliasing)
        card1 = Card(3, 2)
        card2 = card1
        self.assertTrue(card1 == card2)
    
    # TODO
    def test__gt__(self):
        pass

    def testGetImageFileName(self):
        card = Card(1, 1)
        image = card.getImageFileName()
        self.assertTrue(image == "DiamondsAce.gif") 


class testDeck(unittest.TestCase):

    def test__init__(self):
        
        # Verify that every card is in the deck
        deck = Deck()
        for value in Card.VALUES.keys():
            for suit in Card.SUITS.keys():
                self.assertIn(Card(value, suit), deck.cards)
        
        # Verify the deck length is 52
        self.assertTrue(len(deck.cards) == 52)

        # Verify the deck length is 52 afer making another deck
        # messed this up by creating class variable instead of an
        # instance variable
        deck2 = Deck()
        self.assertTrue(len(deck.cards) == 52)
        self.assertTrue(len(deck2.cards) == 52) 
    
    def test__eq__(self):

        # Compare new decks unshuffled
        deck = Deck()
        deck2 = Deck()
        self.assertTrue(deck == deck2)

    
    def testShuffle(self):
        
        # Not sure how to test, so I'm checking to see if they are equal
        # because I assume it is very unlikely that they would be in 
        # the same order after being shuffled
        deck = Deck()
        deck2 = Deck()
        Deck.shuffle(deck2)
        self.assertFalse(deck == deck2)

    def testGetCardAt(self):

        # Unshuffled, deck should be in order
        deck = Deck()
        firstCard = deck.getCardAt(0)
        self.assertTrue(firstCard == Card(1, 0))
        lastCard = deck.getCardAt(len(deck.cards)-1)
        self.assertTrue(lastCard == Card(13, 3))

        # Illegal argument type
        with self.assertRaises(TypeError):
            card = deck.getCardAt("one")
        with self.assertRaises(TypeError):
            card = deck.getCardAt(0.1)
        
        # Illegal position values
        with self.assertRaises(ValueError):
            card = deck.getCardAt(-1)
        with self.assertRaises(ValueError):
            card = deck.getCardAt(deck.getNumCards())
    
    # TODO
    def testDrawCardAt(self):
        pass
    
    def testDeal(self):

        # Normal Deal, unshuffled deck
        deck = Deck()
        hands = deck.deal(3, 2)
        # Every hand is the same, specified length
        for hand in hands:
            self.assertTrue(len(hand) == 2)

        # Illegal argument types
        with self.assertRaises(TypeError):
            hands = deck.deal("one", 1)
        with self.assertRaises(TypeError):
            hands = deck.deal(1, 1.2)
        
        # Illegal argument values
        with self.assertRaises(ValueError):
            hands = deck.deal(0, 10)
        with self.assertRaises(ValueError):
            hands = deck.deal(-1, 3)
        with self.assertRaises(ValueError):
            hands = deck.deal(1, 0)
        with self.assertRaises(ValueError):
            hands = deck.deal(1, -1)
        with self.assertRaises(ValueError):
            hands = deck.deal(10, 10)

        # Test that every card is dealt
        deck = Deck()
        hands = deck.deal(4, 13)
        self.assertTrue(len(hands) == 4)
        self.assertTrue(len(hands[0]) == 13)
        self.assertTrue(hands[3][12] == Card(13,3))


if __name__ == "__main__":
    unittest.main()