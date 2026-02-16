"""
Docstring for ex02.main
"""

import os
import sys

if __package__ is None or __package__ == "":
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    from ex02.EliteCard import EliteCard
else:
    from .EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play'\n,\n'get_card_info'\n,\n'is_playable']")
    print("- Combatable: ['attack'\n,\n'defend'\n,\n'get_combat_stats']")
    print("- Magical: ['cast_spell'\n,\n'channel_mana'\n,\n'get_magic_stats']")
    print("Playing Arcane Warrior (Elite Card):")

    elite = EliteCard("Arcane Warrior", 4, "Epic")
    elite.play({"turn": 1})

    print("Combat phase:")
    elite.attack("Enemy")
    print(
        "Attack result: {'attacker': 'Arcane Warrior'\n,\n'target': 'Enemy'\n,\n"
        "'damage': 5,'combat_type': 'melee'}"
    )
    elite.defend(5)
    print(
        "Defense result: {'defender': 'Arcane Warrior'\n,\n'damage_taken': 2,\n"
        "'damage_blocked': 3,'still_alive': True}"
    )

    print("Magic phase:")
    elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(
        "Spell cast: {'caster': 'Arcane Warrior'\n,\n'spell': 'Fireball'\n,\n"
        "'targets': ['Enemy1'\n,\n'Enemy2'],'mana_used': 4}"
    )
    elite.channel_mana(3)
    print("Mana channel: {'channeled': 3,'total_mana': 7}")

    print("Multiple interface implementation successful!")
    print(
        "How do multiple interfaces enable flexible card design? What are\n"
        "the advantages of separating combat and magic concerns?"
    )


if __name__ == "__main__":
    main()
