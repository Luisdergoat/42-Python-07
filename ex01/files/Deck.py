"""
Docstring for ex01.files.Deck
"""

from ex0.cards import Card
import random


class Node:
    def __init__(self, counter, card: Card):
        self.card = card
        self.card_amount = 0
        self.card_in_deck = True
        self.card_place_on_stack = counter
        self.next = None


class Counter:
    count = 0

    @staticmethod
    def increment():
        Counter.count += 1
        return Counter.count


class CardDeck():
    def __init__(self):
        self.card_top = None
        pass

    def add_card(self, card:  Card):
        place_in_deck = Counter.count
        if card is None:
            return ("No Card was added?")
        if isinstance(card, Card):
            return ("Invalid Card!!")

        new_node = Node(card)
        if self.card_top is None:
            self.card_top = new_node
        else:
            current = self.card_top
            while current.next is not None:
                current = current.next
            current.next = new_node
            current.card_place_on_stack = place_in_deck
            current.card_amount += 1
        print(f"The card: {card} was added to the Deck")

    def remove_card(self, card:  Card):
        if card is None:
            return ("No card was removed")
        if isinstance(card, Card):
            return ("Invalid Card")
        current = self.card_top

        while current is not None:
            if current.card == card:
                current.card_place_on_stack = -1
                current.card_in_deck = False
            current = current.next
        current = self.card_top
        while current is not None:
            current.card_place_on_stack -= 1
            current = current.next

        print(f"{card} got removed from the deck")

    def shuffel(self):
        current = self.card_top
        if current is None:
            return ("No Card in deck")
        elif current.card_amount == 1:
            return ("It's just one Card in deck")

        while current is not None:
            number = list(range(1, current.card_amount))

            random.shuffle(number)
            current.card_place_on_stack = number.pop()
            current = current.next

    def draw_card(self):
        print("First card on stack will get drawn")
        current = self.card_top

        if current is None:
            return ("The stack is empty")

        while current is not None:
            if current.card_place_on_stack == 1:
                return (f"{current.card} was drawen")
            current = current.next
        current.card_amount -= 1

        current = self.card_top
        while current is not None:
            current.card_place_on_stack -= 1
            current = current.next

    def get_deck_stats(self):
        #  die Status sachen muessen noch geschrieben werden sowie ein main...
        #  da muss so rein welche Carten typ es ist...
        pass
