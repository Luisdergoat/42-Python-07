"""
Docstring for ex0.cards.CreatureCard
"""

from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,):
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        self.attack = 0
        self.health = 0

    def init_power_toughness(self, attack: int, health: int):
        self.attack = attack
        self.health = health

    def play(self, mana, game_state):
        if self.is_playable(mana) is False:
            return "Not enough mana to play this card."

        if not game_state:
            game_state = {"Round 1: no actions taken yet."}
            return game_state

        for state in game_state:
            if state.lower().startswith("round"):

                print("Playable: True")
                game_state = {f"Round 1: {self.name} played, "
                              f"mana used: {self.cost}."
                              f"effect: Creature summoned to the battlefield."}
                return game_state

        highest_round = 0
        for state in game_state:
            round_number = int(state.split(" ")[1])
            if round_number > highest_round:
                highest_round = round_number
        new_round = highest_round + 1
        print("Playable: True")
        game_state.add(
            f"Round {new_round}: {self.name} played, "
            f"mana used: {self.cost}."
            f"effect: Creature summoned to the battlefield."
            )
        return game_state

    def attack_target(self, target):
        if isinstance(target, CreatureCard):
            target.health -= self.attack
            self.health -= target.attack
            return (f"attack result: {self.name} attacked {target.name} - "
                    f"damage dealt: {self.attack} combat_resolved: {True},")
        elif not target:
            return "No target to attack."
        else:
            return "Invalid target."

    def get_card_info(self):
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })
        return info
