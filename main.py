from manager import Manager
from data.weapons import weapons
from data.pictos import pictos


manager = Manager()
manager.weapons.extend(weapons)
manager.pictos.extend(pictos)

print(*manager.list_weapons_by_effect("Base Attack"), sep=", ")
print(*manager.list_weapons_by_effect("Free Aim Shot"), sep=", ")
print(*manager.list_weapons_by_effect("Defence"), sep=", ")
print(*manager.list_weapons_by_effect("Rush"), sep=", ")
print(*manager.list_weapons_by_effect("Speed"), sep=", ")
print(*manager.list_weapons_by_effect("Shield"), sep=", ")

# print(*manager.list_pictos_by_effect("Defence"), sep=", ")
# print(*manager.list_pictos_by_effect("Rush"), sep=", ")
# print(*manager.list_pictos_by_effect("Free Aim Shot"), sep=", ")
