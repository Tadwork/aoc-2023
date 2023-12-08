from collections import Counter
from operator import attrgetter
CARD_SCORE = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10, # Ten
    'J': 11, # Jack
    'Q': 12, # Queen
    'K': 13, # King
    'A': 14, # Ace
}

JOKER_CARD_SCORE = CARD_SCORE.copy()
JOKER_CARD_SCORE['J'] = 1


class Hand:
    cards:str
    joker_rep:str
    def __init__(self, cards, bet) -> None:
        self.cards = cards
        self.bet = bet
        most_common = Counter(cards).most_common(2)
        top_card = most_common[0][0]
        if top_card == 'J' and self.compute_hand_type() != 7:
            top_card = most_common[1][0]
        self.joker_rep = self.cards.replace('J',top_card)
    
    def compute_hand_type(self, joker_rules=False):
        if joker_rules:
            cards = self.joker_rep
        else:
            cards = self.cards
        distinct_cards = len(set(cards))
        most_common_card = Counter(cards).most_common(2)[0]
        if distinct_cards == 1: # is_five_of_a_kind
            return 7
        elif distinct_cards == 2 and most_common_card[1] == 4: # is_four_of_a_kind
            return 6
        elif distinct_cards == 2 and most_common_card[1] == 3: # is_full_house
            return 5
        elif distinct_cards == 3 and most_common_card[1] == 3: # is_three_of_a_kind
            return 4
        elif distinct_cards == 3 and most_common_card[1] == 2: # is_two_pair
            return 3
        elif distinct_cards == 4 and most_common_card[1] == 2: # is_one_pair
            return 2
        else:
            return 1
        
    @property
    def score(self):
        hand_type = self.compute_hand_type()
        score = hand_type * 10_000_000_000
        for i,card in enumerate(self.cards):
            place = (4-i)*2
            score += (CARD_SCORE[card] * 10**place)
        return score
    
    @property
    def joker_score(self):
        hand_type = self.compute_hand_type(joker_rules=True)
        score = hand_type * 10_000_000_000
        for i,card in enumerate(self.cards):
            place = (4-i)*2
            score += (JOKER_CARD_SCORE[card] * 10**place)
        return score
    
    def __repr__(self) -> str:
        if not self.joker_rep:
            return f'({self.cards}:{self.bet}:{self.score})'
        else:
            return f'({self.joker_rep}:{self.cards}:{self.bet}:{self.joker_score})'

def compute_winnings(hands, joker_rules=False):
    attr = 'score'
    if joker_rules:
        attr = 'joker_score'
    hands.sort(key=attrgetter(attr))
    total = 0
    for i,hand in enumerate(hands):
        total += hand.bet * (i+1)
    return total

if __name__ == '__main__':
    with open('7/input.txt') as f:
        text = f.read()
        lines = text.split('\n')
        hands = []
        for line in lines:
            if not line:
                continue
            cards,bet = line.split()
            hands.append(Hand(cards,int(bet)))
        print(compute_winnings(hands))
        print(compute_winnings(hands, joker_rules=True))
        