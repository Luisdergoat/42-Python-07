"""
Docstring for ex01.files.SpellCard
"""

from ex0.cards.Card import Card
from ex0.cards.CreatureCard import CreatureCard


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.type = "Spell"
        self.effect = "none"
        self.on_table = False
        self.available_one_time = True

    def init_spell_effect(self, effect: str):
        if effect.lower() == "heal":
            self.effect = effect
        elif effect.lower() == "damage":
            self.effect = effect
        elif effect.lower() == "buff":
            self.effect = effect
        elif effect.lower() == "debuff":
            self.effect = effect
        else:
            print("Invalid effect type. Setting effect to 'none'.")
            self.effect = "none"

    def play(self, mana, game_state):

        if self.available_one_time is False:
            return ("This spell has already been "
                    "used and cannot be played again.")

        if self.is_playable(mana) is False:
            return "Not enough mana to play this card."

        if not game_state:
            game_state = {"Round 1: no actions taken yet."}
            return game_state

        for state in game_state:
            if state.lower().startswith("round"):

                print("Playable: True")
                self.on_table = True
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
        self.on_table = True
        game_state.add(
            f"Round {new_round}: {self.name} played, "
            f"mana used: {self.cost}."
            f"effect: {self.effect}."
            )
        return game_state

    def cast_on_target(self, target):
        if not self.on_table:
            return "Spell must be played before casting on a target."
        if isinstance(target, CreatureCard):
            if self.effect == "heal":
                target.health += 5
                self.available_one_time = False
                return f"{target.name} healed by 5 points."
            elif self.effect == "damage":
                target.health -= 5
                self.available_one_time = False
                return f"{target.name} took 5 damage."
            elif self.effect == "buff":
                target.attack += 3
                target.effect = "buff"
                self.available_one_time = False
                return f"{target.name}'s attack increased by 3."
            elif self.effect == "debuff":
                target.attack -= 3
                target.effect = "debuff"
                self.available_one_time = False
                return f"{target.name}'s attack decreased by 3."
            else:
                return "This spell has no effect."

    def resolve_effect(self, target: str):
        if isinstance(target, CreatureCard):
            if target.effect == "buff":
                target.attack -= 3
            if target.effect == "debuff":
                target.attack += 3
