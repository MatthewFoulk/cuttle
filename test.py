"""
Module for testing various aspects of the Cuttle project
"""

import unittest
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
        card = Card(1, 3)
        assert




if __name__ == "__main__":
    unittest.main()