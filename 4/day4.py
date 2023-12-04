
def score_from_diff(score):
    if score == 1:
        return 1
    elif score >= 2:
        return 2 ** (score-1)
    else:
        return 0
    
def parse_card_input(card):
    name, puzzle = card.split(':')
    winning, yours = puzzle.split('|')
    winning_list, yours_list = winning.strip().split(), yours.strip().split()
    diff = len(winning_list) + len(yours_list) - len(set(winning_list + yours_list))
    return winning_list, yours_list, diff
    
def process_cards(cards):
    cards = [parse_card_input(card) for card in cards.splitlines() if card.strip()]
    return sum([ score_from_diff(diff) for win, yours, diff in cards])

if __name__ == '__main__':
    with open('4/puzzles.txt',mode='r', encoding='utf-8') as f:
        cards = f.read()
    print(process_cards(cards))