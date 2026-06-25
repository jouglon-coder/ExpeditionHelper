from manager import Manager
from data.weapons import weapons
from data.pictos import pictos
from data.skills import skills


def weapons_by_effect(manager):
    effect = input("Effect: ").lower()
    owner = input("Owner: ").lower()
    
    result = manager.list_weapons_by_effect(effect, owner)
    print(*result, sep="")


def weapons_by_elem(manager):
    elem = input("Elem: ").lower()
    owner = input("Owner: ").lower()
    
    result = manager.list_weapons_by_elem(elem, owner)
    print(*result, sep="")


def pictos_by_effect(manager):
    effect = input("Effect: ").lower()
    
    result = manager.list_pictos_by_effect(effect)
    print(*result, sep="")


def pictos_by_location(manager):
    location = input("Location: ").lower()
    
    result = manager.list_pictos_by_location(location)
    print(*result, sep="")


def skills_by_effect(manager):
    effect = input("Effect: ").lower()
    owner = input("Owner: ").lower()
    if owner.lower() != "any":
        special = input("Special: ").lower()
    else:
        special = "any"
    
    result = manager.list_skills_by_effect(effect, owner, special)
    print(*result, sep="")


def main():
    manager = Manager()
    manager.weapons.extend(weapons)
    manager.weapons.sort(key=lambda x: x.owner)
    manager.pictos.extend(pictos)
    manager.pictos.sort(key=lambda x: x.name)
    manager.skills.extend(skills)
    manager.skills.sort(key=lambda x: x.owner)

    print("Expedition Helper")
    request = input("List Weapons or Pictos or Skills? ").lower()

    if request == "list weapons":
        print(*manager.weapons, sep="\n")
    elif request == "list pictos":
        print(*manager.pictos, sep="\n")
    elif request == "list skills":
        print(*manager.skills, sep="\n")
    elif request == "weapons":
        request = input("List Weapons by Effect or by Elem? ").lower()
        if request == "effect":
            weapons_by_effect(manager)
        elif request == "elem":
            weapons_by_elem(manager)
        else:
            print("Wrong Request! Bye!")
    elif request == "pictos":
        request = input("List Pictos by Effect or by Location? ").lower()
        if request == "effect":
            pictos_by_effect(manager)
        elif request == "location":
            pictos_by_location(manager)
        else:
            print("Wrong Request! Bye!")
    elif request == "skills":
        request = input("List Skills by Effect? ").lower()
        if request == "effect":
            skills_by_effect(manager)
        else:
            print("Wrong Request! Bye!")
    else:
        print("Wrong Request! Bye!")


if __name__ == "__main__":
    main()
