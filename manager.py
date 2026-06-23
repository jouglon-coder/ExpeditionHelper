from models import Weapon, Pictos


class Manager:
    weapons: list[Weapon] = []
    pictos: list[Pictos] = []

    def list_weapons_by_effect(self, effect: str, owner):
        result = []
        for weapon in self.weapons:
            fields = [weapon.lvl4, weapon.lvl10, weapon.lvl20]
            if any(effect in field.lower() for field in fields) and (weapon.owner.lower() == owner or owner == "any"):
                result.append(weapon)
        return result

    def list_weapons_by_elem(self, elem: str, owner):
        result = []
        for weapon in self.weapons:
            if weapon.elem.lower() == elem and (weapon.owner.lower() == owner or owner == "any"):
                result.append(weapon)
        return result

    def list_pictos_by_effect(self, effect: str):
        result = []
        for pictos in self.pictos:
            if effect in pictos.description.lower():
                result.append(pictos)
        return result

    def list_pictos_by_location(self, location: str):
        result = []
        for pictos in self.pictos:
            if any(location in loc.lower() for loc in pictos.location.keys()):
                result.append(pictos)
        return result
