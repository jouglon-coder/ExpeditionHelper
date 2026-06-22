from models import Weapon, Pictos


class Manager:
    weapons: list[Weapon] = []
    pictos: list[Pictos] = []

    def list_weapons_by_effect(self, effect: str):
        result = []
        for weapon in self.weapons:
            fields = [weapon.lvl4, weapon.lvl10, weapon.lvl20]
            if any(effect.lower() in field.lower() for field in fields) and effect != effect.upper():
                result.append(weapon)
            elif any(effect in field for field in fields) and effect == effect.upper(): # for AP
                result.append(weapon)
        return result

    def list_pictos_by_effect(self, effect: str):
        print(f"Pictos by {effect}: ", end="")
        result = []
        for pictos in self.pictos:
            if effect.lower() in pictos.description.lower():
                result.append(pictos)
        return result
