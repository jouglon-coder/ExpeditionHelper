from manager import Manager
from data.weapons import weapons
from data.pictos import pictos


def weapons_by_effect(manager):
    effect = input("Effect: ").lower()
    owner = input("Owner: ").lower()
    print("------")
    
    result = manager.list_weapons_by_effect(effect, owner)
    
    for weapon in result:
        print(f"Name:\t{weapon.name}")
        print(f"Elem:\t{weapon.elem}")
        print(f"Owner:\t{weapon.owner}")
        print(f"Lvl 4:\t{weapon.lvl4}")
        print(f"Lvl 10:\t{weapon.lvl10}")
        print(f"Lvl 20:\t{weapon.lvl20}")
        print("------")


def weapons_by_elem(manager):
    elem = input("Elem: ").lower()
    owner = input("Owner: ").lower()
    print("------")
    
    result = manager.list_weapons_by_elem(elem, owner)
    
    for weapon in result:
        print(f"Name:\t{weapon.name}")
        print(f"Elem:\t{weapon.elem}")
        print(f"Owner:\t{weapon.owner}")
        print(f"Lvl 4:\t{weapon.lvl4}")
        print(f"Lvl 10:\t{weapon.lvl10}")
        print(f"Lvl 20:\t{weapon.lvl20}")
        print("------")


def pictos_by_effect(manager):
    effect = input("Effect: ").lower()
    print("------")
    
    result = manager.list_pictos_by_effect(effect)
    
    for pictos in result:
        print(f"Name:\t{pictos.name}")
        print(f"Disc:\t{pictos.description}")
        print(f"Cost:\t{pictos.cost}")
        print(f"Loca:\t{pictos.location}")
        print("------")


def pictos_by_location(manager):
    location = input("Location: ").lower()
    print("------")
    
    result = manager.list_pictos_by_location(location)
    
    for pictos in result:
        print(f"Name:\t{pictos.name}")
        print(f"Disc:\t{pictos.description}")
        print(f"Cost:\t{pictos.cost}")
        print(f"Loca:\t{pictos.location}")
        print("------")


def main():
    manager = Manager()
    manager.weapons.extend(weapons)
    manager.pictos.extend(pictos)

    print("Expedition Helper")
    print("List Weapons or Pictos?")
    request = input().lower()

    if request == "weapons":
        print("List Weapons by Effect or by Elem?")
        request = input().lower()
        if request == "effect":
            weapons_by_effect(manager)
        elif request == "elem":
            weapons_by_elem(manager)
        else:
            print("Wrong Request! Bye!")
    elif request == "pictos":
        print("List Pictos by Effect or by Location?")
        request = input().lower()
        if request == "effect":
            pictos_by_effect(manager)
        elif request == "location":
            pictos_by_location(manager)
        else:
            print("Wrong Request! Bye!")
    else:
        print("Wrong Request! Bye!")


if __name__ == "__main__":
    main()

