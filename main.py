from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    owner: str
    lvl4: str
    lvl10: str
    lvl20: str

    def __repr__(self):
        return f"{self.name}"


@dataclass
class Pictos:
    name: str
    description: str

    def __repr__(self):
        return f"{self.name}"


class Manager:
    weapons: list[Weapon] = []
    pictos: list[Pictos] = []

    def add_weapon(self, name, owner, lvl4, lvl10, lvl20):
        self.weapons.append(Weapon(name, owner, lvl4, lvl10, lvl20))

    def add_pictos(self, name, description):
        self.pictos.append(Pictos(name, description))

    def list_weapons_by_effect(self, effect: str):
        print(f"Weapons by {effect}: ", end="")
        result = []
        for weapon in self.weapons:
            fields = [weapon.lvl4, weapon.lvl10, weapon.lvl20]
            if any(effect.lower() in field.lower() for field in fields):
                result.append(weapon)
        return result

    def list_pictos_by_effect(self, effect: str):
        print(f"Pictos by {effect}: ", end="")
        result = []
        for pictos in self.pictos:
            if effect.lower() in pictos.description.lower():
                result.append(pictos)
        return result


manager = Manager()

manager.add_weapon(
    name=r"Abysseram",
    owner=r"Verso",
    lvl4=r"50% increased damage on Rank D. No damage increase on other ranks.",
    lvl10=r"50% increased Base Attack damage.",
    lvl20=r"On Rank D, recover 20% Health with Base Attack."
)

manager.add_weapon(
    name=r"Blodam",
    owner=r"Verso",
    lvl4=r"Perfection is now based on current Health. Gain 1 Rank every 20% missing Health.",
    lvl10=r"20% increased Light damage with Skills.",
    lvl20=r"+1 AP on Rank Up.",
)

manager.add_weapon(
    name=r"Chevalam",
    owner=r"Verso",
    lvl4=r"Start battle at Rank S, but can't be Healed or gain Shields.",
    lvl10=r"20% increased damage for each consecutive turn without taking damage. Can stack up to 5 times.",
    lvl20=r"Apply Rush on Rank S.",
)

manager.add_weapon(
    name=r"Confuso",
    owner=r"Verso",
    lvl4=r"Light damage can Burn on Critical hits.",
    lvl10=r"Apply 3 Burn instead of Mark.",
    lvl20=r"Increase Burn damage by 50% per Rank, up to 300% on Rank S.",
)
manager.add_weapon(
    name=r"Contorso",
    owner=r"Verso",
    lvl4=r"Switch to Rank S on Break. Base Attack can Break.",
    lvl10=r"100% Critical Chance on Rank S.",
    lvl20=r"Triggers a lightning strike on Critical hits.",
)
manager.add_weapon(
    name=r"Corpeso",
    owner=r"Verso",
    lvl4=r"Base Attack applies 2 Burn stack per Rank.",
    lvl10=r"+1 AP on Rank Up.",
    lvl20=r"Increase Burn damage by 50% per Rank, up to 300% on Rank S.",
)
manager.add_weapon(
    name=r"Cruleram",
    owner=r"Verso",
    lvl4=r"Don't lose Rank when taking damage from Powerless enemies.",
    lvl10=r"+1 Perfection on hitting a Powerless enemy.",
    lvl20=r"Apply Powerless on Counterattack.",
)

manager.add_pictos(
    name=r"Accelerating Heal",
    description=r"Healing an ally also applies Rush for 1 turn.",
)

manager.add_pictos(
    name=r"Accelerating Last Stand",
    description=r"Gain Rush if fighting alone.",
)

manager.add_pictos(
    name=r"Accelerating Shots",
    description=r"20% chance to gain Rush on Free Aim shot.",
)

print(*manager.list_weapons_by_effect("Base Attack"), sep=", ")
print(*manager.list_weapons_by_effect("Shield"), sep=", ")

print(*manager.list_pictos_by_effect("Rush"), sep=", ")
print(*manager.list_pictos_by_effect("Free Aim Shot"), sep=", ")
