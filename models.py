from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    owner: str
    elem: str
    lvl4: str
    lvl10: str
    lvl20: str

    def __str__(self):
        text = f"""-------
Name : {self.name}
Elem : {self.elem}
Owner: {self.owner}
lvl4 : {self.lvl4}
lvl10: {self.lvl10}
lvl20: {self.lvl20}
"""
        return text


@dataclass
class Pictos:
    name: str
    description: str
    cost: int
    location: dict

    def __str__(self):
        text = f"""-------
Name: {self.name}
Desc: {self.description}
Cost: {self.cost}
"""
        return text
