from cards import Deck
from game import Game

class WarGame(Game):
    """Plays the game of war."""

    def __init__(self):
        """Sets up the two players, the war pile, the deck, and the game state."""
        super().__init__()
        self.player1 = Player()
        self.player2 = Player()
        self.warPile = []
        self.gameState = ""
        self.deck = Deck()
        self.deck.shuffle()
        self.deal()

    def __str__(self):
        """Returns the game state."""
        if self.isGameOver():
            return self.winner()
        
        return self.gameState
    
    def deal(self):
        """Deals 26 cards to each player."""
        while not self.deck.isEmpty():
            self.player1.addToUnplayedPile(self.deck.deal())
            self.player2.addToUnplayedPile(self.deck.deal())

    def getInput(self):
        pass

    def step(self, dummyInput):
        """ Makes one move in the games, and returns the two cards played."""

        super().step()

        card1 = self.player1.getCard()
        card2 = self.player2.getCard()
        self.warPile.append(card1)
        self.warPile.append(card2)
        self.gameState = "Player 1: " + str(card1) + "\n" +\
                         "Player 2: " + str(card2)
        if card1.rank == card2.rank:
            self.gameState += "\nCards added to War pile\n"
        elif card1.rank > card2.rank:
            self.transferCardsS(self.player1)
            self.gameState += "\nCards go to Player 1\n"
        else:
            self.transferCards(self.player2)
            self.gameState += "\nCards go to Player 2\n"

        self.gameOver = self.player1.isDone() or self.player2.isDone()
    
    def transferCards(self, player):
        """Transfers cards from the war pile to the player's winnings pile."""
        while len(self.warPile) > 0:
            player.addToWinningsPile(self.warPile.pop())

    def winner(self):
        """Returns None if there is no winner yet. Otherwise,
        returns a string indicating the player who won with each
        player's number of cards, or a tie."""
        if self.player1.isDone() or self.player2.isDone():
            count1 = self.player1.winningsCount()
            count2 = self.player2.winningsCount()
            if count1 > count2:
                return "Player 1 wins, " + str(count1) + " to " +\
                        str(count2) +"!"
            
            elif count2 > count1:
                return "Player 2 wins, " + str(count2) + " to " +\
                        str(count1) +"!"
            else:
                return "The game ends in a tie!\n"
        else:
            return None
        
class Player(object):
    """Represents a War game player."""

    def __init__(self):
        """Sets up the player's unplayed and winnings piles."""
        self.unplayed = []
        self.winning = []

    def __str__(self):
        """Returns a description of the player's winnings pile."""
        winPile = "Winning pile:\n"
        for card in self.winning:
            winPile += str(card) + "\n"
        return winPile
    
    def addToUnplayedPile(self,card):
        """Adds card to the player's unplayed pile."""
        self.unplayed.append(card)

    def addToWinningsPile(self,card):
        """Adds card to the player's winnings pile."""
        self.winning.append(card)

    def getCard(self):
        """Removes and returns a card from the player's unplayed pile."""
        return self.unplayed.pop()
    
    def isDone(self):
        """Returns True if the player's unplayed pile is empty,
        or False otherwise."""
        return len(self.unplayed) == 0
    
    def winningsCount(self):
        """Returns the number of cards in the player's winnings pile."""
        return len(self.winning)
    
if __name__ == "__main__":
    game = WarGame()
    game.main()


