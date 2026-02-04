"""
Docstring for ex01.files.ArtifactCard
"""

from ex0.cards import Card
from ex0.cards import CreatureCard


class ArtifactCard(Card):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.type = "artifact"
        self.durability = 0
        self.effect = 0
        self.active = False

    def init_durability_effect(self, durability: int, effect: str) -> None:
        self.durability = durability

        self.effect = effect

    def activate_ability(self, target):
        if target is None:
            pass
        self.activate_ability = True
        if isinstance(target, CreatureCard):
            target.effect = self.effect

    def get_status(self):
        print(f"The Artefact is for {self.durability} roundt active")
        print(f"The effect of the artefact is: {self.effect}")
        if self.activate_ability is False:
            print("The Artefact is not active")
        else:
            print("Tge Artefact is active")
