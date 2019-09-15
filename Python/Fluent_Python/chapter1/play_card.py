"""
Description:
Author:qxy
Date: 2019-06-22 09:30
File: play_card 
"""

import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [i for i in range(2, 11)] + list('JQKA')
    suits = 'spades diomands clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card(7, 'diomands')
deck = FrenchDeck()

# print(beer_card)
#
# print(len(deck))
#
# print(deck[0])
#
# import random
#
# print(random.choice(deck))

# print(deck)

# for i in deck:
#     print(i)
print(beer_card in deck)

suit_values = dict(spades=3, hearts=2, diomands=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value)
    # print(rank_value)
    # print(len(suit_values))
    # print(suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)