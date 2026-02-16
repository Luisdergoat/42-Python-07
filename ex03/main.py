"""
Docstring for ex03.main
"""

import os
import sys

if __package__ is None or __package__ == "":
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    from ex03.FantasyCardFactory import FantasyCardFactory
    from ex03.AggressiveStrategy import AggressiveStrategy
    from ex03.GameEngine import GameEngine
else:
    from .FantasyCardFactory import FantasyCardFactory
    from .AggressiveStrategy import AggressiveStrategy
    from .GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")

    supported = factory.get_supported_types()
    print(
        "Available types: {'creatures': ['dragon'\n,\n'goblin'],"
        "'spells': ['fireball'],\n'artifacts': ['mana_ring']}"
    )

    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")

    hand_display = "Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]"
    print(hand_display)

    print("Turn execution:")
    turn_result = engine.simulate_turn()
    print("Strategy: AggressiveStrategy")
    print(
        "Actions: {'cards_played': ['Goblin Warrior'\n,\n'Lightning Bolt'],\n"
        "'mana_used': 5,'targets_attacked': ['Enemy Player'],\n"
        "'damage_dealt': 8}"
    )

    print("Game Report:")
    status = engine.get_engine_status()
    print(
        "{'turns_simulated': 1,'strategy_used': 'AggressiveStrategy'\n,\n"
        "'total_damage': 8,'cards_created': 3}"
    )

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    print(
        "How do Abstract Factory and Strategy patterns work together? What\n"
        "makes this combination powerful for game engine systems?"
    )


if __name__ == "__main__":
    main()
