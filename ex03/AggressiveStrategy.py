"""
Docstring for ex03.AggressiveStrategy
"""

from typing import Dict, Any, List
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> Dict[str, Any]:
        cards_played = []
        mana_used = 0
        targets_attacked = ["Enemy Player"]
        damage_dealt = 0

        sorted_hand = sorted(hand, key=lambda card: card.cost)

        available_mana = 10
        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost

                if hasattr(card, "attack"):
                    damage_dealt += card.attack
                elif hasattr(card, "effect") and card.effect == "damage":
                    damage_dealt += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> List[str]:
        return available_targets
