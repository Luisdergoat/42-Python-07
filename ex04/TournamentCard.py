"""
Docstring for ex04.TournamentCard
"""

from typing import Dict, Any
from .Rankable import Rankable

try:
    from ex0.Card import Card
    from ex02.Combatable import Combatable
except ImportError:
    from ex0.cards import Card
    from ex02 import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, base_rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.base_rating = base_rating
        self.rating = base_rating
        self.wins = 0
        self.losses = 0
        self.attack_power = 5

    def play(self, game_state: dict) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "status": "tournament_ready",
            "game_state": game_state
        }

    def attack(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "tournament"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": True
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack_power": self.attack_power,
            "wins": self.wins,
            "losses": self.losses
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "interfaces": ["Card", "Combatable", "Rankable"]
        }
