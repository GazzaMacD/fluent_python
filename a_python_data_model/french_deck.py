import collections
from random import choice, sample

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list(
        "JQKA"
    )  # note concat of lists and list comprehensions
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

# due to the __len__ method, len(works)
print(f"The deck length is {len(deck)}")

# Reading cards is easy due to the __getitem__ method
print(f"The first card in the deck is {deck[0]}")

# Get a random card using the choice function from random which
# Gets a random item from a sequence
print(f"A random card from the deck --> {choice(deck)}")

# Our deck is also iterable
# Print whole deck
for card in deck:
    print(f"{card.rank} of {card.suit}")

# and also supports slicing

# randomise a sequence with random.sample
shuffled_one = sample(list(deck), len(deck))
# select the top 4 from the deck and deal to the user
player_one_first = shuffled_one[0:5]
print("\nFirst hand of user")
for card in player_one_first:
    print(f"{card.rank} of {card.suit}")

print(list(deck))

## NOte, in general special methods are meant to be called by the
# python interpreter not by you.
