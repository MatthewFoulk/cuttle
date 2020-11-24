"""
Module for testing various aspects of the Cuttle project
"""
import os, sys
import unittest

# I don't exactly understand this, but it allows me to import from the parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from CardGame import *

class TestCard(unittest.TestCase):

    def test__init__(self):

        # Simple test
        card = Card(1, 1)
        self.assertEqual(card.value, 1, "Card value should be 1")
        self.assertEqual(card.suit, 1, "Suit value should be 1")

        # Illegal cards
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

    
    def test__str__(self):

        # Ace and Clubs
        card = Card(1, 3)
        strCard = str(card)
        self.assertEqual(strCard, "Ace of Clubs")

        # Jack and Hearts
        card = Card(11, 1)
        strCard = str(card)
        self.assertEqual(strCard, "Jack of Hearts")

        # Queen and Diamonds
        card = Card(12, 2)
        strCard = str(card)
        self.assertEqual(strCard, "Queen of Diamonds")

        # King and Spades
        card = Card(13, 0)
        strCard = str(card)
        self.assertEqual(strCard, "King of Spades")

        # Ten and Hearts
        card = Card(10, 1)
        strCard = str(card)
        self.assertEqual(strCard, "10 of Hearts")

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


class testDeck(unittest.TestCase):

    def test__init__(self):
        
        # Verify that every card is in the deck
        deck = Deck()
        for value in Card.VALUES.keys():
            for suit in Card.SUITS.keys():
                self.assertIn(Card(value, suit), deck.cards)


if __name__ == "__main__":
    unittest.main()