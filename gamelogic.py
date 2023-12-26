import requests

# Host of functions to get what cards can be clicked based on the given card


class cardFinder:
    def __init__(self, board):
        print("object for finding various cards, etc.")
        self.board = board

    def getCard(self, card):
        # Look through the board
        # Find the two places that the board exists.
        # Return those two places so that they can be highlighted?
        boardArray = self.board.board
        twoCards = []
        for row in boardArray:
            for column in row:
                print(column)
                if column == card:
                    twoCards.append(column)

        return

    def getJacks(self):
        return


class gameFunctions:
    def __init__(self):
        self.api = "https://deckofcardsapi.com/api/deck/"
        self.getNewDeck()

    def getNewDeck(self):
        params = "?deck_count=2&jokers_enabled=false"
        url = f"{self.api}new/{params}"
        self.deck = requests.get(url)
        self.deck = self.deck.json()
        self.deck_id = self.deck["deck_id"]

    def startNewGame(self, playerDb):
        # Function for setting up a new game. Should return game ID and set self.db to a new entry in Game table
        return

    def openExistingGame(self, playerDb, gameId):
        # function for setting up an existing game
        return

    def placePiece(self, player, location):
        # function for playing a card
        return

    def drawCard(self, playerId):
        # function for drawing a new card
        url = f"{self.api}{self.deck_id}/draw/?count=1"
        card = requests.get(url)
        card = card.json()
        card = card.cards[0]
        cardCode = card["code"]
        image = card["image"]

        newUrl = f"{self.api}{self.deck_id}/pile/{playerId}/add/?cards={cardCode}"
        requests.get(newUrl)
        return {cardCode, image}

    def discardCard(self, playerId, cardCode):
        # function for discarding a card after play
        url = f"{self.api}{self.deck_id}/pile/{playerId}/draw/?cards={cardCode}"
        url2 = f"{self.api}{self.deck_id}/pile/discard/add/?cards={cardCode}"
        requests.post(url)
        requests.post(url2)
        return

    def checkForWin(self):
        # function for checking if anyone has won
        return

    def getHand(self, playerId):
        url = f"{self.api}{self.deck_id}/pile/{playerId}/list"
        hand = requests.get(url).json()
        hand = hand["piles"][playerId]["cards"]
        handCards = []
        for card in hand:
            handCards.append([card["code"], card["image"]])
        return handCards
