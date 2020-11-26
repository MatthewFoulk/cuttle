
import sys

import pygame

from CardGame import *

# Directory where images for the game board are stored
# e.g. card images
IMAGES_FILE_DIRECTORY = "images/"

# Back of card image file name
BACK_OF_CARD_IMAGE_FILE = "RedBackVertical.gif"

# Pygame display dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_DIM = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Card image dimensions (originally 71x96)
CARD_IN_HAND_WIDTH = 71
CARD_IN_HAND_HEIGHT = 96
CARD_IN_HAND_DIM = (CARD_IN_HAND_WIDTH, CARD_IN_HAND_HEIGHT)

CARD_ON_BOARD_WIDTH = int(CARD_IN_HAND_WIDTH * .9)
CARD_ON_BOARD_HEIGHT = int(CARD_IN_HAND_HEIGHT * .9)
CARD_ON_BOARD_DIM = (CARD_ON_BOARD_WIDTH, CARD_ON_BOARD_HEIGHT)

# Player hand positions on board
CURR_PLAYER_HAND_X = int(SCREEN_WIDTH * 0.5)
CURR_PLAYER_HAND_Y = int(SCREEN_HEIGHT - (1.25 * CARD_IN_HAND_HEIGHT))
OTHER_PLAYER_HAND_X = int(SCREEN_WIDTH * .5)
OTHER_PLAYER_HAND_Y = int((.25 * CARD_IN_HAND_HEIGHT))

# Deck position on board
DECK_X = int(SCREEN_WIDTH - (CARD_ON_BOARD_WIDTH * 1.25))
DECK_Y = int((SCREEN_HEIGHT * .5) - CARD_ON_BOARD_HEIGHT)  
DECK_POS = (DECK_X, DECK_Y)

# Discard pile position on board
DISCARD_X = int(SCREEN_WIDTH - (CARD_ON_BOARD_WIDTH * 1.25))
DISCARD_Y = int(SCREEN_HEIGHT * 0.5)
DISCARD_POS = (DISCARD_X, DISCARD_Y)

# Pygame fonts
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 30)

# Colors RGB
GREEN = (0, 153, 0)
WHITE = (255, 255, 255)

class Player():

    def __init__(self, game = None):
        self.hand = []
        self.pointCards = []
        self.permCards = []
        self.points = 0
        self.game = game

    def getNumCardsInHand(self):
        return len(self.hand)
    
    def setGame(self, game):
        self.game = game
    
    def drawCard(self):
        self.game.currPlayer.hand.append(self.game.deck.drawCardAt(0)) 

class Cuttle():

    def __init__(self, playerGoingFirst, dealer):
        """
        Initialize the game board
        """

        # Add the games to the players
        playerGoingFirst.game = self
        dealer.game = self
    
        self.currPlayer = playerGoingFirst
        self.otherPlayer = dealer
        self.deck = Deck()

        self.imageBackOfCardInHand = None # TODO IDK WHERE TO KEEP THIS
        self.imageBackOfCardOnBoard = None # TODO IDK WHERE TO KEEP THIS

        self.discardPile = [] # list of cards that have been discarded
    
    def switchPlayerTurn(self):
        """
        Switches the current player and the other player
        """
        temp = self.currPlayer
        self.currPlayer = self.otherPlayer
        self.otherPlayer = temp
    
    def getLastDiscarded(self):
        return self.discardPile[len(self.discardPile) - 1]

    def getNumCardsInDiscard(self):
        return len(self.discardPile)

    def dealStartingHands(self):
        """
        Deals 6 cards to the dealer and 5 cards to the non-dealer.
        """
        hands = self.deck.deal(2, 5) 
        hands[1].append(self.deck.drawCardAt(0)) # Add the extra card to the dealer's hand [[dealers hand], [playerGoingFirst]]
        self.currPlayer.hand = hands[0]
        self.otherPlayer.hand = hands[1]

def loadCardImages(game):
    """
    Load all of the card images to the game board
    """
    if not isinstance(game, Cuttle):
        raise TypeError(f"""Illegal argument type: 'game' must be of type Cuttle. You tried
            type {type(game)}""")

    # Load normal card images
    for card in game.deck.cards:
        image = pygame.image.load(IMAGES_FILE_DIRECTORY + card.getImageFileName())
        card.imageInHand = pygame.transform.scale(image, CARD_IN_HAND_DIM)
        card.imageOnBoard = pygame.transform.scale(image, CARD_ON_BOARD_DIM)
    
    # Load back of card image
    # TODO I'm not sure if this is in the right place
    image = pygame.image.load(IMAGES_FILE_DIRECTORY + BACK_OF_CARD_IMAGE_FILE)
    game.imageBackOfCardInHand = pygame.transform.scale(image, CARD_IN_HAND_DIM)
    game.imageBackOfCardOnBoard = pygame.transform.scale(image, CARD_ON_BOARD_DIM)

def drawDeckImage(screen, game):
    return screen.blit(game.imageBackOfCardOnBoard, DECK_POS)

def drawNumCardsInDeck(screen, game, deckImage):
    numCardsDeckText = FONT.render(str(game.deck.getNumCards()), True, WHITE)
    numCardsDeckTextRect = numCardsDeckText.get_rect()
    numCardsDeckTextRect.center = deckImage.center # Centers text on deck image
    screen.blit(numCardsDeckText, numCardsDeckTextRect)
    

def play(player0, player1):

    # Initialize game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a new game
    game = Cuttle(player0, player1)

    # Load card images
    loadCardImages(game)

    # Shuffle the starting deck
    game.deck.shuffle()

    # Deal starting hands
    game.dealStartingHands()

    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Set the x, y position of the click
                clickX, clickY = event.pos

                # Deck clicked, draw card
                if deckImage.collidepoint(clickX, clickY):
                    game.currPlayer.drawCard()

        # Clear screen and set background color
        screen.fill(GREEN)
        
        # Don't draw the deck if there are no cards left
        if game.deck.getNumCards() > 0:
            # Draw deck image
            deckImage = drawDeckImage(screen, game)

            # Draw number of cards in deck
            numCardsDeckText = drawNumCardsInDeck(screen, game, deckImage)

        # Draw current player's points
        currPlayerPoints = game.currPlayer.points
        currPlayerPointsText = FONT.render(str(currPlayerPoints), True, WHITE)
        # TODO where to put this

        # Draw opponent (i.e. 'non-current') player's score
        otherPlayerPoints = game.otherPlayer.points
        otherPlayerPointsText = FONT.render(str(otherPlayerPoints), True, WHITE)
        # TODO where to put this

        # Draw top card in discard pile
        if game.getNumCardsInDiscard() > 0:
            lastDiscarded = game.getLastDiscarded()
            screen.blit(lastDiscarded.imageOnBoard, DISCARD_POS)

        # Draw number of cards in discard pile
        
        # Draw current player's hand
        width = int(CURR_PLAYER_HAND_X ) - ((SCREEN_WIDTH * 0.05) * (game.currPlayer.getNumCardsInHand() * .5))

        for card in game.currPlayer.hand:
            screen.blit(card.imageInHand, (width, CURR_PLAYER_HAND_Y))
            width += int(SCREEN_WIDTH * .05) 
        
        # Draw the other (i.e. 'non-current') player's hand face down
        width = int(OTHER_PLAYER_HAND_X ) - ((SCREEN_WIDTH * 0.05) * (game.otherPlayer.getNumCardsInHand() * .5))

        for card in game.otherPlayer.hand:
            screen.blit(game.imageBackOfCardInHand, (width, OTHER_PLAYER_HAND_Y))
            width += int(SCREEN_WIDTH * .05)
        
        # Draw current player's point cards

        # Draw other player's point cards

        # Draw current player's permanent effect cards

        # Draw other player's permanent effect cards

        pygame.display.flip()