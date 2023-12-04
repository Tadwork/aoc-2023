from collections import defaultdict

def score_from_diff(score):
    if score == 1:
        return 1
    elif score >= 2:
        return 2 ** (score-1)
    else:
        return 0
    
def parse_card_input(card):
    name, puzzle = card.split(':')
    card_id = int(name.split()[1])
    winning, yours = puzzle.split('|')
    winning_list, yours_list = winning.strip().split(), yours.strip().split()
    diff = len(winning_list) + len(yours_list) - len(set(winning_list + yours_list))
    return card_id, diff

def process_cards_and_return_score(cards):
    cards = [parse_card_input(card) for card in cards.splitlines() if card.strip()]
    return sum([ score_from_diff(diff) for card_id, diff in cards])

## Part 2

def process_cards_and_return_count(cards):
    cards = [parse_card_input(card) for card in cards.splitlines() if card.strip()]
    card_counts = defaultdict(int)
    for card_id, diff in cards:
        card_counts[card_id] += 1
        for i in range(1,diff+1):
            card_counts[card_id + i] += card_counts[card_id]
        # print(card_id, diff,card_counts)
    return sum(card_counts.values())
        
            
if __name__ == '__main__':
    with open('4/puzzles.txt',mode='r', encoding='utf-8') as f:
        cards = f.read()
    print(process_cards_and_return_score(cards))
    print(process_cards_and_return_count(cards))