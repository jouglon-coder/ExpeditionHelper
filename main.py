from manager import Manager
from data.weapons import weapons
from data.pictos import pictos


manager = Manager()
manager.weapons.extend(weapons)
manager.pictos.extend(pictos)

effect = input("Effect: ")
print("------")

result = manager.list_weapons_by_effect(effect)

for weapon in result:
    print(f"Name:\t{weapon.name}")
    print(f"Elem:\t{weapon.elem}")
    print(f"Owner:\t{weapon.owner}")
    print(f"Lvl 4:\t{weapon.lvl4}")
    print(f"Lvl 10:\t{weapon.lvl10}")
    print(f"Lvl 20:\t{weapon.lvl20}")
    print("------")

