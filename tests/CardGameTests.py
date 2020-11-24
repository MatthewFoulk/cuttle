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

    def testInitialization(self):

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




if __name__ == "__main__":
    unittest.main()