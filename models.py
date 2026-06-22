from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    owner: str
    elem: str
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
