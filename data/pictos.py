from models import Pictos


pictos = [
    Pictos(
        name="Double Third",
        description="Every third hit of a Skill deals double damage",
        cost=10,
        location={
             "Verso's Drafts": "First Expedition Flag",
        },
    ),
    Pictos(
        name="SOS Healing Tint",
        description="Consume a Healing Tint when falling below 50% Health",
        cost=10,
        location={
             "Verso's Drafts": "Franctale enemy around Gingerbread Door",
        },
    ),
    Pictos(
        name="Damage Share",
        description="50% damage taken is redirected to other allies (if possible)",
        cost=30,
        location={
             "Verso's Drafts": "Two Licorne enemies guard the Gingerbread Door",
        },
    ),
    Pictos(
        name="Empowering Jumps",
        description="Counters deal 100% more damage for each successful Jump Counter this turn",
        cost=5,
        location={
             "Verso's Drafts": "The Gestral sitting on the seesaw",
        },
    ),
    Pictos(
        name="Gradient Parry",
        description="+5% of a gradient charge on Parry",
        cost=10,
        location={
             "Verso's Drafts": "Esquie statue near Hopscotch Tile number 5",
        },
    ),
    Pictos(
        name="Slowing Attack",
        description="Base attack applies Slow for 1 turn",
        cost=10,
        location={
             "Verso's Drafts": "On a glowing ledge around Esquie statues",
        },
    ),
    Pictos(
        name="Clea's Death",
        description="On death, allies gain 25% increased damage until they die",
        cost=15,
        location={
             "Endless Tower": "Clea Unleashed",
        },
    ),
    Pictos(
        name="Feint",
        description="Start each turn with 4 Barbapapa stacks. Every 5th hit with a Skill deals 600% more damage",
        cost=15,
        location={
             "Verso's Drafts": "Monsieur Frappe in Candy Land",
        },
    ),
    Pictos(
        name="Gradient Overcharge",
        description="On turn start, consume 3 Gradient Charges (if able) to deal 200% more damage this turn",
        cost=15,
        location={
             "Verso's Drafts": "On a large floating piece of candy near the Candy Land entrance",
        },
    ),
    Pictos(
        name="Longer Break",
        description="Breaks last 1 more turn but the target cannot be Broken twice",
        cost=10,
        location={
             "Verso's Drafts": "The group of Barbasucette and Machinapieds below the first Expedition Flag",
        },
    ),
    Pictos(
        name="Alternating Critical",
        description="On Critical hit, 100% increased damage of the next non-Critical hit",
        cost=10,
        location={
             "Verso's Drafts": "From the Open Playground expedition flag, take the left fork, enter the cave, then follow the right tunnel",
        },
    ),
    Pictos(
        name="Trigger-Happy",
        description="After shooting 10 times in the same turn, gain +2 AP (once). And following Shots this turn deal 200% more damage",
        cost=20,
        location={
             "Verso's Drafts": "Half-Baked Gestral",
        },
    ),
    Pictos(
        name="AP Discount",
        description="Skills cost 1 less AP",
        cost=30,
        location={
             "Verso's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Consuming Attack",
        description="Base attack consumes up to 100 Burns to deal 10% more damage per Burn consumed",
        cost=10,
        location={
             "Verso's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Empowered Healer",
        description="Using a Healing Skill gives 50% more damage for 1 turn",
        cost=10,
        location={
             "Verso's Drafts": "Parkour after Esquie statue near Hopscotch Tile number 5",
        },
    ),
    Pictos(
        name="First Life",
        description="25% increased damage until death. 20% decreased damage on death",
        cost=15,
        location={
             "Endless Tower": "Chromatic Lampmaster",
        },
    ),
    Pictos(
        name="Frenzy",
        description="Each successive Skill hit deals 10% more damage",
        cost=20,
        location={
             "Verso's Drafts": "Near the Licornapieds Station expedition flag",
        },
    ),
    Pictos(
        name="Accelerating Heal",
        description="Healing an ally also applies Rush for 1 turn",
        cost=5,
        location={
             "The Continent": "An island northeast of Stone Wave Cliffs",
        },
    ),
    Pictos(
        name="Accelerating Last Stand",
        description="Gain Rush if fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Bertrand Big Hands",
        },
    ),
    Pictos(
        name="Accelerating Shots",
        description="20% chance to gain Rush on Free Aim Shot",
        cost=3,
        location={
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Accelerating Tint",
        description="Healing Tints also apply Rush",
        cost=5,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Aegis Revival",
        description="+1 Shield on being revived",
        cost=5,
        location={
             "Spring Meadows": "The Paint Spike around Expedition Camp Expedition Flag",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Anti-Blight",
        description="Immune to Blight",
        cost=10,
        location={
             "The Continent": "Chromatic Portier",
             "The Reacher": "Merchant",
        },
    ),
    Pictos(
        name="Anti-Burn",
        description="Immune to Burn",
        cost=15,
        location={
             "Frozen Hearts": "Gargant",
             "Flying Manor": "Gargant",
        },
    ),
    Pictos(
        name="Anti-Charm",
        description="Immune to Charm",
        cost=10,
        location={
             "Sirene": "Tisseur",
        },
    ),
    Pictos(
        name="Anti-Freeze",
        description="Immune to Freeze",
        cost=15,
        location={
             "Frozen Hearts": "Paint Cage",
        },
    ),
    Pictos(
        name="Anti-Stun",
        description="Immune to Stun",
        cost=5,
        location={
             "The Continent": "Chromatic Petank",
        },
    ),
    Pictos(
        name="At Death's Door",
        description="Deal 50% more damage if Health is below 10%",
        cost=5,
        location={
             "Stone Wave Cliffs": "Lampmaster",
             "Painting Workshop": "Lampmaster",
        },
    ),
    Pictos(
        name="Attack Lifesteal",
        description="Recover 15% Health on Base Attack",
        cost=15,
        location={
             "Ancient Sanctuary": "Sanctuary Maze Expedition Flag, hug the right wall until you crouch to enter an area. Take a right and go straight until you enter a dark cave",
        },
    ),
    Pictos(
        name="Augmented Aim",
        description="50% increased Free Aim damage",
        cost=3,
        location={
             "Flying Waters": "Parkour after the Noco's Hut Expedition Flag",
        },
    ),
    Pictos(
        name="Augmented Attack",
        description="50% increased Base Attack damage",
        cost=7,
        location={
             "Spring Meadows": "Chromatic Lancelier",
        },
    ),
    Pictos(
        name="Augmented Counter I",
        description="25% increased Counterattack damage",
        cost=3,
        location={
             "Flying Waters": "Bourgeon",
             "Flying Manor": "Bourgeon",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Augmented Counter II",
        description="50% increased Counterattack damage",
        cost=5,
        location={
             "Visages": "Chromatic Ramasseur",
        },
    ),
    Pictos(
        name="Augmented Counter III",
        description="75% increased Counterattack damage",
        cost=7,
        location={
             "Lumiere": "Chromatic Echassier",
             "Frozen Hearts": "Danseuse Teacher",
        },
    ),
    Pictos(
        name="Augmented First Strike",
        description="50% increased damage on the first hit. Once per battle",
        cost=5,
        location={
             "Esquie's Nest": "Francois",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Auto Death",
        description="Kill self on battle start",
        cost=1,
        location={
             "Yellow Harvest": "Merchant",
        },
    ),
    Pictos(
        name="Auto Powerful",
        description="Apply Powerful for 3 turns on battle start",
        cost=10,
        location={
             "Floating Cemetery": "The Chalier",
        },
    ),
    Pictos(
        name="Auto Regen",
        description="Apply Regen for 3 turns on battle start",
        cost=10,
        location={
             "Sirene": "Dancing Classes Expedition Flag, around Benisseur",
        },
    ),
    Pictos(
        name="Auto Rush",
        description="Apply Rush for 3 turns on battle start",
        cost=10,
        location={
             "Old Lumiere": "Left Street Expedition Flag,around the broken bridge",
        },
    ),
    Pictos(
        name="Auto Shell",
        description="Apply Shell for 3 turns on battle start",
        cost=10,
        location={
             "Stone Wave Cliffs": "Help the fallen Hexga",
        },
    ),
    Pictos(
        name="Base Shield",
        description="+1 Shield if not affected by any Shield on turn start",
        cost=20,
        location={
             "The Chosen Path": "Complete all the challenges",
        },
    ),
    Pictos(
        name="Beneficial Contamination",
        description="+2 AP on applying a Status Effect. Once per turn",
        cost=15,
        location={
             "Falling Leaves": "Merchant",
        },
    ),
    Pictos(
        name="Break Specialist",
        description="Break damage is increased by 50%, but base damage is reduced by 20%",
        cost=1,
        location={
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Breaker",
        description="25% increased Break damage",
        cost=10,
        location={
             "Ancient Sanctuary": "Ultimate Sakapatate",
        },
    ),
    Pictos(
        name="Breaking Attack",
        description="Base Attack can Break",
        cost=10,
        location={
             "The Monolith": "Clair Obscur",
        },
    ),
    Pictos(
        name="Breaking Burn",
        description="25% increased Break damage on Burning enemies",
        cost=5,
        location={
             "The Continent": "Southwest of Old Lumiere, behind a Bourgeon",
        },
    ),
    Pictos(
        name="Breaking Counter",
        description="50% increased Break damage on Counterattack",
        cost=3,
        location={
             "Stone Wave Cliffs": "Around Hexga after the Entrance Expedition Flag",
        },
    ),
    Pictos(
        name="Breaking Death",
        description="Fully charge enemy's Break Bar on death",
        cost=5,
        location={
             "The Continent": "Thunder Eveque",
        },
    ),
    Pictos(
        name="Breaking Shots",
        description="50% increased Break damage with Free Aim Shots",
        cost=1,
        location={
             "Stone Wave Cliffs": "Basalt Waves Expedition Flag, turn back and head down the rope. Cross the grapple point and follow the left wall to some pillar parkour with the Pictos on the far side",
        },
    ),
    Pictos(
        name="Breaking Slow",
        description="25% increased Break damage against Slowed enemies",
        cost=5,
        location={
             "The Continent": "Inside a Paint Spike a little northwest of Spring Meadows",
        },
    ),
    Pictos(
        name="Burn Affinity",
        description="25% increased damage on Burning Targets",
        cost=10,
        location={
             "Frozen Hearts": "Glacial Falls Expedition Flag, top of the train",
        },
    ),
    Pictos(
        name="Burning Break",
        description="Apply 3 Burn stacks on Breaking a target",
        cost=3,
        location={
             "Frozen Hearts": "Glacial Falls Expedition Flag, on top of a structure in the left side",
        },
    ),
    Pictos(
        name="Burning Death",
        description="Apply 3 Burn to all enemies on Death",
        cost=5,
        location={
             "Frozen Hearts": "Glacial Falls Expedition Flag, 2 Danseuses and a Pelerin",
             "Flying Manor": "Gargant",
        },
    ),
    Pictos(
        name="Burning Mark",
        description="Apply Burn on hitting a Marked enemy",
        cost=15,
        location={
             "Ancient Sanctuary": "Entrance Expedition Flag, run towards the large Gestral structure in the distance and follow the stream on the left. Next to the main path will be a slope leading down. Will be on a ledge after a short climb",
        },
    ),
    Pictos(
        name="Burning Shots",
        description="20% chance to Burn on Free Aim Shot",
        cost=3,
        location={
             "Spring Meadows": "Abandoned Expedition Camp Expedition Flag",
             "Sacred River": "Merchant",
             "Monoco's Station": "Merchant",
        },
    ),
    Pictos(
        name="Charging Alteration",
        description="+10% of a Gradient Charge on applying a Buff. Once per turn",
        cost=10,
        location={
             "Flying Manor": "It's found in the area where you fight the Gargant and Lampmaster. Found on a floating platform that can be reached by using the grappling hook. After coming down the elevator and walking down the stairs, walk forward until you see the place to use the grappling hook, it should be to the left on the floating platform",
        },
    ),
    Pictos(
        name="Charging Attack",
        description="+15% of a Gradient Charge on Base Attack",
        cost=7,
        location={
             "The Reacher": "From the Mountain Expedition Flag, proceed across and grapple to the mountain. Just before the hot air balloon to the next section of the tower, take the left path up and climb up the wall structures at the end of this path. Head left to find the Fading Man. To the right of the Fading Man, grapple across twice. After second grapple, turn left immediately and head through the crawl space. Drop down the wooden ledge to pick up Charging Attack",
        },
    ),
    Pictos(
        name="Charging Burn",
        description="+20% of a Gradient Charge on applying Burn. Once per turn",
        cost=10,
        location={
             "Renoir's Drafts": "On the bridge behind the Merchant",
        },
    ),
    Pictos(
        name="Charging Counter",
        description="+20% of a Gradient Charge on Counterattack",
        cost=10,
        location={
             "The Reacher": "From the Mountain Expedition Flag, proceed across and grapple to the mountain. Take the left path up and climb up the wall structures at the end of this path. Grapple across and continue to the right of the Fading Man. Grapple across and go straight ahead into the field. Take out the enemies and pick up Charging Counter",
        },
    ),
    Pictos(
        name="Charging Critical",
        description="+20% of a Gradient Charge on Critical Hit. Once per turn",
        cost=10,
        location={
             "Endless Tower": "Stage 5, Trial 3",
             "Renoir's Drafts": "Golden Tree Expedition Flag, platforms around Merchant",
        },
    ),
    Pictos(
        name="Charging Mark",
        description="20% of a Gradient Charge on hitting a Marked target. Once per turn",
        cost=10,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Charging Stun",
        description="+5% of a Gradient Charge on hitting a Stunned enemy",
        cost=5,
        location={
             "Lumiere": "Before the Shattered Alley Expedition Flag",
        },
    ),
    Pictos(
        name="Charging Tint",
        description="+5% of a Gradient Charge on using an item",
        cost=2,
        location={
             "The Continent": "On a small patch of land southeast of the Gestral Beach south of Old Lumiere on the world map, near a Stalact",
        },
    ),
    Pictos(
        name="Charging Weakness",
        description="+15% of a Gradient Charge on hitting a Weakness. Once per turn",
        cost=5,
        location={
             "The Reacher": "Merchant",
        },
    ),
    Pictos(
        name="Cheater",
        description="Always play twice in a row",
        cost=40,
        location={
             "The Continent": "Sprong",
        },
    ),
    Pictos(
        name="Cleansing Tint",
        description="Healing Tints also remove all Status Effects from the target",
        cost=5,
        location={
             "Spring Meadows": "Eveque",
        },
    ),
    Pictos(
        name="Clea's Life",
        description="On turn start, if no damage taken since last turn, recover 100% Health",
        cost=30,
        location={
             "Flying Manor": "Clea",
        },
    ),
    Pictos(
        name="Combo Attack I",
        description="Base Attack has 1 extra hit",
        cost=10,
        location={
             "Forgotten Battlefield": "Dualliste",
        },
    ),
    Pictos(
        name="Combo Attack II",
        description="Base Attack has 1 extra hit",
        cost=20,
        location={
             "The Monolith": "Drops from Chromatic Clair Obscur in Monolith Peak after defeating the Paintress and returning",
        },
    ),
    Pictos(
        name="Combo Attack III",
        description="Base Attack has 1 extra hit",
        cost=30,
        location={
             "Dark Gestral Arena": "Win all three challenges",
        },
    ),
    Pictos(
        name="Confident",
        description="Take 50% less damage, but cannot be Healed",
        cost=20,
        location={
             "Stone Wave Cliffs": "Hexga past the Entrance Expedition Flag",
             "The Continent": "On an island northeast of the Stone Wave Cliffs",
        },
    ),
    Pictos(
        name="Confident Fighter",
        description="30% increased damage, but cannot be Healed",
        cost=15,
        location={
             "Visages": "Joyful Vale area. Head up the ramp near the mask on the right side, then defeat the Boucheclier. Proceed to the area on the right",
        },
    ),
    Pictos(
        name="Critical Break",
        description="25% increased Break damage on Critical Hits",
        cost=5,
        location={
             "The Continent": "Inside a Paint Spike on a small beach to the west of the Isle of the Eyes",
        },
    ),
    Pictos(
        name="Critical Burn",
        description="25% increased Critical Chance on Burning enemies",
        cost=5,
        location={
             "Spring Meadows": "After taking out the first wave of Lancelier enemies past the Meadows Corridor Expedition Flag",
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Critical Moment",
        description="50% increased Critical Chance if Health is below 30%",
        cost=5,
        location={
             "Gestral Village": "Merchant",
        },
    ),
    Pictos(
        name="Critical Stun",
        description="100% Critical Chance on hitting a Stunned target",
        cost=5,
        location={
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Critical Vulnerability",
        description="25% increased Critical Chance on Defenceless enemies",
        cost=5,
        location={
             "The Continent": "A camp surrounded by enemies in an alcove to the northwest of Falling Leaves",
        },
    ),
    Pictos(
        name="Critical Weakness",
        description="25% increased Critical Chance on Weakness",
        cost=5,
        location={
             "Endless Tower": "Stage 6, Trial 3",
        },
    ),
    Pictos(
        name="Dead Energy I",
        description="+3 AP on killing an enemy",
        cost=2,
        location={
             "The Continent": "On the southern part of the beach that contains the entrance to Dark Shores, there is a cluster of crates you can break apart containing the Picto",
        },
    ),
    Pictos(
        name="Dead Energy II",
        description="+3 AP on killing an enemy",
        cost=2,
        location={
             "Spring Meadows": "On a ledge at the end of the path directly to the right upon exiting the short tunnel past the Abandoned Expedition Camp Expedition Flag",
        },
    ),
    Pictos(
        name="Death Bomb",
        description="On Death, deal damage to all enemies",
        cost=5,
        location={
             "Yellow Harvest": "From the Harvester's Hollow Expedition Flag, head down the path and go towards the slope on the right. To the right of that slope",
        },
    ),
    Pictos(
        name="Defensive Mode",
        description="On receiving damage, consume 1 AP to take 30% less damage, if possible",
        cost=1,
        location={
             "Stone Wave Cliffs": "Enter Stone Wave Cliffs from the beach portal and directly to the left",
        },
    ),
    Pictos(
        name="Dodger",
        description="Gain 1 AP on Perfect Dodge. Once per turn",
        cost=1,
        location={
             "Spring Meadows": "Portier inside the cave after Lune finds you",
        },
    ),
    Pictos(
        name="Double Burn",
        description="On applying a Burn stack, apply a second one",
        cost=30,
        location={
             "Visages": "Anger Vale. A cavern on the right side. Left path. Moissonneuse with two Bouchecliers",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Double Mark",
        description="Mark requires 1 more hit to be removed",
        cost=20,
        location={
             "Sirene": "Merchant",
        },
    ),
    Pictos(
        name="Draining Cleanse",
        description="Consume 1 AP to prevent Status Effects application, if possible",
        cost=15,
        location={
             "The Reacher": "From the Entrance Expedition Flag, grapple across to the next tower, continue ahead, and grapple onto the next tower. Proceed ahead and take the rope down. From there, take the path on the right, defeat the Orphelin and pick up",
        },
    ),
    Pictos(
        name="Effective Heal",
        description="Double all Heals received",
        cost=30,
        location={
             "Sirene": "Proceed to the Dancing Classes Expedition Flag",
        },
    ),
    Pictos(
        name="Effective Support",
        description="+2 AP on using an item",
        cost=5,
        location={
             "The Continent": "On the ground in a small patch of grassy land northeast of Sirene",
        },
    ),
    Pictos(
        name="Empowering Attack",
        description="Gain Powerful for 1 turn on Base Attack",
        cost=10,
        location={
             "Spring Meadows": "Found after defeating Eveque",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Empowering Break",
        description="Gain Powerful on Breaking a target",
        cost=3,
        location={
             "Flying Manor": "Area where fight Goblu. When enter, hug the left wall until there's a chroma rope you can zip down",
        },
    ),
    Pictos(
        name="Empowering Dodge",
        description="5% increased damage for each consecutive successful Dodge. Can stack up to 10 times",
        cost=5,
        location={
             "The Continent": "A little north of the Endless Night Sanctuary in an abandoned camp in the top left corner",
        },
    ),
    Pictos(
        name="Empowering Last Stand",
        description="Gain Powerful if fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Julien Tiny Head",
        },
    ),
    Pictos(
        name="Empowering Parry",
        description="Each successful Parry increases damage by 5% until end of the following turn. Taking any damage removes this buff",
        cost=5,
        location={
             "The Monolith": "Paint Cage in the Tainted Hearts area",
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Empowering Tint",
        description="Healing Tints also apply Powerful",
        cost=5,
        location={
             "Forgotten Battlefield": "Battlefield Expedition Flag, head through the trenches on the right side of the Fading Woman",
             "Endless Tower": "Stage 8, Trial 3",
        },
    ),
    Pictos(
        name="Energetic Healer",
        description="+2 AP on Healing an ally. Once per turn",
        cost=10,
        location={
             "Flying Manor": "Around Lampmaster",
        },
    ),
    Pictos(
        name="Energising Attack I",
        description="+1 AP on Base Attack",
        cost=10,
        location={
             "Yellow Harvest": "Glaise in the Yellow Spire Wrecks section",
             "Renoir's Drafts": "Merchant",
             "Painting Workshop": "Lampmaster",
        },
    ),
    Pictos(
        name="Energising Attack II",
        description="+1 AP on Base Attack",
        cost=15,
        location={
             "Sirene": "Merchant",
        },
    ),
    Pictos(
        name="Energising Break",
        description="+3 AP on Breaking a target",
        cost=3,
        location={
             "Flying Waters": "Lumieran Streets Expedition Flag, climb the wall on the left and continue down this path. Chromatic Troubadour",
        },
    ),
    Pictos(
        name="Energising Burn",
        description="+1 AP on applying Burn. Once per turn",
        cost=10,
        location={
             "Frozen Hearts": "Chromatic Veilleur",
        },
    ),
    Pictos(
        name="Energising Cleanse",
        description="Dispel the first negative Status Effect received and gain 2 AP",
        cost=10,
        location={
             "The Monolith": "Merchant",
        },
    ),
    Pictos(
        name="Energising Death",
        description="On death, +4 AP to allies",
        cost=5,
        location={
             "Forgotten Battlefield": "In the Fort Ruins section, head inside the structure to find a Chalier. Defeat it, then head to the ledge it was blocking to find",
             "Monoco's Station": "Merchant",
        },
    ),
    Pictos(
        name="Energising Gradient",
        description="+1 AP per Gradient Charge consumed",
        cost=10,
        location={
             "The Continent": "Frost Eveque",
        },
    ),
    Pictos(
        name="Energising Heal",
        description="On Healing an ally, also give 2 AP",
        cost=10,
        location={
             "The Continent": "On the beach just below the Endless Tower",
        },
    ),
    Pictos(
        name="Energising Jump",
        description="+1 AP on Jump Counterattack",
        cost=5,
        location={
             "Ancient Sanctuary": "Left side of the starting area",
        },
    ),
    Pictos(
        name="Energising Pain",
        description="No longer gain AP on Parry. +1 AP on getting hit",
        cost=10,
        location={
             "Stone Wave Cliffs": "Follow the main path all the way to the destroyed airship. Go through the tunnel that was left by the remnants of the airship, then cross the platform to reach the other side. Stay on this path until you encounter a duo of a Greatsword Cultist and Reaper Cultist near the bridge",
             "Flying Manor": "Greatsword Cultist",
             "The Continent": "West of the Isle of the Eyes, there is a small shore. Greatsword Cultist",
             "The Monolith": "Two Greatsword Cultists past the Tainted Cliffs Expedition Flag",
        },
    ),
    Pictos(
        name="Energising Parry",
        description="+1 AP on successful Parry",
        cost=15,
        location={
             "Forgotten Battlefield": "Chromatic Luster",
             "Sacred River": "Merchant",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Energising Powerful",
        description="Give 2 AP on applying Powerful",
        cost=10,
        location={
             "Lumiere": "The spot where Prologue started",
        },
    ),
    Pictos(
        name="Energising Revive",
        description="+3 AP to all allies when revived",
        cost=5,
        location={
             "Stone Wave Cliffs Cave": "Chromatic Hexga",
        },
    ),
    Pictos(
        name="Energising Rush",
        description="Give 2 AP on applying Rush",
        cost=10,
        location={
             "Endless Tower": "Stage 2, Trial 3",
        },
    ),
    Pictos(
        name="Energising Shell",
        description="Give 2 AP on applying Shell",
        cost=10,
        location={
             "The Continent": "In a paint spike in the area of the Chromatic Petank to the east of The Meadows",
        },
    ),
    Pictos(
        name="Energising Shots",
        description="20% chance to gain 1 AP on Free Aim Shot",
        cost=10,
        location={
             "Flying Manor": "On the left side of Goblu's arena",
        },
    ),
    Pictos(
        name="Energising Start I",
        description="+1 AP on battle start",
        cost=5,
        location={
             "The Continent": "On the right side of the beach behind the Gestral Village",
        },
    ),
    Pictos(
        name="Energising Start II",
        description="+1 AP on battle start",
        cost=10,
        location={
             "Ancient Sanctuary": "From the Sanctuary Maze Expedition Flag, stay on the right path and go through the crouch hole. From there take the right path and go forward until you reach the end of the room with a Ranger Sakapatate. You will be able to climb the ledge on the left and find the pictos at the end of the path",
        },
    ),
    Pictos(
        name="Energising Start III",
        description="+1 AP on battle start",
        cost=15,
        location={
             "Esquie's Nest": "Cross the pillar and use your grappling hook to get across the second gap as well",
        },
    ),
    Pictos(
        name="Energising Start IV",
        description="+1 AP on battle start",
        cost=20,
        location={
             "Forgotten Battlefield": "Main Gate Expedition Flag, stick to the right. The nearby path to find a trench",
        },
    ),
    Pictos(
        name="Energising Stun",
        description="+1 AP on hitting a Stunned target with a Skill",
        cost=10,
        location={
             "Flying Manor": "Paint Cage on the left side of the Eveque bosses area",
        },
    ),
    Pictos(
        name="Energising Turn",
        description="+1 AP on turn start",
        cost=20,
        location={
             "Sirene": "Sirene",
             "Sacred River": "Merchant",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Energy Master",
        description="Every AP gain is increased by 1",
        cost=40,
        location={
             "The Continent": "Serpenphare",
        },
    ),
    Pictos(
        name="Enfeebling Attack",
        description="Base Attack applies Powerless for 1 turn",
        cost=10,
        location={
             "The Monolith": "Corpse next to a train near the Merchant in the Tainted Hearts section",
        },
    ),
    Pictos(
        name="Enfeebling Mark",
        description="Marked targets deal 30% less damage",
        cost=10,
        location={
             "Stone Wave Cliffs": "From the Flooded Buildings Expedition Flag, head down the path past the Rocher. A short ways down, enter the building to your left. Head up and exit to the open area, and grapple to the cliffs to the right",
        },
    ),
    Pictos(
        name="Exhausting Power",
        description="50% increased damage if Exhausted",
        cost=2,
        location={
             "Stone Wave Cliffs Cave": "In the left side of the Chromatic Hexga arena",
        },
    ),
    Pictos(
        name="Exposing Attack",
        description="Base Attack applies Defenceless for 1 turn",
        cost=10,
        location={
             "Flying Waters": "Merchant",
        },
    ),
    Pictos(
        name="Exposing Break",
        description="Apply Defenceless on Break",
        cost=5,
        location={
             "The Reacher": "Merchant",
        },
    ),
    Pictos(
        name="Faster Than Strong",
        description="Always play twice in a row, but deal 50% less damage",
        cost=10,
        location={
             "Lumiere": "Creation",
        },
    ),
    Pictos(
        name="First Offensive",
        description="First hit dealt and taken deals 50% more damage",
        cost=5,
        location={
             "Abbest Cave": "Chromatic Abbest",
        },
    ),
    Pictos(
        name="First Strike",
        description="Play first",
        cost=10,
        location={
             "Stone Wave Cliffs": "Make your way through the broken airship past the Hexga, and make your way to the next section. Go through the field past the enemies and make your way up the shorter cliffs on the right. Defeat the group of enemies and pick up this Pictos at the base of the statue behind them",
        },
    ),
    Pictos(
        name="Fueling Break",
        description="Breaking a target doubles its Burn amount",
        cost=5,
        location={
             "The Continent": "Exit from the northern portal in Monoco's Station and then make your way up to the right then take the path on the left when you reach the fork in the path. In the next fork in the path, take the left path to reach the other portal to The Carousel, just ahead on the right you can pick up Fueling Break between two boxes",
             "Endless Tower": "Stage 7, Trial 3",
        },
    ),
    Pictos(
        name="Full Strength",
        description="25% increased damage on full Health",
        cost=15,
        location={
             "Lumiere": "Merchant",
        },
    ),
    Pictos(
        name="Glass Cannon",
        description="Deal 25% more damage, but take 25% more damage",
        cost=10,
        location={
             "Visages": "Chromatic Ramasseur",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Gradient Break",
        description="+50% of a Gradient Charge on Breaking a target",
        cost=5,
        location={
             "Endless Night Sanctuary": "There is a small cave-like room where you'll find a dead expeditioner and this pictos. Starting from the entrance, continue straight until you reach the Grandis NPC. Take the middle path and turn right before reaching the crawl space. The cave will be on the left",
        },
    ),
    Pictos(
        name="Gradient Breaker",
        description="50% increased Breaking damage with Gradient Attacks",
        cost=5,
        location={
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Gradient Fighter",
        description="+25% increased damage with Gradient Attacks",
        cost=5,
        location={
             "Lumiere": "In Lumiere's Garden, follow the path on the left",
        },
    ),
    Pictos(
        name="Greater Defenceless",
        description="+15% to Defenceless damage amplification",
        cost=15,
        location={
             "The Monolith": "Merchant",
             "Endless Tower": "Stage 1, Trial 3",
        },
    ),
    Pictos(
        name="Greater Powerful",
        description="+15% to Powerful damage increase",
        cost=10,
        location={
             "Sirene": "Merchant",
        },
    ),
    Pictos(
        name="Greater Powerless",
        description="+15% to Powerless damage reduction",
        cost=15,
        location={
             "Endless Tower": "Stage 10, Trial 3",
        },
    ),
    Pictos(
        name="Greater Rush",
        description="+25% Rush Speed increase",
        cost=10,
        location={
             "Monoco's Station": "Merchant",
        },
    ),
    Pictos(
        name="Greater Shell",
        description="+10% to Shell damage reduction",
        cost=10,
        location={
             "Sirene": "Dancing Classes Expedition Flag, head straight ahead until left turn under an arch. Follow the path left, across the gap and down to another moving platform. After taking the podium down, turn right at the path and head to the end",
        },
    ),
    Pictos(
        name="Greater Slow",
        description="+15% to Slow Speed reduction",
        cost=15,
        location={
             "Sky Island": "On a broken set of stairs past the Chromatic Glaise",
        },
    ),
    Pictos(
        name="Healing Boon",
        description="Heal 15% HP on applying a buff",
        cost=10,
        location={
             "The Reacher": "On the unreachable ledge in the Ladder Area. Need to take the hot air balloon from the Foggy Area located near the merchant",
        },
    ),
    Pictos(
        name="Healing Counter",
        description="Recover 25% Health on Counterattack",
        cost=10,
        location={
             "Old Lumiere": "Merchant",
        },
    ),
    Pictos(
        name="Healing Death",
        description="On death, the rest of the Expedition recover all Health",
        cost=5,
        location={
             "Old Lumiere": "From the Manor Gardens Expedition Flag, head to the right (away from the Manor) to find a new path",
        },
    ),
    Pictos(
        name="Healing Fire",
        description="Recover 25% Health when attacking a Burning target. Once per turn",
        cost=10,
        location={
             "Sirene": "Crumbling Path Expedition Flag, turn to the right and up the ramp. Go to the edge and take the rope down",
        },
    ),
    Pictos(
        name="Healing Mark",
        description="Recover 25% Health on hitting a Marked enemy. Once per turn",
        cost=20,
        location={
             "Gestral Village": "Merchant",
        },
    ),
    Pictos(
        name="Healing Parry",
        description="Recover 3% Health on Parry",
        cost=5,
        location={
             "The Continent": "At a camp behind the Bourgeon after defeating it",
        },
    ),
    Pictos(
        name="Healing Share",
        description="Receive 15% of all Heals affecting other characters",
        cost=5,
        location={
             "Visages": "Merchant",
        },
    ),
    Pictos(
        name="Healing Stun",
        description="Recover 5% Health on hitting a Stunned target",
        cost=10,
        location={
             "Lumiere": "After exiting the Opera House, grapple across until you encounter an Aberration and a Ballet",
        },
    ),
    Pictos(
        name="Healing Tint Energy",
        description="Healing Tints also give 1 AP",
        cost=1,
        location={
             "Stone Wave Cliffs": "From the Flooded Buildings Expedition Flag, take the stairs down and head to the end of the path and use your grappling hook to the other side. Take the group of enemies (1 Hexga and 2 Greatsword Cultists), turn to the left, and you find a sword that's stuck in the ground. There you can pick up the Healing Tint Energy Pictos",
        },
    ),
    Pictos(
        name="Immaculate",
        description="30% increased damage until a hit is received",
        cost=10,
        location={
             "Visages": "Mask Keeper",
        },
    ),
    Pictos(
        name="In Medias Res",
        description="+3 Shields on Battle Start, but max Health is halved",
        cost=10,
        location={
             "Dark Shores": "2 Noir",
        },
    ),
    Pictos(
        name="Inverted Affinity",
        description="Apply Inverted on self for 3 turns on battle start. 50% increased damage while Inverted",
        cost=5,
        location={
             "Forgotten Battlefield": "Merchant",
        },
    ),
    Pictos(
        name="Last Stand Critical",
        description="100% Critical Chance while fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Matthieu the Colossus",
        },
    ),
    Pictos(
        name="Longer Burn",
        description="Burn duration is increased by 2",
        cost=15,
        location={
             "The Continent": "Chromatic Aberration",
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Longer Powerful",
        description="On applying Powerful, its duration is increased by 2",
        cost=10,
        location={
             "Old Lumiere": "Merchant",
        },
    ),
    Pictos(
        name="Longer Rush",
        description="On applying Rush, its duration is increased by 2",
        cost=10,
        location={
             "The Continent": "On the southern tip of the valley",
        },
    ),
    Pictos(
        name="Longer Shell",
        description="On applying Shell, its duration is increased by 2",
        cost=10,
        location={
             "Forgotten Battlefield": "Chalier near a fork in the path at the start",
             "The Reacher": "Mountain Expedition Flag, continue ahead and grapple across to the mountain. Take the path up on the right to find a little course to go through. Carefully make your way across to the other side and pick up Longer Shell",
             "The Continent": "Group of enemies consisting of a Rocher, a Bouchelier, and a Chalier at the yellow forest northeast of The Carousel",
             "The Monolith": "Nevrons near Tainted Battlefield Expedition Flag",
        },
    ),
    Pictos(
        name="Marking Break",
        description="Apply Mark on Break",
        cost=5,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Marking Shots",
        description="20% chance to apply Mark on Free Aim Shot",
        cost=3,
        location={
             "Flying Waters": "Found at the end of a path guarded by 2 Lusters, on the path to the left right after encountering the first solo Luster",
        },
    ),
    Pictos(
        name="Painted Power",
        description="Damage can exceed 9,999",
        cost=5,
        location={
             "The Monolith": "The Paintress",
        },
    ),
    Pictos(
        name="Painter",
        description="Convert all Physical damage to Void damage",
        cost=10,
        location={
             "Flying Manor": "Eveque boss area",
        },
    ),
    Pictos(
        name="Perilous Parry",
        description="+1 AP on Parry, but damage received is doubled",
        cost=5,
        location={
             "Stone Wave Cliffs": "Gold Chevaliere in the second lower level",
        },
    ),
    Pictos(
        name="Piercing Shot",
        description="25% increased Free Aim damage. Free Aim Shots ignore Shields",
        cost=2,
        location={
             "Ancient Sanctuary": "From the Sanctuary Maze Expedition Flag, head forward and hug the left wall until you reach a Paint Spike",
        },
    ),
    Pictos(
        name="Powered Attack",
        description="On every damage dealt, try to consume 1 AP. If successful, increase damage by 20%",
        cost=10,
        location={
             "Visages": "Anger Vale, head to the path on the left then go down the rope beyond the group of Bouchecliers",
        },
    ),
    Pictos(
        name="Powerful Heal",
        description="Healing an ally also applies Powerful for 1 turn",
        cost=5,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Powerful Mark",
        description="Gain Powerful on hitting a Marked enemy",
        cost=5,
        location={
             "Flying Manor": "Path to Goblu",
        },
    ),
    Pictos(
        name="Powerful on Shell",
        description="Apply Powerful on applying Shell",
        cost=10,
        location={
             "Sirene": "After taking the platform at the end of the path from the Dancing Classes Expedition Flag, head into the path on the right, and follow the ribbon on the right side going down to fight a Benisseur",
             "The Continent": "A little north of the Endless Night Sanctuary in an abandoned camp in the top left corner",
        },
    ),
    Pictos(
        name="Powerful Revive",
        description="Apply Powerful for 3 turns when revived",
        cost=3,
        location={
             "The Continent": "Chromatic Bruler by the beach behind the Gestral Village",
             "Flying Manor": "Paint Cage in an area behind Dualliste reached by grappling",
        },
    ),
    Pictos(
        name="Powerful Shield",
        description="10% increased damage per Shield Point on self",
        cost=5,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Powerful Shots",
        description="20% chance to gain Powerful on Free Aim Shot",
        cost=3,
        location={
             "Gestral Village": "Paint Spike across from the Gestral Doctor",
        },
    ),
    Pictos(
        name="Pro Retreat",
        description="Allows Flee to be instantaneous",
        cost=40,
        location={
             "Camp": "Rewarded by Sastro for finding all 9 Lost Gestrals",
        },
    ),
    Pictos(
        name="Protecting Attack",
        description="Gain Shell for 1 turn on Base Attack",
        cost=10,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Protecting Death",
        description="On death, allies gain Shell",
        cost=5,
        location={
             "Sirene": "From the Sewing Atelier Expedition Flag, head backwards, up the rope and across the 2 grapple points",
        },
    ),
    Pictos(
        name="Protecting Heal",
        description="Healing an ally also applies Shell for 1 turn",
        cost=5,
        location={
             "The Reacher": "Merchant",
             "Esoteric Ruins": "Friendly Portier",
        },
    ),
    Pictos(
        name="Protecting Last Stand",
        description="Gain Shell if fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Dominique Giant Feet",
        },
    ),
    Pictos(
        name="Protecting Shots",
        description="20% chance to gain Shell on Free Aim Shot",
        cost=3,
        location={
             "Flying Manor": "Upon entering the location, head down the stairs and turn right. To the right, pass in front of the Cruler statue and between the pillars. Use the rope to zip down and find Protecting Shots on the edge of a broken picture frame",
        },
    ),
    Pictos(
        name="Protecting Tint",
        description="Healing Tints also apply Shell",
        cost=5,
        location={
             "The Reacher": "From the Foggy Area Expedition Flag, cross the bridges down to the field, before heading into the field, make a U-turn to the right. Cross the plank",
        },
    ),
    Pictos(
        name="Quick Break",
        description="Play again on Breaking a target",
        cost=3,
        location={
             "Endless Night Sanctuary": "Chromatic Cruler",
        },
    ),
    Pictos(
        name="Random Defense",
        description="Damage taken is randomly multiplied by a value between 50% and 200%",
        cost=5,
        location={
             "The Monolith": "Behind the Tainted Sanctuary Paint Spike",
        },
    ),
    Pictos(
        name="Recovery",
        description="Recovers 10% Health on turn start",
        cost=10,
        location={
             "Red Woods": "Merchant",
        },
    ),
    Pictos(
        name="Rejuvenating Revive",
        description="Apply Regen for 3 turns when revived",
        cost=3,
        location={
             "Stone Wave Cliffs": "Chromatic Gault",
        },
    ),
    Pictos(
        name="Revive Paradox",
        description="Play immediately when revived",
        cost=5,
        location={
             "Old Lumiere": "Chromatic Danseuse",
        },
    ),
    Pictos(
        name="Revive Tint Energy",
        description="Revive Tints also give 3 AP",
        cost=10,
        location={
             "Forgotten Battlefield": "After defeating Dualliste",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Rewarding Mark",
        description="+2 AP on dealing damage to a Marked target. Once per turn",
        cost=5,
        location={
             "Flying Waters": "At the end of the path to the left past the Cruler after the Coral Cave Expedition Flag",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Roulette",
        description="Every hit has a 50% chance to deal either 50% or 200% of its damage",
        cost=5,
        location={
             "Gestral Village": "Interact with a door to talk to a Gestral Gambler",
             "Flying Manor": "Eveque bosses",
        },
    ),
    Pictos(
        name="Rush on Powerful",
        description="Apply Rush on applying Powerful",
        cost=10,
        location={
             "Endless Tower": "Stage 9, Trial 3",
             "Renoir's Drafts": "From Golden Tree Expedition Flag, go up the ramp, go to the right of the portal, and grapple up to the building. The Picto is at the end of the path",
        },
    ),
    Pictos(
        name="SOS Power",
        description="Apply Powerful when falling below 50% Health",
        cost=5,
        location={
             "Stone Wave Cliffs": "From the Paintress Shrine Expedition Flag, go down the path on the right and cross the narrow stone bridge. Take the path on the right and hug the right wall up the grassy slope",
        },
    ),
    Pictos(
        name="SOS Rush",
        description="Apply Rush when falling below 50% Health",
        cost=5,
        location={
             "Falling Leaves": "Near Expedition 35's Journal and the Human Bridge",
        },
    ),
    Pictos(
        name="SOS Shell",
        description="Apply Shell when falling below 50% Health ",
        cost=5,
        location={
             "Flying Waters": "Hugging the left wall from the start of the area",
        },
    ),
    Pictos(
        name="Second Chance",
        description="Revive with 100% Health. Once per battle",
        cost=40,
        location={
             "The Monolith": "Renoir",
             "Renoir's Drafts": "Creation",
        },
    ),
    Pictos(
        name="Shared Care",
        description="When healing an ally, also Heal self for 50% of that value",
        cost=10,
        location={
             "The Continent": "Some broken crates on the southern part of the island northwest of the Red Woods",
        },
    ),
    Pictos(
        name="Shell On Rush",
        description="Apply Shell on applying Rush",
        cost=10,
        location={
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Shield Affinity",
        description="30% increased damage while having Shields, but receiving any damage always removes all Shields",
        cost=15,
        location={
             "Sirene": "Break the Paint Cage to obtain Shield Affinity",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Shielding Death",
        description="On death, allies gain 3 Shield points",
        cost=10,
        location={
             "The Crows": "Shoot all the crows and defeat the Chromatic Chapelier",
        },
    ),
    Pictos(
        name="Shielding Tint",
        description="Healing Tints also add 2 Shields",
        cost=10,
        location={
             "The Continent": "On the ground under wooden crates near the Bourgeon southeast of Forgotten Battlefield",
        },
    ),
    Pictos(
        name="Shortcut",
        description="Immediately play when falling below 30% Health. Once per battle",
        cost=5,
        location={
             "Lumiere": "Head up the stairs at the harbour and defeat the Aberration to receive Shortcut as a drop",
        },
    ),
    Pictos(
        name="Slowing Break",
        description="Apply Slow on Break",
        cost=5,
        location={
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Sniper",
        description="First Free Aim Shot each turn deals 200% increased damage and can Break",
        cost=15,
        location={
             "The Reacher": "Mountain Expedition Flag, proceed along the path ahead, and grapple across to the mountain",
        },
    ),
    Pictos(
        name="Solidifying",
        description="+2 Shields when the character's Health falls below 50%. Once per battle",
        cost=10,
        location={
             "Crushing Cavern": "Giant Sapling",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Solo Fighter",
        description="Deal 50% more damage if fighting alone",
        cost=1,
        location={
             "Hidden Gestral Arena": "Bertrand Big Hands",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Staggering Attack",
        description="50% increased Break damage on Base Attack",
        cost=1,
        location={
             "Flying Waters": "Next to the Coral Caves Expedition Flag",
        },
    ),
    Pictos(
        name="Stay Marked",
        description="50% chance to apply Mark when attacking a Marked target",
        cost=10,
        location={
             "The Monolith": "Chromatic Bourgeon",
             "Flying Manor": "Merchant",
        },
    ),
    Pictos(
        name="Stun Boost",
        description="30% increased damage on Stunned targets",
        cost=10,
        location={
             "Ancient Sanctuary": "Ultimate Sakapatate, there will be a small cave",
             "Sacred River": "Merchant",
        },
    ),
    Pictos(
        name="Survivor",
        description="Survive fatal damage with 1 Health. Once per battle",
        cost=20,
        location={
             "Monoco's Station": "Merchant",
        },
    ),
    Pictos(
        name="Sweet Kill",
        description="Recover 50% Health on killing an enemy",
        cost=5,
        location={
             "Forgotten Battlefield": "From the Main Gate flag, enter the left trench, then go up the stairs and across the bridge",
             "Renoir's Drafts": "Merchant",
        },
    ),
    Pictos(
        name="Tainted",
        description="15% increased damage for each Status Effect on self",
        cost=3,
        location={
             "Stone Wave Cliffs": "Chromatic Gault",
             "The Reacher": "Merchant",
        },
    ),
    Pictos(
        name="Teamwork",
        description="10% increased damage while all allies are alive",
        cost=5,
        location={
             "Yellow Harvest": "Merchant",
        },
    ),
    Pictos(
        name="The One",
        description="Max Health is reduced to 1",
        cost=1,
        location={
             "Sunless Cliffs": "Mime",
        },
    ),
    Pictos(
        name="Time Tint",
        description="Energy Tints also apply Rush",
        cost=5,
        location={
             "Endless Tower": "Stage 4, Trial 3",
        },
    ),
    Pictos(
        name="Versatile",
        description="After a Free Aim hit, Base Attack damage is increased by 50% for 1 turn",
        cost=5,
        location={
             "Flying Waters": "After Lumieran Streets Expedition Flag, go straight and grapple up twice onto broken houses, then follow the path",
             "Endless Night Sanctuary": "Merchant",
        },
    ),
    Pictos(
        name="Warming Up",
        description="5% increased damage per turn. Can stack up to 5 times",
        cost=15,
        location={
             "The Continent": "Grosse Tete",
        },
    ),
    Pictos(
        name="Weakness Gain",
        description="+1 AP on hitting an enemy's Weakness. Once per turn",
        cost=3,
        location={
             "The Monolith": "From the Tainted Cliffs Expedition Flag, make your way up and grapple across to the cliffs ahead. Continue down this straight path, past the forks in the path. At the end where you are met with a statue, take the right path, head right to find a broken airship",
        },
    ),
]
