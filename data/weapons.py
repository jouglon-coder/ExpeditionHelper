from models import Weapon


weapons = [
    Weapon(
        name=r"Abysseram",
        owner=r"Verso",
        lvl4=r"50% increased damage on Rank D. No damage increase on other ranks.",
        lvl10=r"50% increased Base Attack damage.",
        lvl20=r"On Rank D, recover 20% Health with Base Attack."
    ),
    
    Weapon(
        name=r"Blodam",
        owner=r"Verso",
        lvl4=r"Perfection is now based on current Health. Gain 1 Rank every 20% missing Health.",
        lvl10=r"20% increased Light damage with Skills.",
        lvl20=r"+1 AP on Rank Up.",
    ),
    
    Weapon(
        name=r"Chevalam",
        owner=r"Verso",
        lvl4=r"Start battle at Rank S, but can't be Healed or gain Shields.",
        lvl10=r"20% increased damage for each consecutive turn without taking damage. Can stack up to 5 times.",
        lvl20=r"Apply Rush on Rank S.",
    ),
    
    Weapon(
        name=r"Confuso",
        owner=r"Verso",
        lvl4=r"Light damage can Burn on Critical hits.",
        lvl10=r"Apply 3 Burn instead of Mark.",
        lvl20=r"Increase Burn damage by 50% per Rank, up to 300% on Rank S.",
    ),
    Weapon(
        name=r"Contorso",
        owner=r"Verso",
        lvl4=r"Switch to Rank S on Break. Base Attack can Break.",
        lvl10=r"100% Critical Chance on Rank S.",
        lvl20=r"Triggers a lightning strike on Critical hits.",
    ),
    Weapon(
        name=r"Corpeso",
        owner=r"Verso",
        lvl4=r"Base Attack applies 2 Burn stack per Rank.",
        lvl10=r"+1 AP on Rank Up.",
        lvl20=r"Increase Burn damage by 50% per Rank, up to 300% on Rank S.",
    ),
    Weapon(
        name=r"Cruleram",
        owner=r"Verso",
        lvl4=r"Don't lose Rank when taking damage from Powerless enemies.",
        lvl10=r"+1 Perfection on hitting a Powerless enemy.",
        lvl20=r"Apply Powerless on Counterattack.",
    ),
]
