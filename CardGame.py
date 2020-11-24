"""
Module for implimenting a card game
"""

import random

class Card():
    """
    Class for implimenting a playing card from a standard deck.
    Each card has both a suit and value.
    """

    SUITS = {0: "Spades", 1: "Hearts", 2: "Diamonds", 3: "Clubs"}
    VALUES = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
            8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}

    def __init__(self, value, suit):
        """
        Initialize playing card.
        Each playing card has:
            - 'value': an integer value between 1 to 13: 1 for Ace,
                    2 through 10 for numerical cards, 11 for Jack,
                    12 for Queen, 13 for King
            - 'suit': an integer value between 0 to 3: 0 for Spade,
                    1 for Heart, 2 for Diamond, 3 for Club
        """
        if value < 1 or value > 13:
            raise ValueError(f"""Illegal card value attempted. Acceptable values
                are between 1 to 13. You tried: {value}""")

        if suit < 0 or suit > 3:
            raise ValueError(f"""Illegal suit attempted. Acceptable values
                are between 0 to 3. You tried: {suit}""")

        self.value = value
        self.suit = suit
    
    def __str__(self):
        """
        String representation of a card object
        """
        return f"{Card.VALUES[self.value]} of {Card.SUITS[self.suit]}"
    
    def __eq__(self, other):
        """
        Equals method
        """
        if not isinstance(other, self.__class__):
            return False

        return (self.value == other.value and self.suit == other.suit)
            


        


class Deck():
    """
    Class for implimenting a standard playing card deck.
    """

    def __init__(self):
        """
        Initialize a standard 52 card deck.
        """
        self.cards = list()
        for value in Card.VALUES.keys():
            for suit in Card.SUITS.keys():
                self.cards.append(Card(value, suit))
    
    def __eq__(self, other):
        """
        Equals method
        """

        # Not a deck object
        if not isinstance(other, self.__class__):
            return False
        
        # Different number of cards
        if len(self.cards) != len(other.cards):
            return False
        
        # Check if each card position is the same
        for index in range(len(self.cards)):
            if self.cards[index] != other.cards[index]:
                return False
        
        return True
    
    def shuffle(self):
        """
        Randomly shuffles the cards in the deck
        """
        random.shuffle(self.cards)

