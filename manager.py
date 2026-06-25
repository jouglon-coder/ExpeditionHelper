from models import Weapon, Pictos, Skill


class Manager:
    weapons: list[Weapon] = []
    pictos: list[Pictos] = []
    skills: list[Skill] = []

    def list_weapons_by_effect(self, effect: str, owner: str):
        result = []
        for weapon in self.weapons:
            fields = [weapon.lvl4, weapon.lvl10, weapon.lvl20]
            if any(effect in field.lower() for field in fields) and (weapon.owner.lower() == owner or owner == "any"):
                result.append(weapon)
        return result

    def list_weapons_by_elem(self, elem: str, owner: str):
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

    def list_skills_by_effect(self, effect: str, owner:str, special: str):
        users = ["lune", "maelle", "monoco", "sceil", "verso"]
        result = []
        for skill in self.skills:
            if effect in skill.description.lower():
                if owner == "any" and special == "any":
                    result.append(skill)
                elif owner in users and special == "any" and owner == skill.owner.lower():
                    result.append(skill)
                elif owner in users and special != "any" and owner == skill.owner.lower() and special in skill.special.lower():
                    result.append(skill)
        return result
