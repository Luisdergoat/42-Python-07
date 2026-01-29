"""
Docstring for ex0.main
"""

import cards


def main():

    fire_dragon = cards.CreatureCard("Fire Dragon", 5, "Legendary")
    fire_dragon.init_power_toughness(7, 5)
    gamme_state = fire_dragon.get_card_info()
    mana_available = 6

    print("=== DataDeck Card Foundation ===")
    print("\nCreatureCard Info:")
    print(gamme_state)

    print("\nPlaying Fire Dragon with 6 mana available:")
    fire_dragon.is_playable(mana_available)
    mana_available -= fire_dragon.cost
    game_start = {"round 1"}
    game_state = fire_dragon.play(6, game_start)
    print(game_state)
    goblin_warrior = cards.CreatureCard("Goblin Warrior", 2, "Common")
    goblin_warrior.init_power_toughness(3, 2)
    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target(goblin_warrior)
    print(attack_result)
    print("\nTesting insufficient mana (3 available):")
    returns = fire_dragon.play(mana_available, game_state)
    print(returns)
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
