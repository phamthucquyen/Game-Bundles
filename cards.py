import random

class Card(object):
    """A card object with a suit, rank, and file name.
    The file name refers to the card's image on disk."""

    RANKS = tuple(range(1,14))
    SUITS = ('Spades','Hearts', 'Diamonds', 'Clubs')
    BACK_NAME = 'DECK/b.gif'

    def __init__(self, rank, suit):
        """Creates a card with the fiven rank and suit."""
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit
        self.fileName = 'DECK/' + str(rank) + suit[0].lower() + '.gif'

    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank,suit))

    def __len__(self):
        return len(self.cards)
    
    def isEmpty(self):
        return len(self.cards) == 0
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)

def testCards():
    card = Card(13, "Hearts")
    print("Pass: Executed as expected with no error:", card)

    try:
        card = Card(13, "Heart")
    except RuntimeError as exc:
        print("Pass: Expected runtime error because used incorrect suit")

if __name__ == "__main__":
    testCards()