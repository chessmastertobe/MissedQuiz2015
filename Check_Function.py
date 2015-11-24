
def multiple(n, cards):

    for c in cards:
        if cards.count(c) == n: return c
    return None

def flush(hand):
    # check same suit
    suits = [s for c, s in hand]
    return len(set(suits)) == 1

def straight(cards):
    # check a straight
    return (max(cards ) -min(cards) == 4) and len(set(cards)) == 5

def two_pair(cards):
    # check two pair
    pair = multiple(2, cards)
    lowpair = multiple(2, list(reversed(cards)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def sort(hand):
    # sort hand into ascending order
    cards = ['--23456789TJQKA'.index(c) for c, s in hand]
    cards.sort(reverse = True)
    # special case for ace-low straight
    return [5, 4, 3, 2, 1] if (cards == [14, 5, 4, 3, 2]) else cards

def value(hand):
    # returns a tuple with the hand value and other determining features
    cards = sort(hand)
    if straight(cards) and flush(hand):
        return (8, max(cards))
    elif multiple(4, cards):
        return (7, multiple(4, cards), multiple(1, cards))
    elif multiple(3, cards) and multiple(2, cards):
        return (6, multiple(3, cards), multiple(2, cards))
    elif flush(hand):
        return (5, cards)
    elif straight(cards):
        return (4, max(cards))
    elif multiple(3, cards):
        return (3, multiple(3, cards), cards)
    elif two_pair(cards):
        return (2, two_pair(cards), cards)
    elif multiple(2, cards):
        return (1, multiple(2, cards), cards)
    else:
        return (0, cards)
