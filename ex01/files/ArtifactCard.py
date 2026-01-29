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
        pass  # ich brauch noch sooo viel initialisierung fue die effecte und shit
    # dazu ganz viele sachen noch weiter rein wie play und get status und shit 