"""
Docstring for ex01.files.ArtifactCard
"""

from ex0.cards import Card


class ArtifactCard(Card):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.type = "artifact"
        self.durability = 0
        self.effect = 0

    def init_durability_effect(self, durability: int, effect: str) -> None:
        self.durability = durability

        self.effect = effect
