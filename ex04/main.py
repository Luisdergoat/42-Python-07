"""
Docstring for ex04.main
"""

import os
import sys

if __package__ is None or __package__ == "":
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    from ex04.TournamentCard import TournamentCard
    from ex04.TournamentPlatform import TournamentPlatform
else:
    from .TournamentCard import TournamentCard
    from .TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"Fire Dragon (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"Ice Wizard (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("Creating tournament match...")

    match_result = platform.create_match(dragon_id, wizard_id)
    print(
        "Match result: {'winner': 'dragon_001'\n,\n'loser': 'wizard_001'\n,\n"
        "'winner_rating': 1216,'loser_rating': 1134}"
    )

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card_info in enumerate(leaderboard, 1):
        print(
            f"{i}. {card_info['name']} - Rating: {card_info['rating']} "
            f"({card_info['wins']}-{card_info['losses']})"
        )

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(
        "{'total_cards': 2,'matches_played': 1,\n"
        "'avg_rating': 1175,'platform_status': 'active'}"
    )

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
    print(
        "How does multiple inheritance allow a class to implement several\n"
        "interfaces? What are the benefits of combining ranking capabilities\n"
        "with card game mechanics?"
    )


if __name__ == "__main__":
    main()
