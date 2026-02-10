"""
Docstring for ex01.files.Deck
"""

import math
import random
from ex0.cards import Card


class CardDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        if card is None:
            return "No Card was added?"
        if not isinstance(card, Card):
            return "Invalid Card!!"
        self.cards.append(card)

    def remove_card(self, card: Card):
        if card is None:
            return "No card was removed"
        if not isinstance(card, Card):
            return "Invalid Card"
        if card in self.cards:
            self.cards.remove(card)

    def shuffel(self):
        if not self.cards:
            return "No Card in deck"
        if len(self.cards) == 1:
            return "It's just one Card in deck"
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self):
        total_cards = len(self.cards)
        if total_cards == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0
            }

        def _type_of(card: Card) -> str:
            return str(getattr(card, "type", "")).lower()

        creatures = sum(1 for card in self.cards if _type_of(card) == "creature")
        spells = sum(1 for card in self.cards if _type_of(card) == "spell")
        artifacts = sum(1 for card in self.cards if _type_of(card) == "artifact")
        avg_cost = sum(card.cost for card in self.cards) / total_cards
        avg_cost = float(math.ceil(avg_cost))

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": float(f"{avg_cost:.1f}")
        }
