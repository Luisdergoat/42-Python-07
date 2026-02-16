"""
Docstring for ex03.GameEngine
"""

from typing import Dict, Any
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand = []
        self.battlefield = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        if not self.hand:
            self.hand = [
                self.factory.create_creature(),
                self.factory.create_creature(),
                self.factory.create_spell()
            ]
            self.cards_created = len(self.hand)

        result = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": result
        }

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name() if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
