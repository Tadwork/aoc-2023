import pytest

from day7 import ( Hand, compute_winnings)
class TestHand:
    def test_score(self):
        hand = Hand('398KA',100)
        assert hand.score == 10309081314
        # KK677 and KTJJT are both two pair. 
        # Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), 
        # so KTJJT gets rank 2 and KK677 gets rank 3.
        assert Hand('KK677',100).score > Hand('KTJJT',100).score
        # T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
        assert Hand('T55J5',100).score < Hand('QQQJA',100).score
    
def test_compute_winnings():
    hands = [
        Hand('32T3K',765),
        Hand('T55J5',684),
        Hand('KK677',28),
        Hand('KTJJT',220),
        Hand('QQQJA',483),
    ]
    assert compute_winnings(hands) == 6440
    
def test_compute__joker_winnings():
    hands = [
        Hand('32T3K',765),
        Hand('T55J5',684),
        Hand('KK677',28),
        Hand('KTJJT',220),
        Hand('QQQJA',483),
    ]
    assert compute_winnings(hands,joker_rules=True) == 5905
    