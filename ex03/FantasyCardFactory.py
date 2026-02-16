"""
Docstring for ex03.FantasyCardFactory
"""

from typing import Dict, Any, Optional, Union
import random
from .CardFactory import CardFactory

try:
    from ex0.cards.CreatureCard import CreatureCard
    from ex01.files.SpellCard import SpellCard
    from ex01.files.ArtifactCard import ArtifactCard
except ImportError:
    from ex0.cards import CreatureCard
    from ex01.files import SpellCard, ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature_templates = {
            "dragon": {"name": "Fire Dragon", "cost": 5, "attack": 7, "health": 5},
            "goblin": {"name": "Goblin Warrior", "cost": 2, "attack": 3, "health": 2}
        }
        self.spell_templates = {
            "fireball": {"name": "Lightning Bolt", "cost": 3, "effect": "damage"}
        }
        self.artifact_templates = {
            "mana_ring": {"name": "Mana Crystal", "cost": 2, "durability": 5}
        }

    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> CreatureCard:
        template = self.creature_templates["dragon"]
        creature = CreatureCard(
            template["name"],
            template["cost"],
            "legendary"
        )
        creature.init_power_toughness(template["attack"], template["health"])
        return creature

    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> SpellCard:
        template = self.spell_templates["fireball"]
        spell = SpellCard(template["name"], template["cost"], "common")
        spell.init_spell_effect(template["effect"])
        return spell

    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> ArtifactCard:
        template = self.artifact_templates["mana_ring"]
        artifact = ArtifactCard(template["name"], template["cost"], "rare")
        artifact.init_durability_effect(
            template["durability"],
            "Permanent: +1 mana per turn"
        )
        return artifact

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck = []
        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                deck.append(self.create_creature())
            elif card_type == "spell":
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {
            "deck_size": size,
            "cards": deck,
            "theme": "fantasy"
        }

    def get_supported_types(self) -> Dict[str, list]:
        return {
            "creatures": list(self.creature_templates.keys()),
            "spells": list(self.spell_templates.keys()),
            "artifacts": list(self.artifact_templates.keys())
        }
