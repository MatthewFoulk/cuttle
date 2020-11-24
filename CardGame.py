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
        if not isinstance(value, int):
            raise TypeError(f"""Illegal value type: value must be of type int. You
                tried type {type(value)}""")
        elif not isinstance(suit, int):
            raise TypeError(f"""Illegal suit type: suit must be of type int. You tried
                type {type(suit)}""")
        elif value < 1 or value > 13:
            raise ValueError(f"""Illegal card value attempted. Acceptable values
                are between 1 to 13. You tried: {value}""")
        elif suit < 0 or suit > 3:
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
        Equals Method:
        Cards are equal if their value and suit are the same
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
        for suit in Card.SUITS.keys():
            for value in Card.VALUES.keys():
                self.cards.append(Card(value, suit))
    
    def __eq__(self, other):
        """
        Equals Method: 
        Decks are equal if every card is in the same position
        and the decks are the same length.
        """

        # Not a deck object
        if not isinstance(other, self.__class__):
            return False
        
        # Different number of cards
        if self.getNumCards() != len(other.cards):
            return False
        
        # Check if each card position is the same
        for index in range(self.getNumCards()):
            if self.cards[index] != other.cards[index]:
                return False
        
        return True
    
    def shuffle(self):
        """
        Randomly shuffles the cards in the deck
        """
        random.shuffle(self.cards)
    
    def getCardAt(self, position):
        """
        Returns the card at the given position in the deck
        (0 indexed, i.e. position=0 returns the first card)
        """
        if not isinstance(position, int):
            raise TypeError(f"""Illegal position type: position must be of type int. You tried
                type {type(position)}""")
        elif position < 0 or position >= self.getNumCards():
            raise ValueError("""Illegal position attempted: position must be between 0 and the number of 
                remaining cards. You tried {position}""")

        return self.cards[position]

    def removeCardAt(self, position):
        """
        Removes the card at the given position from self.cards
        """
        self.cards.pop(position)

    
    def getNumCards(self):
        """
        Returns the number of cards in the deck
        """
        return len(self.cards)

    def deal(self, players, numCards) :
        """
        Deal out cards determined by the number of cards in each hand and
        the number of players to deal to.
        Parameters:
            numCards - (int) number of cards to deal to each player
            players - (int) number of players to deal cards to
        Returns a list containing a list of Cards for each player
        """
        if not isinstance(numCards, int):
            raise TypeError(f"""Illegal argument type: numCards must be of type int.
                You tried type {type(numCards)}""")
        elif not isinstance(players, int):
            raise TypeError(f"""Illegal argument type: players must be of type int. 
                You tried type {type(players)}""")
        elif players <= 0:
            raise ValueError(f"""Illegal number of players attempted: Must be greater than 0. You
                tried {players}""")
        elif numCards <= 0:
            raise ValueError(f"""Illegal number of cards attempted: Must be greater than 0. You
                tried {numCards}""")
        elif players * numCards > self.getNumCards():
            raise ValueError(f"""Too many cards/players attempted: numCards * players must be less
                than or equal to the number of cards remaining in the deck. You tried to deal 
                {players * numCards} cards and there are {self.getNumCards()} remaining""")

        # Initialize list of lists to hold players hands
        hands = [[] for player in range(players)]

        # Deals cards like a normal human
        # i.e. dealing one card to each person before repeating
        for card in range(numCards):
            for player in range(players):
                hands[player].append(self.getCardAt(0)) # Add to playeres hand
                self.removeCardAt(0) # Remove it because it's being dealt
        
        return hands

