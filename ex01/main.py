"""
Docstring for ex01.main
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import files  # type: ignore


def main():
    print("Building deck with different card types...")
    deck = files.CardDeck()
    card1 = files.SpellCard("Lightning Bolt", 3, "common")
    card1.init_spell_effect("damage")
    card2 = files.ArtifactCard("Mana Crystal", 2, "rare")
    card2.init_durability_effect(5, "Permanent: +1 mana per turn")
    card3 = files.CreatureCard("Fire Dragon", 5, "legendary")
    card3.init_power_toughness(5, 5)

    deck.add_card(card1)
    deck.add_card(card2)
    deck.add_card(card3)

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("Drawing and playing cards:")

    while True:
        drawn = deck.draw_card()
        if drawn is None:
            break
        card_type = getattr(drawn, "type", "").capitalize()
        print(f"Drew: {drawn.name} ({card_type})")

        if card_type.lower() == "spell":
            effect = "Deal 3 damage to target"
        elif card_type.lower() == "artifact":
            effect = "Permanent: +1 mana per turn"
        else:
            effect = "Creature summoned to battlefield"

        print("Play result:", {
            "card_played": drawn.name,
            "mana_used": drawn.cost,
            "effect": effect
        })


if __name__ == "__main__":
    main()
