# Host of functions to get what cards can be clicked based on the given card


class cardFinder:
    def __init__(self, board):
        print("object for finding various cards, etc.")
        self.board = board

    def getCard(self):
        # Look through the board
        # Find the two places that the board exists.
        # Return those two places so that they can be highlighted?
        return

    def getJacks(self):
        return


class gameFunctions:
    def __init__(self, db):
        self.db = db

    def startNewGame(self, player):
        # Function for setting up a new game. Should return game ID
        return

    def openExistingGame(self, player, gameId):
        # function for setting up an existing game
        return

    def placePiece(self, player, gameId):
        # function for playing a card
        return

    def drawCard(self, player):
        # function for drawing a new card
        # Draw card from the api
        # Make sure it's not joker, discard if it is
        # Add card to the player's hand
        return

    def discardCard(self, player, gameId, cardInfo):
        # function for discarding a card after play
        return

    def checkForWin(self, gameId):
        # function for checking if anyone has won
        return

    def getHand(self, player, gameId):
        # function for getting the info on a player's hand.
        return
