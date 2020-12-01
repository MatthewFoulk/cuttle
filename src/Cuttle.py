
import sys
import random

import pygame

from CardGame import *
from Gui import *

class Player():

    def __init__(self):
        self.hand = []
        self.pointsCards = []
        self.permCards = []
        self.jacks = {} # Dictionary with card keys that have list of jack cards attached to them 
        self.score = 0
        self.handVisible = False # 8's make opp hand visible
        self.pointsNeededToWin = 21
        self.queenProtection = False # Queens protect against two's and jacks
        self.selectedCard = None 
        self.turnFinished = False

        # True if in the middle of playing one of these cards
        self.playingTwo = False
        self.playingThree = False
        self.playingSeven = False
        self.playingJack = False
        self.scuttling = False

    def getNumCardsInJacks(self):
        return len(self.jacks)

    def getNumCardsInHand(self):
        return len(self.hand)
    
    def getNumCardsInPointsCards(self):
        return len(self.pointsCards)
    
    def getNumCardsInPermCards(self):
        return len(self.permCards)
    
    def removeCardFromHand(self, card):
        self.hand.remove(card)

    def removeCardFromPointsCards(self, card):
        self.pointsCards.remove(card)
    
    def removeCardFromPermCards(self, card):
        self.permCards.remove(card)
    
    def removeCardFromJacks(self, card):
        self.jacks.pop(card)
    
    def removeJackFromJacks(self, card):
        self.jacks[card].pop(0)
    
    def addCardToHand(self, card):
        self.hand.append(card)
    
    def addCardToPermCards(self, card):
        self.permCards.append(card)
    
    def addCardToPointsCards(self, card):
        self.pointsCards.append(card)
    
    def playPointsCard(self):
        self.addCardToPointsCards(self.selectedCard)
        self.removeCardFromHand(self.selectedCard)
        self.turnFinished = True

    def drawCard(self, deck):
        self.hand.append(deck.drawCardAt(0)) 
    
    def playAce(self, otherPlayer, discardPile):
        """
        Discard all points cards and attached jacks
        """
        for card in self.pointsCards:
            self.discardCard(discardPile, card)
        for card in otherPlayer.pointsCards:
            otherPlayer.discardCard(discardPile, card)
        for card in self.jacks.keys():
            for jack in self.jacks[card]:
                self.discardCard(discardPile, jack)
        for card in otherPlayer.jacks.keys():
            for jack in otherPlayer.jacks[card]:
                otherPlayer.discardCard(discardPile, jack)
        
        # Remove all cards from points
        self.pointsCards = []
        otherPlayer.pointsCards = []
        self.jacks = {}
        otherPlayer.jacks = {}
    
    def playNormalTwo(self, otherPlayer, card, discardPile, currPlayer=False, isJack=False):
        """
        Use a two to remove a permanent effect card
        """
        self.discardCard(discardPile, self.selectedCard)
        self.removeCardFromHand(self.selectedCard)

        # Card being removed from otherPlayer
        if not currPlayer:

            # Card being removed is a jack
            if isJack:

                # Discard the jack
                otherPlayer.discardCard(discardPile, otherPlayer.jacks[card][0])
                otherPlayer.removeJackFromJacks(card) # Remove the jack from other's jacks

                # Add the jacks to the curr player if any remaining
                if (len(otherPlayer.jacks[card]) > 0):
                    self.jacks[card] = otherPlayer.jacks[card]
                
                # Remove from other's points and add to curr
                otherPlayer.removeCardFromPointsCards(card)
                self.addCardToPointsCards(card)

                # Remove card from other's jacks
                otherPlayer.removeCardFromJacks(card)

            # Remove Non jack perm card
            else:
                
                # Discard the cadr being 'twoed'
                otherPlayer.discardCard(discardPile, card)
                otherPlayer.removeCardFromPermCards(card)

                # If 8, reset curr player's hand visibility
                if card.value == 8:
                    self.handVisible = False
                
                # If king, reset other player's points needed to win
                elif card.value == Card.NAME_TO_VALUE["King"]:
                    otherPlayer.playKing()
                
                # If queen, reset other player's queen protection
                elif card.value == Card.NAME_TO_VALUE["Queen"]:
                    otherPlayer.queenProtection = False
        
        # Card being removed is from current player (whoops why would they do that...)
        else:

            # Card being removed is a jack
            if isJack:
                
                # Discard the jack
                self.discardCard(discardPile, self.jacks[card][0])
                self.removeJackFromJacks(card)

                # Add the card to the other player's jacks if any jacks remain
                if (len(self.jacks[card]) > 0):
                    otherPlayer.jacks[card] = self.jacks[card]
                
                # Remove the card from curr points and add to others
                self.removeCardFromPointsCards(card)
                otherPlayer.addCardToPointsCards(card)

                self.removeCardFromJacks(card) # Remove card from your own jacks
            
            # Remove Non jack perm card
            else:
                # Discard the card being 'twoed'
                self.discardCard(discardPile, card)
                self.removeCardFromPermCards(card)

                # If 8, reset other player's hand visibility
                if card.value == 8:
                    otherPlayer.handVisible = False
                
                # If king, Reset curr points needed to win
                elif card.value == Card.NAME_TO_VALUE["King"]:
                    self.playKing()

                # if queen, removed current's own protection
                elif card.value == Card.NAME_TO_VALUE["Queen"]:
                    self.queenProtection = False

        self.turnFinished = True

    def playThree(self, card, discardPile):
        """
        Add a card from the discard to the hand
        """

        # Discard three and remove from hand
        self.discardCard(discardPile, self.selectedCard)
        self.removeCardFromHand(self.selectedCard)

        # Remove card from discard pile and add to hand
        self.removeCardFromDiscard(discardPile, card)
        self.addCardToHand(card)

        self.playingThree = False
        self.turnFinished = True
        
    
    def playFour(self, otherPlayer, discardPile):
        """
        Randomly discard two cards from opponents hand
        """

        # One card remaining, so can only remove one
        if otherPlayer.getNumCardsInHand() == 1:
            cardToRemove = otherPlayer.hand[0]
            otherPlayer.discardCard(discardPile, cardToRemove)
            otherPlayer.removeCardFromHand(otherPlayer.hand[0])

        # Randomly discard two cards from opponent
        else:
            numCardsInHand = otherPlayer.getNumCardsInHand()
            firstCardToRemove = otherPlayer.hand[random.randint(0, numCardsInHand - 1)]
            secondCardToRemove = otherPlayer.hand[random.randint(0, numCardsInHand - 1)]

            # If second card choice is the same as the first
            # Choose again until its a different card
            while (secondCardToRemove == firstCardToRemove):
                secondCardToRemove = otherPlayer.hand[random.randint(0, numCardsInHand - 1)]

            otherPlayer.discardCard(discardPile, firstCardToRemove)
            otherPlayer.removeCardFromHand(firstCardToRemove)
            otherPlayer.discardCard(discardPile, secondCardToRemove)
            otherPlayer.removeCardFromHand(secondCardToRemove)
    
    def playFive(self, deck, handLimit):
        """
        Draw two cards, or one if hand is currently one less than max
        """
        self.drawCard(deck)

        if (handLimit > self.getNumCardsInHand()):
            self.drawCard(deck)
    
    def playSix(self, otherPlayer, discardPile):
        """
        Discard all permanent effect cards (jacks included)
        """
        
        for card in self.permCards:
            self.discardCard(discardPile, card)
        for card in self.jacks.keys():
            self.discardCard(discardPile, card)
            # Return card to original player
            if len(self.jacks[card]) % 2 != 0:
                self.removeCardFromPointsCards(card)
                otherPlayer.addCardToPointsCards(card)
        for card in otherPlayer.permCards:
            otherPlayer.discardCard(discardPile, card)
        for card in otherPlayer.jacks.keys():
            otherPlayer.discardCard(discardPile, card)
            # Return card to original player
            if len(otherPlayer.jacks[card]) % 2 != 0:
                otherPlayer.removeCardFromPointsCards(card)
                self.addCardToPointsCards(card)

        # Reset perm effects
        self.queenProtection = False
        self.pointsNeededToWin = 21
        self.handVisible = False
        otherPlayer.queenProtection = False
        otherPlayer.pointsNeededToWin = 21
        otherPlayer.handVisible = False

        self.permCards = []
        self.jacks = {}
        otherPlayer.permCards = []
        otherPlayer.jacks = {}

    def playSeven(self, otherPlayer, deck, discardPile):

        self.drawCard(deck)
        self.selectedCard = self.hand[self.getNumCardsInHand() - 1] # Get the newest card

        # Continue to Draw cards until one is drawn that can be played
        while(self.selectedCard.value == Card.NAME_TO_VALUE["Jack"] and
            (otherPlayer.getNumCardsInPointsCards() + self.getNumCardsInPointsCards() == 0)):
            self.drawCard(deck)
            self.selectedCard = self.hand[self.getNumCardsInHand() - 1] # Get the newest card

        self.playingSeven = True

    def playOneOffCard(self, otherPlayer, deck, discardPile, handLimit):

        # If no more actions needed (e.g. for a 2,3, or 7), then finish playing turn
        # Must go before rest of logic because 7 changes selected card
        if (self.selectedCard.value != 2 and self.selectedCard.value != 3):
            self.discardCard(discardPile, self.selectedCard)
            self.removeCardFromHand(self.selectedCard)

            # Finish turn if not playing 7
            if (self.selectedCard.value != 7):
                self.turnFinished = True

        if self.selectedCard.value == Card.NAME_TO_VALUE["Ace"]:
            self.playAce(otherPlayer, discardPile)
        elif self.selectedCard.value == 2:
            self.playingTwo = True
        elif self.selectedCard.value == 3:
            self.playingThree = True
        elif self.selectedCard.value == 4:
            self.playFour(otherPlayer, discardPile)
        elif self.selectedCard.value == 5:
            self.playFive(deck, handLimit)
        elif self.selectedCard.value == 6:
            self.playSix(otherPlayer, discardPile)
        elif self.selectedCard.value == 7:
            self.playSeven(otherPlayer, deck, discardPile)
    
    def playPermCard(self, otherPlayer):

        if self.selectedCard.value == Card.NAME_TO_VALUE["Jack"]:
            self.playingJack = True

        else:
            self.addCardToPermCards(self.selectedCard)
            self.removeCardFromHand(self.selectedCard)

            if self.selectedCard.value == 8:
                otherPlayer.handVisible = True
            elif self.selectedCard.value == Card.NAME_TO_VALUE["Queen"]:
                self.queenProtection = True
            elif self.selectedCard.value == Card.NAME_TO_VALUE["King"]:
                self.playKing()
        
            self.turnFinished = True
    
    def playJack(self, otherPlayer, card):

        # Jacked opponent, switch the card over
        if card in otherPlayer.pointsCards:
            otherPlayer.removeCardFromPointsCards(card)
            self.addCardToPointsCards(card)

            if card in otherPlayer.jacks.keys():
                self.jacks[card] = otherPlayer.jacks[card]
                self.jacks[card].append(self.selectedCard)
                otherPlayer.removeCardFromJacks(card)
            else:
                self.jacks[card] = [self.selectedCard]

        # Jacked yourself (whoops! That sucks...)
        else:
            self.removeCardFromPointsCards(card)
            otherPlayer.addCardToPointsCards(card)
            if card in self.jacks.keys():
                otherPlayer.jacks[card] = self.jacks[card]
                otherPlayer.jacks[card].append(self.selectedCard)
                self.removeCardFromJacks(card)
            else:
                otherPlayer.jacks[card] = [self.selectedCard]
        
        self.removeCardFromHand(self.selectedCard)
        self.turnFinished = True
    
    def playKing(self):
        kingCount = 0
        for card in self.permCards:
            if card.value == Card.NAME_TO_VALUE["King"]:
                kingCount += 1
        
        if kingCount == 1:
            self.pointsNeededToWin = 14
        elif kingCount == 2:
            self.pointsNeededToWin = 10
        elif kingCount == 3:
            self.pointsNeededToWin = 7
        else:
            self.pointsNeededToWin = 5
    
    def scuttle(self, otherPlayer, card, discardPile):
        # If jacks attached remove
        for testCard in otherPlayer.jacks.keys():
            if testCard == card:
                otherPlayer.removeCardFromJacks(card)
                break
        self.discardCard(discardPile, self.selectedCard)
        self.removeCardFromHand(self.selectedCard)
        otherPlayer.discardCard(discardPile, card)
        otherPlayer.removeCardFromPointsCards(card)
        self.turnFinished = True

    def discardCard(self, discardPile, card):
        discardPile.append(card)

    def removeCardFromDiscard(self, discardPile, card):
        """
        Removes given card from the discard pile
        """
        discardPile.remove(card)

    def isTwoInHand(self):
        """
        Returns true if there is a two in players hand, else false
        """
        for card in self.hand:
            if card.value == 2:
                return True
        return False

    def discardTwo(self, discardPile):
        """
        Discards the lowest value two from hand
        """
        lowestTwo = self.hand[0]

        for card in self.hand:
            if card.value == 2:
                if card < lowestTwo:
                    lowestTwo = card
        
        self.discardCard(discardPile, lowestTwo)
        self.removeCardFromHand(lowestTwo)


    def clearCurrAction(self):
        self.playingSeven = False
        self.playingJack = False
        self.playingTwo = False
        self.scuttling = False
    
    def updateScore(self):
        self.score = 0
        for card in self.pointsCards:
            self.score += card.value

class Cuttle():

    TIME_BETWEEN_TURNS = 2 * 600 # Seconds * Time in milliseconds
    HAND_LIMIT = 8 # Max limit on number of cards in hand

    def __init__(self, playerGoingFirst, dealer):
        """
        Initialize the game board
        """
    
        self.currPlayer = playerGoingFirst
        self.otherPlayer = dealer
        self.deck = Deck()
        self.winner = None

        self.imageBackOfCardInHand = None
        self.imageBackOfCardOnBoard = None 

        self.promptOtherPointsCards = False
        self.promptCurrPointsCards = False 
        self.promptOtherPermCards = False
        self.promptCurrPermCards = False

        self.cancelButton = False
        self.cancelButtonObj = None
        
        self.pointsButtonObj = None
        self.permButtonObj = None
        self.oneOffButtonObj = None
        self.scuttleButtonObj = None

        self.discardPile = [] # list of cards that have been discarded
        self.showMaxDiscard = 5
        self.discardBackButtonObj = None
        self.discardNextButtonObj = None

        self.switchingTurns = False # True if in the middle of switcing turns
        self.startWaitTime = 0 # Time when waiting for turn switch started
        self.waitTime = 0 # Amount of time since begun switching turns

        self.askTwo = False # True if two needs to be asked
        self.twoPlayer = None # Which player would be playing two
        self.twoYesButton = None
        self.twoNoButton = None
        self.twoAsked = False # True if two has been asked, False if it hasn't
    
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
    
    def clearSecondaryPrompts(self):
        self.promptOtherPointsCards = False
        self.promptCurrPointsCards = False
        self.promptOtherPermCards = False
        self.promptCurrPermCards = False
        self.cancelButtonObj = None
        self.cancelButton = False

    def clearPrimaryPrompts(self):
        self.pointsButtonObj = None
        self.permButtonObj = None
        self.oneOffButtonObj = None
        self.scuttleButtonObj = None
    
    def checkWinner(self):
        if self.currPlayer.score >= self.currPlayer.pointsNeededToWin:
            self.winner = self.currPlayer
        elif self.otherPlayer.score >= self.otherPlayer.pointsNeededToWin:
            self.winner = self.otherPlayer
    
    def promptJackPlaying(self):
        """
        Hint to the current player where they can play their Jack
        """

        # Can be played on opponent points cards
        if (self.otherPlayer.getNumCardsInPointsCards() > 0 and
            not self.otherPlayer.queenProtection):
            self.promptOtherPointsCards = True

        # Can be played on yourself
        if (self.currPlayer.getNumCardsInPointsCards() > 0 and
            not self.currPlayer.queenProtection):
            self.promptCurrPointsCards = True
        
        # Turn on the cancel button
        self.cancelButton = True
    
    def promptTwoPlaying(self):
        """
        Hint to the current player where they can play their Two
        """

        # Prompt opponent's perm area if they have an perm cards in it
        if self.otherPlayer.getNumCardsInPermCards() > 0:
            self.promptOtherPermCards = True
        
        # Prompt opp points area if opp has any jacks in their points area
        # and no queen protection
        if len(self.otherPlayer.jacks) > 0 and not self.otherPlayer.queenProtection:
            self.promptOtherPointsCards = True

        # Prompt curr player's perm area if they have perm cards in it
        if self.currPlayer.getNumCardsInPermCards() > 0:
            self.promptCurrPermCards = True
        
        # Prompt curr player's points area if they have any jacks
        # and no queen protection
        if len(self.currPlayer.jacks) > 0 and not self.currPlayer.queenProtection:
            self.promptCurrPointsCards = True
        
        # Turn on back button
        self.cancelButton = True
                    

def play(player0, player1):

    # Initialize game window
    pygame.init()
    screen = getScreen()

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
            
            # Nothing can be done besides quiting while waiting for turn to end
            # or the game is already over
            elif game.switchingTurns or game.winner is not None:
                continue

            elif event.type == pygame.MOUSEBUTTONUP:
                # Set the x, y position of the click
                clickX, clickY = event.pos
                
                # Determine if anything relevant was clicked
                deckClicked = checkDeckClicked(game, clickX, clickY)
                cancelButtonClicked = checkCancelButtonClicked(game, clickX, clickY)
                otherPointsCardClicked = checkOtherPointsClicked(game, clickX, clickY)
                otherPermCardClicked = checkOtherPermClicked(game, clickX, clickY)
                otherJackCardClicked = checkOtherJackClicked(game, clickX, clickY)
                currPointsCardClicked = checkCurrPointsClicked(game, clickX, clickY)
                currPermCardClicked = checkCurrPermClicked(game, clickX, clickY)
                currJackCardClicked = checkCurrJackClicked(game, clickX, clickY)
                permButtonClicked = checkPermButtonClicked(game, clickX, clickY)
                pointsButtonClicked = checkPointsButtonClicked(game, clickX, clickY)
                oneOffButtonClicked = checkOneOffButtonClicked(game, clickX, clickY)
                scuttleButtonClicked = checkScuttleButtonClicked(game, clickX, clickY)
                cardInHandClicked = checkCardInHandClicked(game, clickX, clickY)
                twoYesClicked = checkTwoYesButtonClicked(game, clickX, clickY)
                twoNoClicked = checkTwoNoButtonClicked(game, clickX, clickY)

                if game.askTwo:

                    if twoYesClicked:
                        if game.twoPlayer == game.otherPlayer:
                            twoInHand = game.otherPlayer.isTwoInHand()
                            if twoInHand:
                                # Discard two and switching player being asked about two
                                game.otherPlayer.discardTwo(game.discardPile)
                                game.twoPlayer = game.currPlayer

                        elif game.twoPlayer == game.currPlayer:
                            twoInHand = game.currPlayer.isTwoInHand()
                            if twoInHand:
                                game.currPlayer.discardTwo(game.discardPile)
                                game.twoPlayer = game.otherPlayer
                    elif twoNoClicked:
                        if game.twoPlayer == game.currPlayer:
                            # end their turn without completing action
                            game.askTwo = False
                            game.askedTwo = True
                            game.currPlayer.turnFinished = True
                        else:
                            game.askTwo = False
                            game.twoAsked = True # This will finish curr players one-off

                        
                        # Reset two things
                        game.twoPlayer = None
                        game.askTwo = False
                        game.twoYesButton = None
                        game.twoNoButton = None 

                # Currently in the middle of playing a three, you can NOT go back once you start
                elif game.currPlayer.playingThree:
                    cardInDiscardClicked = checkCardInDiscardClicked(game, clickX, clickY)
                    discardBackButtonClicked = checkDiscardBackButtonClicked(game, clickX, clickY)
                    discardNextButtonClicked = checkDiscardNextButtonClicked(game, clickX, clickY)
                    
                    if cardInDiscardClicked:
                        game.currPlayer.playThree(cardInDiscardClicked, game.discardPile)
                        game.showMaxDiscard = 5
                    elif discardBackButtonClicked:
                        game.showMaxDiscard -= 5
                    elif discardNextButtonClicked:
                        game.showMaxDiscard += 5

                # Clicked on cancel button, so cancel usage selection
                elif cancelButtonClicked:
                    game.clearSecondaryPrompts()
                    game.currPlayer.clearCurrAction()
                
                # Clicked on deck to draw a card 
                elif (deckClicked and not game.currPlayer.playingSeven
                    and (game.currPlayer.getNumCardsInHand() < game.HAND_LIMIT)):
                    game.currPlayer.drawCard(game.deck)
                    game.currPlayer.turnFinished = True
                    game.currPlayer.clearCurrAction()
                    game.clearPrimaryPrompts()
                    game.clearSecondaryPrompts()
                
                # Change selected card
                elif (cardInHandClicked is not None and 
                    not game.currPlayer.playingSeven):
                    # Deselect cards
                    if cardInHandClicked == game.currPlayer.selectedCard: 
                        game.currPlayer.selectedCard = None
                    # Select card
                    else:
                        game.currPlayer.selectedCard = cardInHandClicked
                    game.currPlayer.clearCurrAction()
                    game.clearSecondaryPrompts()

                # In the process of playing a two
                elif game.currPlayer.playingTwo:
                    # If perm card (jacks included) is clicked, play two
                    # (unless queen protect, then must be a queen clicked)
                    if (otherPermCardClicked is not None
                        and (not game.otherPlayer.queenProtection or
                        otherPermCardClicked.value == Card.NAME_TO_VALUE["Queen"])):
                        game.currPlayer.playNormalTwo(game.otherPlayer, 
                            otherPermCardClicked, game.discardPile)
                        game.clearSecondaryPrompts()
                    elif otherJackCardClicked is not None and not game.otherPlayer.queenProtection:
                        game.currPlayer.playNormalTwo(game.otherPlayer, 
                            otherJackCardClicked, game.discardPile,isJack=True)
                        game.clearSecondaryPrompts()
                    elif (currPermCardClicked is not None
                        and (not game.currPlayer.queenProtection or
                        currPermCardClicked.value == Card.NAME_TO_VALUE["Queen"])):
                        game.currPlayer.playNormalTwo(game.otherPlayer, 
                            currPermCardClicked, game.discardPile, currPlayer=True)
                        game.clearSecondaryPrompts()
                    elif (currJackCardClicked is not None and not game.currPlayer.queenProtection):
                        game.currPlayer.playNormalTwo(game.otherPlayer, 
                            currJackCardClicked, game.discardPile, currPlayer=True,
                            isJack=True)
                        game.clearSecondaryPrompts()

                # Currently in the process of playing a Jack
                elif game.currPlayer.playingJack:
                    # If any point card is clicked and no queen protection, 
                    # finish playing the jack
                    if (otherPointsCardClicked is not None and 
                        not game.otherPlayer.queenProtection):
                        game.currPlayer.playJack(game.otherPlayer, otherPointsCardClicked)
                        game.clearSecondaryPrompts()
                    elif (currPointsCardClicked is not None and 
                        not game.currPlayer.queenProtection):
                        game.currPlayer.playJack(game.otherPlayer, currPointsCardClicked)
                        game.clearSecondaryPrompts()

                # In the process of scuttling
                elif game.currPlayer.scuttling:
                    # If any opponent point card is clicked, scuttle
                    if otherPointsCardClicked is not None:
                        game.currPlayer.scuttle(game.otherPlayer,
                             otherPointsCardClicked, game.discardPile)
                        game.clearSecondaryPrompts()

                # Play the selected card as a permanent effect
                elif permButtonClicked:
                    # If Jack then turn on prompts for playing jack
                    if game.currPlayer.selectedCard.value == Card.NAME_TO_VALUE["Jack"]:
                        game.promptJackPlaying()
                    game.currPlayer.playPermCard(game.otherPlayer)
                    game.clearPrimaryPrompts()

                # Play the selected card for points
                elif pointsButtonClicked:
                    game.currPlayer.playPointsCard()
                    game.clearPrimaryPrompts()

                # Play the selected card as a one-off effect
                # or if all possible twos have been played or asked to play
                # and denied
                elif oneOffButtonClicked or game.twoAsked:
                    # If two is finished asking, then complete one off
                    if game.twoAsked:
                        if game.currPlayer.selectedCard.value == 2:
                            game.promptTwoPlaying()
                        game.currPlayer.playOneOffCard(game.otherPlayer, game.deck, 
                            game.discardPile, game.HAND_LIMIT)
                        game.clearPrimaryPrompts()
                        game.askTwo = False
                        game.twoAsked = False
                    # Prompt two before completing one-off
                    else:
                        game.twoPlayer = game.otherPlayer # First person to ask about two
                        game.askTwo = True
                
                # Play the selected card as a scuttle
                elif scuttleButtonClicked:
                    game.currPlayer.scuttling = True
                    game.promptOtherPointsCards = True
                    game.cancelButton = True
                    game.clearPrimaryPrompts()

        # Clear screen and set background color
        screen.fill(GREEN)

        # Draw points and perm indicator words
        drawBoardIndicators(screen)

        # Prepare to switch players if turn is ending
        if game.currPlayer.turnFinished:
            game.currPlayer.selectedCard = None # Reset for next turn
            game.clearPrimaryPrompts() # Reset for next turn
            game.clearSecondaryPrompts() # Reset for next turn
        
        # Draw the deck and card count if cards left
        if game.deck.getNumCards() > 0:
            # Draw deck image
            drawDeckImage(game, screen)

            # Draw number of cards in deck
            drawNumCardsInDeck(game, screen)

        # Draw players' scores
        game.currPlayer.updateScore()
        game.otherPlayer.updateScore()
        drawPlayersScore(game, screen)

        # Draw top card in discard pile, if any have been discarded
        numCardsInDiscard = game.getNumCardsInDiscard()
        if numCardsInDiscard > 0:
            if not game.currPlayer.playingThree:
                drawDiscardPile(game, screen)
            else:
                game.clearPrimaryPrompts()
                drawCardsInDiscard(game, screen)
                drawDiscardButtons(game, screen)
        
        # Draw players' hands
        drawPlayersHands(game, screen)

        # Prompt for card usage if selected and not playing three
        if (game.currPlayer.selectedCard is not None
            and not game.currPlayer.playingThree):
            promptCardUsage(game, screen)
        
        # Draw players' points cards
        drawPointsCards(game, screen)

        # Draw players' permanent effect cards
        drawPermCards(game, screen)

        # Draw players' jacks
        drawJacks(game, screen)

        # Display two question if needed
        if game.askTwo:
            drawTwoResponsePrompt(game, screen, game.twoPlayer)

        if game.winner is not None:
            if game.winner == game.currPlayer:
                drawWinner(game, screen)
        elif game.switchingTurns:
            drawSwitchingTurns(game, screen)
            game.waitTime = pygame.time.get_ticks() - game.startWaitTime
            if game.waitTime > game.TIME_BETWEEN_TURNS:
                game.switchingTurns = False
                game.switchPlayerTurn()
        elif game.currPlayer.turnFinished:
            game.switchingTurns = True
            game.startWaitTime = pygame.time.get_ticks()
            game.currPlayer.turnFinished = False # Reset for next turn
            game.currPlayer.clearCurrAction()
            game.checkWinner()
        
        pygame.display.flip()