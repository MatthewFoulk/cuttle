
import pygame

from CardGame import *

### NOTE THERE ARE INCONSISTENCIES ON HOW I DREW OBJECTS ###
# Sometimes I used the x,y for the top left corner, other times for the center


# Directory where images for the game board are stored
# e.g. card images
IMAGES_FILE_DIRECTORY = "src/images/"

# Directory where fonts are stored
FONTS_DIRECTORY = "src/fonts/"

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

# Minimum spacing between objects
MINI_BUFFER = 1
BUFFER = 4

# Player hand positions on board (partial cards)
CURR_PLAYER_HAND_X = int((SCREEN_WIDTH * .5))
CURR_PLAYER_HAND_Y = int(SCREEN_HEIGHT - (.5 * CARD_IN_HAND_HEIGHT))
CURR_PLAYER_SELECTED_CARD_Y = int(CURR_PLAYER_HAND_Y - (.1 * CARD_IN_HAND_HEIGHT))
OTHER_PLAYER_HAND_X = int((SCREEN_WIDTH * .5) - (CARD_ON_BOARD_WIDTH))
OTHER_PLAYER_HAND_Y = int((-.5 * CARD_IN_HAND_HEIGHT))

# Deck position on board
DECK_X = int(SCREEN_WIDTH - (CARD_ON_BOARD_WIDTH + BUFFER))
DECK_Y = int((SCREEN_HEIGHT * .5) - (CARD_ON_BOARD_HEIGHT + (2 * BUFFER))) 
DECK_POS = (DECK_X, DECK_Y)

# Discard pile position on board
DISCARD_X = int(SCREEN_WIDTH - (CARD_ON_BOARD_WIDTH + BUFFER))
DISCARD_Y = int((SCREEN_HEIGHT * 0.5) + (2 * BUFFER))
DISCARD_POS = (DISCARD_X, DISCARD_Y)

# Button for card usage
USAGE_BUTTON_WIDTH = CARD_IN_HAND_WIDTH
USAGE_BUTTON_HEIGHT = 15

# Curr player's permanent effect space
CURR_PLAYER_PERM_CARDS_RECT_X = BUFFER
CURR_PLAYER_PERM_CARDS_RECT_Y = int((SCREEN_HEIGHT * .5) + (2 * BUFFER))
CURR_PLAYER_PERM_CARDS_RECT_WIDTH = int((3 * CARD_ON_BOARD_WIDTH) + (4 * BUFFER))
CURR_PLAYER_PERM_CARDS_RECT_HEIGHT = int((2 * CARD_ON_BOARD_HEIGHT) + (3 * BUFFER))

# Curr player's permanent effecet cards
CURR_PLAYER_PERM_CARDS_X = CURR_PLAYER_PERM_CARDS_RECT_X + BUFFER
CURR_PLAYER_PERM_CARDS_Y = int(CURR_PLAYER_PERM_CARDS_RECT_Y + 5)

# Other player's permanent effect space
OTHER_PLAYER_PERM_CARDS_RECT_X = BUFFER
OTHER_PLAYER_PERM_CARDS_RECT_Y = int((SCREEN_HEIGHT * .5) - ((2 * CARD_ON_BOARD_HEIGHT) + (5 * BUFFER)))
OTHER_PLAYER_PERM_CARDS_RECT_WIDTH = int((3 * CARD_ON_BOARD_WIDTH) + (4 * BUFFER))
OTHER_PLAYER_PERM_CARDS_RECT_HEIGHT = int((2 * CARD_ON_BOARD_HEIGHT) + (3 * BUFFER))

# Other player's permanent effect cards
OTHER_PLAYER_PERM_CARDS_X = OTHER_PLAYER_PERM_CARDS_RECT_X + BUFFER
OTHER_PLAYER_PERM_CARDS_Y = int((SCREEN_HEIGHT * .5) - (CARD_ON_BOARD_HEIGHT + (3 * BUFFER)))

# Curr player points space
CURR_PLAYER_POINTS_CARDS_RECT_X = (CURR_PLAYER_PERM_CARDS_RECT_WIDTH + 
    CURR_PLAYER_PERM_CARDS_RECT_X + BUFFER)
CURR_PLAYER_POINTS_CARDS_RECT_Y = int((SCREEN_HEIGHT * .5) + (2 * BUFFER))
CURR_PLAYER_POINTS_CARDS_RECT_WIDTH = int(SCREEN_WIDTH - (CURR_PLAYER_PERM_CARDS_RECT_WIDTH + 
    CARD_ON_BOARD_WIDTH + (4 * BUFFER)))
CURR_PLAYER_POINTS_CARDS_RECT_HEIGHT = int((2 * CARD_ON_BOARD_HEIGHT) + (3 * BUFFER))

# Curr player points cards
CURR_PLAYER_POINTS_CARDS_X = CURR_PLAYER_POINTS_CARDS_RECT_X + BUFFER
CURR_PLAYER_POINTS_CARDS_Y = CURR_PLAYER_POINTS_CARDS_RECT_Y + BUFFER

# Other player points space
OTHER_PLAYER_POINTS_CARDS_RECT_X = (CURR_PLAYER_PERM_CARDS_RECT_WIDTH + 
    CURR_PLAYER_PERM_CARDS_RECT_X + BUFFER)
OTHER_PLAYER_POINTS_CARDS_RECT_Y = int((SCREEN_HEIGHT * .5) - ((2 * CARD_ON_BOARD_HEIGHT) + (5 * BUFFER)))
OTHER_PLAYER_POINTS_CARDS_RECT_WIDTH = int(SCREEN_WIDTH - (OTHER_PLAYER_PERM_CARDS_RECT_WIDTH + 
    CARD_ON_BOARD_WIDTH + (4 * BUFFER)))
OTHER_PLAYER_POINTS_CARDS_RECT_HEIGHT = int((2 * CARD_ON_BOARD_HEIGHT) + (3 * BUFFER))

# Other player points cards
OTHER_PLAYER_POINTS_CARDS_X = OTHER_PLAYER_POINTS_CARDS_RECT_X + BUFFER
OTHER_PLAYER_POINTS_CARDS_Y = int((SCREEN_HEIGHT * .5) - (CARD_ON_BOARD_HEIGHT + (3 * BUFFER)))

# Jacks
CURR_PLAYER_JACKS_Y = int(CURR_PLAYER_POINTS_CARDS_RECT_Y + (CARD_ON_BOARD_HEIGHT * .3))
OTHER_PLAYER_JACKS_Y = int(OTHER_PLAYER_POINTS_CARDS_Y - (CARD_ON_BOARD_HEIGHT * .3))

# Scores center
CURR_PLAYER_SCORE_X = int(SCREEN_WIDTH * .95)
CURR_PLAYER_SCORE_Y = (11 * BUFFER)
OTHER_PLAYER_SCORE_X = int(SCREEN_WIDTH * .95)
OTHER_PLAYER_SCORE_Y = (5 * BUFFER)

# Alerts (e.g. winner, loser, switching turns)
ALERT_X = int(SCREEN_WIDTH * .5)
ALERT_Y = int((CARD_ON_BOARD_HEIGHT * .5) +  BUFFER + 30)

# Discard cards display when playing three
DISCARD_CARD_X = DISCARD_X
DISCARD_CARD_Y = DISCARD_Y
MAX_DISCARDS = 5 # Max number of cards to show from discard at a time starting at 4

# Discard (3) navigation buttons
NAVIGATION_BUTTON_WIDTH = CARD_ON_BOARD_WIDTH
NAVIGATION_BUTTON_HEIGHT = 20
NAVIGTAION_BUTTON_X = DISCARD_CARD_X
NEXT_BUTTON_Y = (DISCARD_CARD_Y + (2.5 * CARD_ON_BOARD_HEIGHT) + BUFFER)
BACK_BUTTON_Y = (NEXT_BUTTON_Y + NAVIGATION_BUTTON_HEIGHT + BUFFER)

# Board card position indicators
PERM_INDICATOR_X = (CURR_PLAYER_PERM_CARDS_RECT_X + CURR_PLAYER_PERM_CARDS_RECT_WIDTH * .5)
PERM_INDICATOR_Y = SCREEN_HEIGHT * .5
POINTS_INDICATOR_X = (CURR_PLAYER_POINTS_CARDS_RECT_X + CURR_PLAYER_POINTS_CARDS_RECT_WIDTH * .5)
POINTS_INDICATOR_Y = SCREEN_HEIGHT * .5

# Two question box
TWO_QUESTION_X = SCREEN_WIDTH * .5
TWO_QUESTION_Y = SCREEN_HEIGHT * .5
TWO_YES_X = SCREEN_WIDTH * .5
TWO_YES_Y = SCREEN_HEIGHT * .5 + 20 + BUFFER # twenty for the font size
TWO_NO_X = SCREEN_WIDTH * .5
TWO_NO_Y = TWO_YES_Y + 20 + BUFFER # twenty for the font size

# Pygame fonts
pygame.font.init()
ALERT_FONT = pygame.font.SysFont(FONTS_DIRECTORY + "OpenSans-Regular.ttf", 60)
DECK_FONT = pygame.font.Font(FONTS_DIRECTORY + "OpenSans-Regular.ttf", 30)
POINTS_FONT = pygame.font.SysFont(FONTS_DIRECTORY + "OpenSans-Regular.ttf", 25)
BUTTON_FONT = pygame.font.SysFont(FONTS_DIRECTORY + "OpenSans-Regular.ttf", 14)
INDICATOR_FONT = pygame.font.SysFont(FONTS_DIRECTORY + "OpenSans-Regular.ttf", 20)
QUESTION_FONT = pygame.font.SysFont(FONTS_DIRECTORY + "OpenSans-Regular.ttf", 30)

# Colors RGB
BRIGHT_GREEN = (0, 255, 0)
GREEN = (0, 153, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def getScreen():
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def loadCardImages(game):
    """
    Load all of the card images to the game board
    """
    # Load normal card images
    for card in game.deck.cards:
        image = pygame.image.load(IMAGES_FILE_DIRECTORY + card.getImageFileName())
        card.imageInHand = pygame.transform.scale(image, CARD_IN_HAND_DIM)
        card.imageOnBoard = pygame.transform.scale(image, CARD_ON_BOARD_DIM)
    
    # Load back of card image
    image = pygame.image.load(IMAGES_FILE_DIRECTORY + BACK_OF_CARD_IMAGE_FILE)
    game.imageBackOfCardInHand = pygame.transform.scale(image, CARD_IN_HAND_DIM)
    game.imageBackOfCardOnBoard = pygame.transform.scale(image, CARD_ON_BOARD_DIM)

def drawDeckImage(game, screen):
    game.deck.imageObj = screen.blit(game.imageBackOfCardOnBoard, DECK_POS)

def drawNumCardsInDeck(game, screen):
    numCardsDeckText = DECK_FONT.render(str(game.deck.getNumCards()), True, WHITE)
    numCardsDeckTextRect = numCardsDeckText.get_rect()
    numCardsDeckTextRect.center = game.deck.imageObj.center # Centers text on deck image
    screen.blit(numCardsDeckText, numCardsDeckTextRect)

def drawPlayersScore(game, screen):
    # Draw current player's points
    currPlayerScore = game.currPlayer.score
    currPlayerScoreText = POINTS_FONT.render("YOU: " + str(currPlayerScore), True, WHITE)
    currPlayerScoreTextRect = currPlayerScoreText.get_rect()
    currPlayerScoreTextRect.center = (CURR_PLAYER_SCORE_X, CURR_PLAYER_SCORE_Y) 
    screen.blit(currPlayerScoreText, currPlayerScoreTextRect)

    # Draw other (i.e. 'non-current') player's score
    otherPlayerScore = game.otherPlayer.score
    otherPlayerScoreText = POINTS_FONT.render("OPP: " + str(otherPlayerScore), True, WHITE)
    otherPlayerScoreTextRect = otherPlayerScoreText.get_rect()
    otherPlayerScoreTextRect.center = (OTHER_PLAYER_SCORE_X, OTHER_PLAYER_SCORE_Y)
    screen.blit(otherPlayerScoreText, otherPlayerScoreTextRect)

def drawDiscardPile(game, screen):
    # Draw top card in discard pile
    lastDiscarded = game.getLastDiscarded()
    screen.blit(lastDiscarded.imageOnBoard, DISCARD_POS)

def drawCardsInDiscard(game, screen):

    numCardsInDiscard = game.getNumCardsInDiscard()

    # Establish last card to display
    if game.showMaxDiscard > numCardsInDiscard:
        lastCardIndex = -1 # One less than the minimum index of 0
    else:
        lastCardIndex = numCardsInDiscard - game.showMaxDiscard - 1

    # Establish first card to display
    firstCardIndex = numCardsInDiscard - game.showMaxDiscard + MAX_DISCARDS - 1

    y = DISCARD_CARD_Y
    for index in range(firstCardIndex, lastCardIndex, -1):
        card = game.discardPile[index]
        card.imageObj = screen.blit(card.imageOnBoard, (DISCARD_CARD_X, y))
        y += (CARD_ON_BOARD_HEIGHT * .35)

def drawDiscardButtons(game, screen):
    
    # Draw Next Button if more cards to show
    if game.showMaxDiscard < game.getNumCardsInDiscard():
        nextButtonY = NEXT_BUTTON_Y
        nextButton = pygame.Rect(NAVIGTAION_BUTTON_X, nextButtonY, NAVIGATION_BUTTON_WIDTH, 
            NAVIGATION_BUTTON_HEIGHT)
        nextText = BUTTON_FONT.render("NEXT-->", True, WHITE)
        nextTextRect = nextText.get_rect()
        nextTextRect.center = nextButton.center
        game.discardNextButtonObj = pygame.draw.rect(screen, BLACK, nextButton)
        screen.blit(nextText, nextTextRect)
    else:
        game.discardNextButtonObj = None

    # Draw Back Button if cards to go back to 
    if game.showMaxDiscard > MAX_DISCARDS:
        backButtonY = BACK_BUTTON_Y
        backButton = pygame.Rect(NAVIGTAION_BUTTON_X, backButtonY, NAVIGATION_BUTTON_WIDTH, 
            NAVIGATION_BUTTON_HEIGHT)
        backText = BUTTON_FONT.render("<--BACK", True, WHITE)
        backTextRect = backText.get_rect()
        backTextRect.center = backButton.center
        game.discardBackButtonObj = pygame.draw.rect(screen, BLACK, backButton)
        screen.blit(backText, backTextRect)
    else:
         game.discardBackButtonObj = None

def drawPlayersHands(game, screen):
    # Draw current player's hand
    x = int(CURR_PLAYER_HAND_X - (game.currPlayer.getNumCardsInHand() * .3 * (CARD_ON_BOARD_WIDTH)))
    for card in game.currPlayer.hand:
        # Raise selected card
        if card == game.currPlayer.selectedCard:
            card.imageObj = screen.blit(card.imageInHand, (x, CURR_PLAYER_SELECTED_CARD_Y))
        else:
            card.imageObj = screen.blit(card.imageInHand, (x, CURR_PLAYER_HAND_Y))
        x += int(CARD_ON_BOARD_WIDTH * .5)
    
    # Draw the other (i.e. 'non-current') player's hand 
    x = int(OTHER_PLAYER_HAND_X + ((game.otherPlayer.getNumCardsInHand() * .3) * (CARD_ON_BOARD_WIDTH)))
    for card in game.otherPlayer.hand:
        if game.otherPlayer.handVisible:
            screen.blit(card.imageInHand, (x, OTHER_PLAYER_HAND_Y))
        else:
            screen.blit(game.imageBackOfCardInHand, (x, OTHER_PLAYER_HAND_Y))
        x -= int(CARD_ON_BOARD_WIDTH * .5)

def promptCardUsage(game, screen):

    # Selected card value
    cardValue = game.currPlayer.selectedCard.value

    # Rectangle holding selected card
    selectedCardRect = game.currPlayer.selectedCard.imageObj

    # Usage selected, provide option to go back
    if game.cancelButton:
        cancelButtonX = selectedCardRect.x
        cancelButtonY = selectedCardRect.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
        cancelButton = pygame.Rect(cancelButtonX, cancelButtonY, USAGE_BUTTON_WIDTH, 
            USAGE_BUTTON_HEIGHT)
        cancelText = BUTTON_FONT.render("CANCEL", True, WHITE)
        cancelTextRect = cancelText.get_rect()
        cancelTextRect.center = cancelButton.center
        game.cancelButtonObj = pygame.draw.rect(screen, RED, cancelButton)
        screen.blit(cancelText, cancelTextRect)

    # Provide options for card usage
    else:
        # Possible uses
        points = False
        perm = False
        oneOff = False
        scuttle = False

        if cardValue <= 10:
            points = True
            # Check if scuttle is possible
            for card in game.otherPlayer.pointsCards:
                # Opp has lower card, so scuttle possible
                if card < game.currPlayer.selectedCard:
                    scuttle = True

        if cardValue == Card.NAME_TO_VALUE["Ace"]:
            oneOff = True
        elif cardValue == 2:
            # One off possible if any perm cards on table
            if ((game.otherPlayer.getNumCardsInPermCards() + 
                game.otherPlayer.getNumCardsInJacks() + 
                game.currPlayer.getNumCardsInPermCards() +
                game.currPlayer.getNumCardsInJacks())> 0):
                oneOff = True
        elif cardValue == 3:
            # One off possible if any cards in discard
            if game.getNumCardsInDiscard() > 0:
                oneOff = True
        elif cardValue == 4:
            # One off possible if opponent has any cards in hand
            if game.otherPlayer.getNumCardsInHand() > 0:
                oneOff = True
        elif cardValue == 5:
            # One off possible if any cards in deck and hand less than max
            if (game.deck.getNumCards() > 0 and 
                game.currPlayer.getNumCardsInHand() <= game.HAND_LIMIT ):
                oneOff = True
        elif cardValue == 6:
            oneOff = True
        elif cardValue == 7:
            # One off possible if any cards in deck
            if game.deck.getNumCards() > 0:
                oneOff = True
        elif cardValue == Card.NAME_TO_VALUE["Jack"]:
            if ((game.currPlayer.getNumCardsInPointsCards() > 0 and 
                not game.currPlayer.queenProtection) or
                (game.otherPlayer.getNumCardsInPointsCards() > 0 and
                not game.otherPlayer.queenProtection)):
                perm = True
        elif (cardValue == Card.NAME_TO_VALUE["Queen"]
            or cardValue == Card.NAME_TO_VALUE["King"]
            or cardValue == 8):
            perm = True
            
        
        if points:
            pointsButtonX = selectedCardRect.x
            pointsButtonY = selectedCardRect.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            pointsButton = pygame.Rect(pointsButtonX, pointsButtonY, USAGE_BUTTON_WIDTH, 
                USAGE_BUTTON_HEIGHT)
            pointsText = BUTTON_FONT.render("Points", True, WHITE)
            pointsTextRect = pointsText.get_rect()
            pointsTextRect.center = pointsButton.center
            game.pointsButtonObj = pygame.draw.rect(screen, BLACK, pointsButton)
            screen.blit(pointsText, pointsTextRect)
        else:
            game.pointsButtonObj = None

        if perm:
            permButtonX = selectedCardRect.x
            if points:
                permButtonY = game.pointsButtonObj.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            else:
                permButtonY = selectedCardRect.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            permButton = pygame.Rect(permButtonX, permButtonY, USAGE_BUTTON_WIDTH, 
                USAGE_BUTTON_HEIGHT)
            permText = BUTTON_FONT.render("Permanent", True, WHITE)
            permTextRect = permText.get_rect()
            permTextRect.center = permButton.center
            game.permButtonObj = pygame.draw.rect(screen, BLACK, permButton)
            screen.blit(permText, permTextRect)
        else:
            game.permButtonObj = None

        if oneOff:
            oneOffButtonX = selectedCardRect.x
            if points:
                oneOffButtonY = game.pointsButtonObj.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            else:
                oneOffButtonY = selectedCardRect.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            oneOffButton = pygame.Rect(oneOffButtonX, oneOffButtonY, USAGE_BUTTON_WIDTH, 
                USAGE_BUTTON_HEIGHT)
            oneOffText = BUTTON_FONT.render("One-Off", True, WHITE)
            oneOffTextRect = oneOffText.get_rect()
            oneOffTextRect.center = oneOffButton.center
            game.oneOffButtonObj = pygame.draw.rect(screen, BLACK, oneOffButton)
            screen.blit(oneOffText, oneOffTextRect)
        else:
            game.oneOffButtonObj = None

        if scuttle:
            scuttleButtonX = selectedCardRect.x
            if points and not oneOff and not perm:
                scuttleButtonY = game.pointsButtonObj.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            elif oneOff:
                scuttleButtonY = game.oneOffButtonObj.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            elif perm:
                scuttleButtonY = game.permButtonObj.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            else:
                scuttleButtonY = selectedCardRect.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            scuttleButton = pygame.Rect(scuttleButtonX, scuttleButtonY, USAGE_BUTTON_WIDTH, 
                USAGE_BUTTON_HEIGHT)
            scuttleText = BUTTON_FONT.render("Scuttle", True, WHITE)
            scuttleTextRect = scuttleText.get_rect()
            scuttleTextRect.center = scuttleButton.center
            game.scuttleButtonObj = pygame.draw.rect(screen, BLACK, scuttleButton)
            screen.blit(scuttleText, scuttleTextRect)
        else:
            game.scuttleButtonObj = None
        
        if not any([points, perm, oneOff, scuttle]):
            noneButtonX = selectedCardRect.x
            noneButtonY = selectedCardRect.y - USAGE_BUTTON_HEIGHT - MINI_BUFFER
            noneButton = pygame.Rect(noneButtonX, noneButtonY, USAGE_BUTTON_WIDTH, 
                USAGE_BUTTON_HEIGHT)
            noneText = BUTTON_FONT.render("NO ACTIONS", True, WHITE)
            noneTextRect = noneText.get_rect()
            noneTextRect.center = noneButton.center
            pygame.draw.rect(screen, RED, noneButton)
            screen.blit(noneText, noneTextRect)
        
def drawCurrPointsCardsRect(screen, color):
    currPlayerPointsCardsRect = pygame.Rect(CURR_PLAYER_POINTS_CARDS_RECT_X, CURR_PLAYER_POINTS_CARDS_RECT_Y, 
        CURR_PLAYER_POINTS_CARDS_RECT_WIDTH, CURR_PLAYER_POINTS_CARDS_RECT_HEIGHT)
    pygame.draw.rect(screen, color, currPlayerPointsCardsRect, 1)

def drawOtherPointsCardsRect(screen, color):
    otherPlayerPointsCardsRect = pygame.Rect(OTHER_PLAYER_POINTS_CARDS_RECT_X, OTHER_PLAYER_POINTS_CARDS_RECT_Y, 
        OTHER_PLAYER_POINTS_CARDS_RECT_WIDTH, OTHER_PLAYER_POINTS_CARDS_RECT_HEIGHT)
    pygame.draw.rect(screen, color, otherPlayerPointsCardsRect, 1)

def drawPointsCards(game, screen):

    # !! CURR PLAYER !!

    # Draw rectangle outline for curr player point cards area
    if game.promptCurrPointsCards:
        drawCurrPointsCardsRect(screen, YELLOW)
    else:
        drawCurrPointsCardsRect(screen, GRAY)

    # Draw the cards from left to right
    x = CURR_PLAYER_POINTS_CARDS_X
    for card in game.currPlayer.pointsCards:
        card.imageObj = screen.blit(card.imageOnBoard, (x, CURR_PLAYER_POINTS_CARDS_Y))
        x += (CARD_ON_BOARD_WIDTH + BUFFER)
    
    # !! OTHER PLAYER !!

    # Draw rectangle outline for other player point cards area
    if game.promptOtherPointsCards:
        drawOtherPointsCardsRect(screen, YELLOW)
    else:
        drawOtherPointsCardsRect(screen, GRAY)

    # Draw point cards from left to right
    x = OTHER_PLAYER_POINTS_CARDS_X
    for card in game.otherPlayer.pointsCards:
        card.imageObj = screen.blit(card.imageOnBoard, (x, OTHER_PLAYER_POINTS_CARDS_Y))
        x += (CARD_ON_BOARD_WIDTH + BUFFER)

def drawCurrPermCardsRect(screen, color):
    currPlayerPermCardsRect = pygame.Rect(CURR_PLAYER_PERM_CARDS_RECT_X, CURR_PLAYER_PERM_CARDS_RECT_Y, 
        CURR_PLAYER_PERM_CARDS_RECT_WIDTH, CURR_PLAYER_PERM_CARDS_RECT_HEIGHT)
    pygame.draw.rect(screen, color, currPlayerPermCardsRect, 1)

def drawOtherPermCardsRect(screen, color):
    otherPlayerPermCardsRect = pygame.Rect(OTHER_PLAYER_PERM_CARDS_RECT_X, OTHER_PLAYER_PERM_CARDS_RECT_Y, 
        OTHER_PLAYER_PERM_CARDS_RECT_WIDTH, OTHER_PLAYER_PERM_CARDS_RECT_HEIGHT)
    pygame.draw.rect(screen, color, otherPlayerPermCardsRect, 1)

def drawPermCards(game, screen):

    # !! CURR PLAYER !!

    # Draw outline of area for curr player's perm cards
    if game.promptCurrPermCards:
        drawCurrPermCardsRect(screen, YELLOW)
    else:
        drawCurrPermCardsRect(screen, GRAY)

    # Draw each of the current player's perm cards (2 rows of 3)
    x = CURR_PLAYER_PERM_CARDS_X
    y = CURR_PLAYER_PERM_CARDS_Y
    cardCount = 0 # Track how many cards have been drawn, used to create new row
    for card in game.currPlayer.permCards:
        cardCount += 1
        card.imageObj = screen.blit(card.imageOnBoard, (x, y))
        x += (CARD_ON_BOARD_WIDTH + BUFFER)

        # Create new row
        if cardCount == 3:
            x = CURR_PLAYER_PERM_CARDS_X
            y += (CARD_ON_BOARD_HEIGHT + BUFFER)
    
    # !! OTHER PLAYER !!

    # Draw outline of area for the other player's perm cards (2 rows of 3)
    if game.promptOtherPermCards:
        drawOtherPermCardsRect(screen, YELLOW)
    else:
        drawOtherPermCardsRect(screen, GRAY)

    x = OTHER_PLAYER_PERM_CARDS_X
    y = OTHER_PLAYER_PERM_CARDS_Y
    cardCount = 0 # Track how many cards have been drawn, used to create new row
    for card in game.otherPlayer.permCards:
        cardCount += 1
        card.imageObj = screen.blit(card.imageOnBoard, (x, y))
        x += (CARD_ON_BOARD_WIDTH + BUFFER)

        if cardCount == 3:
            x = OTHER_PLAYER_PERM_CARDS_X
            y -= (CARD_ON_BOARD_HEIGHT + BUFFER)

def drawJacks(game, screen):

    # Draw jacks that are on currPLayer's point cards
    for card in game.currPlayer.jacks.keys():
        y = CURR_PLAYER_JACKS_Y
        for jack in game.currPlayer.jacks[card]:
            jack.imageObj = screen.blit(jack.imageOnBoard, (card.imageObj.x, y))
            y += (CARD_ON_BOARD_HEIGHT * .3)
        
    # Draw jacks on other player's point cards
    for card in game.otherPlayer.jacks.keys():
        y = OTHER_PLAYER_JACKS_Y
        for jack in game.otherPlayer.jacks[card]:
            jack.imageObj = screen.blit(jack.imageOnBoard, (card.imageObj.x, y))
            y -= (CARD_ON_BOARD_HEIGHT * .3)

def drawWinner(game, screen):
    winnerText = ALERT_FONT.render("YOU WON!!!!", True, BRIGHT_GREEN)
    winnerTextRect = winnerText.get_rect()
    winnerTextRect.center = (ALERT_X, ALERT_Y)
    pygame.draw.rect(screen, BLACK, winnerTextRect)
    screen.blit(winnerText, winnerTextRect)

def drawLoser(game, screen):
    loserText = ALERT_FONT.render("YOU LOST!!!!", True, RED)
    loserTextRect = loserText.get_rect()
    loserTextRect.center = (ALERT_X, ALERT_Y)
    pygame.draw.rect(screen, BLACK, loserTextRect)
    screen.blit(loserText, loserTextRect)

def drawSwitchingTurns(game, screen):
    switchingTurnsText = ALERT_FONT.render("SWITCHING TURNS", True, WHITE)
    switchingTurnsTextRect = switchingTurnsText.get_rect()
    switchingTurnsTextRect.center = (ALERT_X,  ALERT_Y)
    pygame.draw.rect(screen, BLACK, switchingTurnsTextRect)
    screen.blit(switchingTurnsText, switchingTurnsTextRect)

def drawBoardIndicators(screen):
    """
    Adds the words 'permanent' and 'points' to game board
    to indicate what is being played where
    """
    # Draw permanent effect indicator
    permText = INDICATOR_FONT.render("PERMANENT", True, WHITE)
    permTextRect = permText.get_rect()
    permTextRect.center = (PERM_INDICATOR_X,  PERM_INDICATOR_Y)
    screen.blit(permText, permTextRect)

    # Draw points indicator
    pointsText = INDICATOR_FONT.render("POINTS", True, WHITE)
    pointsTextRect = pointsText.get_rect()
    pointsTextRect.center = (POINTS_INDICATOR_X,  POINTS_INDICATOR_Y)
    screen.blit(pointsText, pointsTextRect)

def drawTwoResponsePrompt(game, screen, twoPLayer):
    """
    Draw question and response butons (yes or no), asking if player
    (curr or other) would like to play a two in response
    """

    # SLightly different question depending on which player is being asked
    if game.twoPlayer == game.currPlayer:
        twoQuestionText = QUESTION_FONT.render("Cancel opponents two?", True, WHITE)
    elif game.twoPlayer == game.otherPlayer:
        twoQuestionText = QUESTION_FONT.render("  Ask opponent: Use two?  ", True, WHITE)
    
    twoQuestionTextRect = twoQuestionText.get_rect()
    twoQuestionTextRect.center = (TWO_QUESTION_X, TWO_QUESTION_Y)
    pygame.draw.rect(screen, BLACK, twoQuestionTextRect)
    screen.blit(twoQuestionText, twoQuestionTextRect)

    # Draw response buttons
    yesButtonText = QUESTION_FONT.render("   YES   ", True, WHITE)
    yesButtonTextRect = yesButtonText.get_rect()
    yesButtonTextRect.center = (TWO_YES_X, TWO_YES_Y)
    game.twoYesButton = pygame.draw.rect(screen, BLACK, yesButtonTextRect)
    screen.blit(yesButtonText, yesButtonTextRect)

    noButtonText = QUESTION_FONT.render("   NO   ", True, WHITE)
    noButtonTextRect = noButtonText.get_rect()
    noButtonTextRect.center = (TWO_NO_X, TWO_NO_Y)
    game.twoNoButton = pygame.draw.rect(screen, BLACK, noButtonTextRect)
    screen.blit(noButtonText, noButtonTextRect)

def checkDeckClicked(game, clickX, clickY):
    """
    Returns true if the deck was clicked, otherwise false
    """
    return game.deck.imageObj.collidepoint(clickX, clickY)

def checkCancelButtonClicked(game, clickX, clickY):
    """
    Returns true if the cancel button was clicked, else false
    """
    return (game.cancelButtonObj is not None and 
        game.cancelButtonObj.collidepoint(clickX, clickY))

def checkOtherPointsClicked(game, clickX, clickY):
    """
    If one of the opponent's points cards has been clicked,
    return the card that was clicked, else None
    """
    for card in game.otherPlayer.pointsCards:
        if card.imageObj.collidepoint(clickX, clickY):
            return card
    return None

def checkOtherPermClicked(game, clickX, clickY):
    """
    If one of the opponent's perm cards has been clicked,
    return the card that was clicked, else None
    """
    for card in game.otherPlayer.permCards:
        if card.imageObj.collidepoint(clickX, clickY):
            return card
    return None

def checkOtherJackClicked(game, clickX, clickY):
    """
    If one of the opponent's jack cards has been clicked 
    (all jacks attached to opp points cards are considered theirs),
    return the card that was clicked, else None
    """
    for card in game.otherPlayer.jacks.keys():
        for jack in game.otherPlayer.jacks[card]:
            if jack.imageObj.collidepoint(clickX, clickY):
                return card
    return None

def checkCurrPointsClicked(game, clickX, clickY):
    """
    If one of the current player's points cards has been clicked,
    return the card that was clicked, else None
    """
    for card in game.currPlayer.pointsCards:
        if card.imageObj.collidepoint(clickX, clickY):
            return card
    return None

def checkCurrPermClicked(game, clickX, clickY):
    """
    If one of the current player's perm cards has been clicked,
    return the card that was clicked, else None
    """
    for card in game.currPlayer.permCards:
        if card.imageObj.collidepoint(clickX, clickY):
            return card
    return None

def checkCurrJackClicked(game, clickX, clickY):
    """
    If one of the current player's jack cards has been clicked 
    (all jacks attached to curr points cards are considered theirs),
    return the card that was clicked, else None
    """
    for card in game.currPlayer.jacks.keys():
        for jack in game.currPlayer.jacks[card]:
            if jack.imageObj.collidepoint(clickX, clickY):
                return card
    return None

def checkPermButtonClicked(game, clickX, clickY):
    """
    Returns true if permanent button was clicked, else false
    """
    return (game.permButtonObj is not None and 
        game.permButtonObj.collidepoint(clickX, clickY))

def checkPointsButtonClicked(game, clickX, clickY):
    """
    Returns true if points button was clicked, else false
    """
    return (game.pointsButtonObj is not None and 
        game.pointsButtonObj.collidepoint(clickX, clickY))

def checkOneOffButtonClicked(game, clickX, clickY):
    """
    Returns true if one-off button was clicked, else false
    """
    return (game.oneOffButtonObj is not None and 
        game.oneOffButtonObj.collidepoint(clickX, clickY))

def checkScuttleButtonClicked(game, clickX, clickY):
    """
    Returns true if scuttle button was clicked, else false
    """
    return (game.scuttleButtonObj is not None and 
        game.scuttleButtonObj.collidepoint(clickX, clickY))

def checkCardInHandClicked(game, clickX, clickY):
    """
    Returns the card in current player's hand that was clicked, else None
    """
    for card in reversed(game.currPlayer.hand): # Reversed so checked from top layer down on gui
        if card.imageObj.collidepoint(clickX, clickY):
            return card

def checkCardInDiscardClicked(game, clickX, clickY):
    """
    Returns the card from the discard pile that was clicked, else None
    """

    numCardsInDiscard = game.getNumCardsInDiscard()

    # Establish lasfirst card to check (last to be displayed)
    if game.showMaxDiscard > numCardsInDiscard:
        firstCardIndex = 0
    else:
        firstCardIndex = numCardsInDiscard - game.showMaxDiscard

    # Establish last card to check (first to be displayed)
    lastCardIndex = numCardsInDiscard - game.showMaxDiscard + MAX_DISCARDS

    for index in range(firstCardIndex, lastCardIndex):
        card = game.discardPile[index]
        if card.imageObj.collidepoint(clickX, clickY):
            return card
    return None

def checkDiscardBackButtonClicked(game, clickX, clickY):
    """
    Returns true if back button was clicked, else false
    """
    return (game.discardBackButtonObj is not None and 
        game.discardBackButtonObj.collidepoint(clickX, clickY))

def checkDiscardNextButtonClicked(game, clickX, clickY):
    """
    Returns true if next button was clicked, else false
    """
    return (game.discardNextButtonObj is not None and
        game.discardNextButtonObj.collidepoint(clickX, clickY))

def checkTwoYesButtonClicked(game, clickX, clickY):
    """
    Returns true if two yes button was clicked, else false
    """
    return (game.twoYesButton is not None and
        game.twoYesButton.collidepoint(clickX, clickY))

def checkTwoNoButtonClicked(game, clickX, clickY):
    """
    Returns true if two no button was clicked, else false
    """
    return (game.twoNoButton is not None and
        game.twoNoButton.collidepoint(clickX, clickY))

