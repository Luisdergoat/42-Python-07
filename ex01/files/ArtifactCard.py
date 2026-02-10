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
        self.active = True
        if isinstance(target, CreatureCard):
            target.effect = self.effect

    def play(self, mana, game_state):
        if self.is_playable(mana) is False:
            return "Not enough mana to play this card."

        if not game_state:
            game_state = {"Round 1: no actions taken yet."}
            return game_state

        for state in game_state:
            if state.lower().startswith("round"):
                print("Playable: True")
                self.active = True
                game_state = {f"Round 1: {self.name} played, "
                              f"mana used: {self.cost}."
                              f"effect: {self.effect}."}
                return game_state

        highest_round = 0
        for state in game_state:
            round_number = int(state.split(" ")[1])
            if round_number > highest_round:
                highest_round = round_number
        new_round = highest_round + 1
        print("Playable: True")
        self.active = True
        game_state.add(
            f"Round {new_round}: {self.name} played, "
            f"mana used: {self.cost}."
            f"effect: {self.effect}."
            )
        return game_state

    def get_status(self):
        print(f"The Artefact is for {self.durability} roundt active")
        print(f"The effect of the artefact is: {self.effect}")
        if self.active is False:
            print("The Artefact is not active")
        else:
            print("Tge Artefact is active")
