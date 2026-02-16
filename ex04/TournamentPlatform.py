"""
Docstring for ex04.TournamentPlatform
"""

from typing import Dict, Any, List
from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        name_parts = card.name.lower().split()
        card_id = f"{name_parts[-1]}_001"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner_id = card1_id
        loser_id = card2_id

        card1.update_wins(1)
        card2.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": card1.rating,
            "loser_rating": card2.rating
        }

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda x: x[1].rating,
            reverse=True
        )
        return [
            {
                "name": card.name,
                "rating": card.rating,
                "wins": card.wins,
                "losses": card.losses
            }
            for card_id, card in sorted_cards
        ]

    def generate_tournament_report(self) -> Dict[str, Any]:
        total_cards = len(self.cards)
        avg_rating = sum(card.rating for card in self.cards.values()) // total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
