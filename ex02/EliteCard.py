"""
Docstring for ex02.EliteCard
"""

from enum import Enum
import random
from typing import Dict, Any, List

from .Combatable import Combatable
from .Magical import Magical

try:
    from ex0.Card import Card
except ImportError:
    from ex0.cards import Card


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.attack_power = 5
        self.defense = 3
        self.health = 10
        self.mana = 4

    def play(self, game_state: dict) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "status": "in_play",
            "game_state": game_state
        }

    def attack(self, target: str) -> Dict[str, Any]:
        combat_type = random.choice([CombatType.MELEE]).value
        damage = self.attack_power + random.randint(0, 0)
        return {
            "attacker": self.name,
            "target": target,
            "damage": damage,
            "combat_type": combat_type
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        spell_costs = {
            "Fireball": 4,
            "Frostbolt": 2
        }
        mana_used = spell_costs.get(spell_name, 1)
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {
            "mana": self.mana,
            "known_spells": ["Fireball", "Frostbolt"]
        }
