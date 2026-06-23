from models import Pictos


pictos = [
    Pictos(
        name="Double Third",
        description="Every third hit of a Skill deals double damage",
        cost=10,
        location={
             "Verso’s Drafts": "Found on the cliff below the first Expedition Flag. Defeat the group of Barbasucette and Machinapieds enemies standing near the cliff edge",
        },
    ),
    Pictos(
        name="SOS Healing Tint",
        description="Consume a Healing Tint when falling below 50% Health",
        cost=10,
        location={
             "Verso's Draft": "Defeat the Franctale enemy patrolling the woods to the left of the Gingerbread Door. Upon victory, you’ll receive the SOS Healing Tint Picto",
        },
    ),
    Pictos(
        name="Damage Share",
        description="50% damage taken is redirected to other allies (if possible)",
        cost=30,
        location={
             "Verso's Draft": "Near the Lake and Gingerbread Door. From the Gestral Baths area, go right toward the stairs near the lake. Two Licorne enemies guard the path to the Gingerbread Door. Defeat both to receive the Damage Share Picto automatically",
        },
    ),
    Pictos(
        name="Empowering Jumps",
        description="Counters deal 100% more damage for each successful Jump Counter this turn",
        cost=5,
        location={
             "Verso's Draft": "Seesaw Area (north of the Twisted Woods). Approach the Half-baked Gestral sitting on the seesaw and interact. Jump with him 4 times to complete the playful side quest. Once finished, he rewards you with the Empowering Jumps Picto. The jump timings are triggered when the Gestral hits the see-saw, not when the indicator appears",
        },
    ),
    Pictos(
        name="Gradient Parry",
        description="+5% of a gradient charge on Parry",
        cost=10,
        location={
             "Verso's Draft": "From the Gestral Baths expedition flag, follow the descending path to an Esquie statue near Hopscotch Tile number 5, where the Picto can be collected from its hand",
        },
    ),
    Pictos(
        name="Slowing Attack",
        description="Base attack applies Slow for 1 turn",
        cost=10,
        location={
             "Verso's Drafts": "Explore the Gestral Baths to the right of the entrance area . Past the second pair of Esquie statues playing in the water, you’ll find the Picto on a glowing ledge",
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
             "Verso's Drafts": "Can be obtained by defeating Monsieur Frappe in Candy Land after successfully parrying his attack three times during the encounter",
        },
    ),
    Pictos(
        name="Gradient Overcharge",
        description="On turn start, consume 3 Gradient Charges (if able) to deal 200% more damage this turn",
        cost=15,
        location={
             "Verso's Draft": "It can be found on a large floating piece of candy near the Candy Land entrance. Reach it by climbing the overhead swing beams in the area",
        },
    ),
    Pictos(
        name="Longer Break",
        description="Breaks last 1 more turn but the target can't be Broken twice",
        cost=10,
        location={
             "Verso’s Drafts": "Found on the cliff below the first Expedition Flag. Defeat the group of Barbasucette and Machinapieds enemies standing near the cliff edge",
        },
    ),
    Pictos(
        name="Alternating Critical",
        description="On Critical hit, 100% increased damage of the next non-Critical hit",
        cost=10,
        location={
             "Verso's Draft": "From the Open Playground expedition flag, take the left fork, enter the cave, then follow the right tunnel to its end to obtain the Picto",
        },
    ),
    Pictos(
        name="Trigger-Happy",
        description="After shooting 10 times in the same turn, gain +2 AP (once). And following Shots this turn deal 200% more damage",
        cost=20,
        location={
             "Verso's Draft": "Can be obtained after defeating Half-Baked Gestral",
        },
    ),
    Pictos(
        name="AP Discount",
        description="Skills cost 1 less AP",
        cost=30,
        location={
             "Verso's Drafts": "Can be purchased from Najabla for 217,000 Chromas",
        },
    ),
    Pictos(
        name="Consuming Attack",
        description="Base attack consumes up to 100 Burns to deal 10% more damage per Burn consumed",
        cost=10,
        location={
             "Verso's Draft": "Available for purchase from Najabla for 130,200 Chromas",
        },
    ),
    Pictos(
        name="Empowered Healer",
        description="Using a Healing Skill gives 50% more damage for 1 turn",
        cost=10,
        location={
             "Verso's Draft": "Continue along the same right path past Gradient Parry until you reach a parkour challenge involving narrow platforms. Successfully completing the sequence rewards the Empowered Healer Picto",
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
             "Verso's Draft": "After defeating the Licornapieds boss near the Licornapieds Station expedition flag",
        },
    ),
    Pictos(
        name="Accelerating Heal",
        description="Healing an ally also applies Rush for 1 turn",
        cost=5,
        location={
             "The Continent": "Can be found in an abandoned expedition camp on an island northeast of Stone Wave Cliffs",
        },
    ),
    Pictos(
        name="Accelerating Last Stand",
        description="Gain Rush if fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Defeat Bertrand Big Hands",
        },
    ),
    Pictos(
        name="Accelerating Shots",
        description="20% chance to gain Rush on Free Aim shot",
        cost=3,
        location={
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Accelerating Tint",
        description="Healing Tints also apply Rush",
        cost=5,
        location={
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 80,040 Chroma",
        },
    ),
    Pictos(
        name="Aegis Revival",
        description="+1 Shield on being revived",
        cost=5,
        location={
             "Spring Meadows": "From the abandoned Expedition Camp Expedition Flag, break through the Paint Spike to the right of Jar. Head down the path and grapple across to the other cliff. Aegis Revival can be found on the right by some boxes and a figure",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
        },
    ),
    Pictos(
        name="Anti-Blight",
        description="Immune to Blight",
        cost=10,
        location={
             "The Continent": "Reward for defeating the Chromatic Portier boss",
             "The Reacher": "Can be purchased from Gestral merchant Eragol for 67,350 chroma",
        },
    ),
    Pictos(
        name="Anti-Burn",
        description="Immune to Burn",
        cost=15,
        location={
             "Frozen Hearts": "Dropped as a reward for defeating the Gargant boss",
             "Flying Manor": "Dropped as a reward for defeating the Gargant boss",
        },
    ),
    Pictos(
        name="Anti-Charm",
        description="Immune to Charm",
        cost=10,
        location={
             "Sirene": "Obtained as a reward for defeating Tisseur in Sirene",
        },
    ),
    Pictos(
        name="Anti-Freeze",
        description="Immune to Freeze",
        cost=15,
        location={
             "Frozen Hearts": "Can be obtained upon destroying the Paint Cage in Glacial Falls past the Manor entrance. Once exiting the cave, the Paint Cage will be on the left",
        },
    ),
    Pictos(
        name="Anti-Stun",
        description="Immune to Stun",
        cost=5,
        location={
             "The Continent": "Dropped upon defeating the Chromatic Petank",
        },
    ),
    Pictos(
        name="At Death's Door",
        description="Deal 50% more damage if Health is below 10%",
        cost=5,
        location={
             "Stone Wave Cliffs": "Defeat the Lampmaster",
             "Painting Workshop": "Defeat the Lampmaster",
        },
    ),
    Pictos(
        name="Attack Lifesteal",
        description="Recover 15% Health on Base Attack",
        cost=15,
        location={
             "Ancient Sanctuary": "From the Sanctuary Maze Expedition Flag, hug the right wall until you crouch to enter an area. Take a right and go straight until you enter a dark cave. The Pictos will be shortly to the left from the beginning of the cave",
        },
    ),
    Pictos(
        name="Augmented Aim",
        description="50% increased Free Aim damage",
        cost=3,
        location={
             "Flying Waters": "Shortly after the Noco's Hut Expedition Flag, the Pictos can be found atop the giant anchor in Flying Waters, accessible via a climbable pillar behind the anchor (with grapple points to reach the anchor)",
        },
    ),
    Pictos(
        name="Augmented Attack",
        description="50% increased Base Attack damage",
        cost=7,
        location={
             "Spring Meadows": "Dropped upon defeating the Chromatic Lancelier past the Grand Meadow Expedition Flag",
        },
    ),
    Pictos(
        name="Augmented Counter I",
        description="25% increased Counterattack damage",
        cost=3,
        location={
             "Flying Waters": "Defeat the Bourgeon",
             "Flying Manor": "Defeat the Bourgeon near the Eveque Boss",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
        },
    ),
    Pictos(
        name="Augmented Counter II",
        description="50% increased Counterattack damage",
        cost=5,
        location={
             "Visages": "Defeat the Chromatic Ramasseur at the Sad Vale on the left side to receive the Augmented Counter II Pictos",
        },
    ),
    Pictos(
        name="Augmented Counter III",
        description="75% increased Counterattack damage",
        cost=7,
        location={
             "Lumiere": "Defeat the Chromatic Echassier in the Shattered Alley section to receive the Augmented Counter III as a drop",
             "Frozen Hearts": "Defeat the Danseuse Teacher after passing her parry test to receive Augmented Counter III as a drop",
        },
    ),
    Pictos(
        name="Augmented First Strike",
        description="50% increased damage on the first hit. Once per battle",
        cost=5,
        location={
             "Esquie's Nest": "Defeat Francois",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour. Fight the merchant to reveal this item in its shop",
        },
    ),
    Pictos(
        name="Auto Death",
        description="Kill self on battle start",
        cost=1,
        location={
             "Yellow Harvest": "Can be purchased from the Merchant Pinabby for 5,320 Chroma",
        },
    ),
    Pictos(
        name="Auto Powerful",
        description="Apply Powerful for 3 turns on battle start",
        cost=10,
        location={
             "Floating Cemetery": "The Chalier NPC will reward you with this Picto upon agreeing to end its life",
        },
    ),
    Pictos(
        name="Auto Regen",
        description="Apply Regen for 3 turns on battle start",
        cost=10,
        location={
             "Sirene": "After taking the platform at the end of the path from the Dancing Classes Expedition Flag, head into the path on the right, and follow the ribbon on the right side going down to fight a Benisseur, you can pick up Auto Regen on the side",
        },
    ),
    Pictos(
        name="Auto Rush",
        description="Apply Rush for 3 turns on battle start",
        cost=10,
        location={
             "Old Lumiere": "From the Left Street Expedition Flag, follow the main path until you ecounter the broken bridge which you must grapple across. Immediately after is an archway on the left, take out the enemies and pick up Auto Rush",
        },
    ),
    Pictos(
        name="Auto Shell",
        description="Apply Shell for 3 turns on battle start",
        cost=10,
        location={
             "Stone Wave Cliffs": "Help the fallen Hexga obtain 3 Rock Crystals in the Cavern, return it to him and you will be able to pick it up from the crater that it used to lay in",
        },
    ),
    Pictos(
        name="Base Shield",
        description="+1 Shield if not affected by any Shield on turn start",
        cost=20,
        location={
             "The Chosen Path": "Complete all the challenges to unlock the door in this location. You'll find this inside the locked room, next to a mirror",
        },
    ),
    Pictos(
        name="Beneficial Contamination",
        description="+2 AP on applying a Status Effect. Once per turn",
        cost=15,
        location={
             "Falling Leaves": "Can be purchased from Persik for 48,200 Chroma",
        },
    ),
    Pictos(
        name="Break Specialist",
        description="Break damage is increased by 50%, but base damage is reduced by 20%",
        cost=1,
        location={
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Breaker",
        description="25% increased Break damage",
        cost=10,
        location={
             "Ancient Sanctuary": "Obtained as a drop from the Ultimate Sakapatate",
        },
    ),
    Pictos(
        name="Breaking Attack",
        description="Base Attack can Break",
        cost=10,
        location={
             "The Monolith": "Dropped upon defeating the boss Clair Obscur in the Tainted Lumiere section, best accessed by backtracking from the Tower Peak Expedition Flag",
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
             "Stone Wave Cliffs": "After defeating the Hexga after the Entrance Expedition Flag, go into the leftmost jar structure to find this Pictos",
        },
    ),
    Pictos(
        name="Breaking Death",
        description="Fully charge enemy's Break Bar on death",
        cost=5,
        location={
             "The Continent": "Acquired as a drop reward for defeating the Thunder Eveque",
        },
    ),
    Pictos(
        name="Breaking Shots",
        description="50% increased Break damage with Free Aim Shots",
        cost=1,
        location={
             "Stone Wave Cliffs": "From the Basalt Waves Expedition Flag, turn back and head down the rope. Cross the grapple point and follow the left wall to some pillar parkour with the Pictos on the far side",
        },
    ),
    Pictos(
        name="Breaking Slow",
        description="25% increased Break damage against Slowed enemies",
        cost=5,
        location={
             "The Continent": "Requires the ability to destroy Paint Spikes & Esquie's ability to fly. Found inside a Paint Spike a little northwest of Spring Meadows",
        },
    ),
    Pictos(
        name="Burn Affinity",
        description="25% increased damage on Burning Targets",
        cost=10,
        location={
             "Frozen Hearts": "From the Glacial Falls Expedition Flag, continue along the path to the right, take the rope up, and head to the end to grapple across to the cliff ahead. At the end of this path, there are broken tracks and wall structures on them. Climb up the structure towards the right, turn around and grapple to the floating train. Take the rope down to pick up Burn Affinity on another train",
        },
    ),
    Pictos(
        name="Burning Break",
        description="Apply 3 Burn stacks on Breaking a target",
        cost=3,
        location={
             "Frozen Hearts": "Can be found on top of a structure in the left side of the field in the first area of the Glacial Falls. Head up the slope on the left and hop across to the structure to pick it up",
        },
    ),
    Pictos(
        name="Burning Death",
        description="Apply 3 Burn to all enemies on Death",
        cost=5,
        location={
             "Frozen Hearts": "From the Glacial Falls Expedition Flag, continue down the path to the right. Atop the rope, there are 2 Danseuses and a Pelerin, which give it on death",
             "Flying Manor": "Drops from the Gargant boss",
        },
    ),
    Pictos(
        name="Burning Mark",
        description="Apply Burn on hitting a Marked enemy",
        cost=15,
        location={
             "Ancient Sanctuary": "From the Entrance Expedition Flag, run towards the large Gestral structure in the distance and follow the stream on the left. Next to the main path will be a slope leading down. Will be on a ledge after a short climb",
        },
    ),
    Pictos(
        name="Burning Shots",
        description="20% chance to Burn on Free Aim shot",
        cost=3,
        location={
             "Spring Meadows": "Found sitting on the cliff on the left upon exiting the short tunnel past the Abandoned Expedition Camp Expedition Flag",
             "Sacred River": "Sold by the Gestral Merchant after defeating him in a duel",
             "Monoco's Station": "Sold by the Grandis Merchant after completing the Eternal Ice quest",
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
             "Renoir's Drafts": "On the bridge behind the Gestral Merchant Grour",
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
             "Endless Tower": "Rewarded for completing Stage 5, Trial 3",
             "Renoir's Drafts": "From the the Golden Tree Expedition Flag, head backwards and grapple to the roof with Merchant Grour. Jump across the platforms on the right to pick up a Pictos upgrade for Charging Critical",
        },
    ),
    Pictos(
        name="Charging Mark",
        description="20% of a Gradient Charge on hitting a Marked target. Once per turn",
        cost=10,
        location={
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 100,050 Chroma",
        },
    ),
    Pictos(
        name="Charging Stun",
        description="+5% of a Gradient Charge on hitting a Stunned enemy",
        cost=5,
        location={
             "Lumiere": "As you go through the Central Plaza, you can find a Young Boy along the path. Go behind the tree in the middle of the area right before the Shattered Alley Expedition Flag to find the Charging Stun Pictos",
        },
    ),
    Pictos(
        name="Charging Tint",
        description="+5% of a Gradient Charge on using an item",
        cost=2,
        location={
             "The Continent": "The Charging Tint Pictos can be found on a small patch of land southeast of the Gestral Beach south of Old Lumiere on the world map, near a Stalact",
        },
    ),
    Pictos(
        name="Charging Weakness",
        description="+15% of a Gradient Charge on hitting a Weakness. Once per turn",
        cost=5,
        location={
             "The Reacher": "Can be purchased from Eragol for 53,880 Chroma",
        },
    ),
    Pictos(
        name="Cheater",
        description="Always play twice in a row",
        cost=40,
        location={
             "The Continent": "Acquired as a reward for defeating Sprong. Requires Esquie's fly or swim ability to reach the boss",
        },
    ),
    Pictos(
        name="Cleansing Tint",
        description="Healing Tints also remove all Status Effects from the target",
        cost=5,
        location={
             "Spring Meadows": "Dropped upon defeating Eveque just after The Blue Tree Expedition Flag",
        },
    ),
    Pictos(
        name="Clea's Life",
        description="On turn start, if no damage taken since last turn, recover 100% Health",
        cost=30,
        location={
             "Flying Manor": "Obtained as a reward for defeating Clea",
        },
    ),
    Pictos(
        name="Combo Attack I",
        description="Base Attack has 1 extra hit",
        cost=10,
        location={
             "Forgotten Battlefield": "Obtained as a drop by defeating Dualliste",
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
             "Dark Gestral Arena": "Win all three challenges to obtain this as a reward",
        },
    ),
    Pictos(
        name="Confident",
        description="Take 50% less damage, but can't be Healed",
        cost=20,
        location={
             "Stone Wave Cliffs": "Dropped from the Hexga past the Entrance Expedition Flag",
             "The Continent": "Requires Esquie's swim ability. Found in an abandoned expedition camp on an island northeast of the Stone Wave Cliffs",
        },
    ),
    Pictos(
        name="Confident Fighter",
        description="30% increased damage, but can't be Healed",
        cost=15,
        location={
             "Visages": "In the Joyful Vale area, head up the ramp near the mask on the right side, then defeat the Boucheclier by the ledge. After the area is clear, proceed to the area on the right to find the Confident Fighter Pictos",
        },
    ),
    Pictos(
        name="Critical Break",
        description="25% increased Break damage on Critical Hits",
        cost=5,
        location={
             "The Continent": "Requires the ability to destroy Paint Spikes. The Critical Break Pictos can be found inside a Paint Spike on a small beach to the west of the Isle of the Eyes. ",
        },
    ),
    Pictos(
        name="Critical Burn",
        description="25% increased Critical Chance on Burning enemies",
        cost=5,
        location={
             "Spring Meadows": "Found at the end of the path to the right, right after taking out the first wave of Lancelier enemies past the Meadows Corridor Expedition Flag",
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 100,050 Chroma. Fight the merchant to reveal this item in its shop",
        },
    ),
    Pictos(
        name="Critical Moment",
        description="50% increased Critical Chance if Health is below 30%",
        cost=5,
        location={
             "Gestral Village": "Can be purchased from Jujubree for 5,520 Chroma",
        },
    ),
    Pictos(
        name="Critical Stun",
        description="100% on Critical Chance on hitting a Stunned target",
        cost=5,
        location={
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 53,880 Chroma",
        },
    ),
    Pictos(
        name="Critical Vulnerability",
        description="25% increased Critical Chance on Defenceless enemies",
        cost=5,
        location={
             "The Continent": "The Critical Vulnerability Pictos can be found by a camp surrounded by enemies in an alcove to the northwest of Falling Leaves",
        },
    ),
    Pictos(
        name="Critical Weakness",
        description="25% increased Critical Chance on Weakness",
        cost=5,
        location={
             "Endless Tower": "Rewarded for completing Stage 6, Trial 3",
        },
    ),
    Pictos(
        name="Dead Energy I",
        description="+3 AP on killing an enemy",
        cost=2,
        location={
             "The Continent": "Found on the southern part of the beach that contains the entrance to Dark Shores, there is a cluster of crates you can break apart containing the Picto",
        },
    ),
    Pictos(
        name="Dead Energy II",
        description="+3 AP on killing an enemy",
        cost=2,
        location={
             "Spring Meadows": "Found on a ledge at the end of the path directly to the right upon exiting the short tunnel past the Abandoned Expedition Camp Expedition Flag",
        },
    ),
    Pictos(
        name="Death Bomb",
        description="On Death, deal damage to all enemies",
        cost=5,
        location={
             "Yellow Harvest": "From the Harvester's Hollow Expedition Flag, head down the path and go towards the slope on the right. To the right of that slope, you can pick up Death Bomb",
        },
    ),
    Pictos(
        name="Defensive Mode",
        description="On receiving damage, consume 1 AP to take 30% less damage, if possible",
        cost=1,
        location={
             "Stone Wave Cliffs": "After unlocking Esquie's swim ability, enter Stone Wave Cliffs from the beach portal and directly to the left, you can pick up Defensive Mode",
        },
    ),
    Pictos(
        name="Dodger",
        description="Gain 1 AP on Perfect Dodge. Once per turn",
        cost=1,
        location={
             "Spring Meadows": "Obtained upon defeating the Portier inside the cave after Lune finds you",
        },
    ),
    Pictos(
        name="Double Burn",
        description="On applying a Burn stack, apply a second one",
        cost=30,
        location={
             "Visages": "In the Anger Vale area, you can find a cavern on the right side. Enter it, then follow the left path to find a Moissonneuse with two Bouchecliers. Defeat the enemies, then pick up the Double Burn Pictos beside the remains of a human",
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 112,250 Chroma",
        },
    ),
    Pictos(
        name="Double Mark",
        description="Mark requires 1 more hit to be removed",
        cost=20,
        location={
             "Sirene": "Can be purchased from Klaudiso for 42,400 Chroma",
        },
    ),
    Pictos(
        name="Draining Cleanse",
        description="Consume 1 AP to prevent Status Effects application, if possible",
        cost=15,
        location={
             "The Reacher": "From the Entrance Expedition Flag, grapple across to the next tower, continue ahead, and grapple onto the next tower. Proceed ahead and take the rope down. From there, take the path on the right, defeat the Orphelin and pick up the Draining Cleanse",
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
             "The Continent": "The Pictos can be found on the ground in a small patch of grassy land northeast of Sirene on the world map",
        },
    ),
    Pictos(
        name="Empowering Attack",
        description="Gain Powerful for 1 turn on Base Attack",
        cost=10,
        location={
             "Spring Meadows": "Found after defeating Eveque, it is found on an exposes branch near the boss area and near the exit to Spring Meadows",
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 67,350 Chroma",
        },
    ),
    Pictos(
        name="Empowering Break",
        description="Gain Powerful on Breaking a target",
        cost=3,
        location={
             "Flying Manor": "Can be found in the area where you fight Goblu (up the elevator). When you enter, hug the left wall until there's a chroma rope you can zip down. Across the grapple point, you'll see a Cruler enemy roaming around and blocking the path where the item is",
        },
    ),
    Pictos(
        name="Empowering Dodge",
        description="5% increased damage for each consecutive successful Dodge. Can stack up to 10 times",
        cost=5,
        location={
             "The Continent": "A little north of the Endless Night Sanctuary in an abandoned camp in the top left corner. Right across from 3 enemies. (Moissonneuse, Benisseur, Glaise)",
        },
    ),
    Pictos(
        name="Empowering Last Stand",
        description="Gain Powerful if fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Defeat Julien Tiny Head",
        },
    ),
    Pictos(
        name="Empowering Parry",
        description="Each successful Parry increases damage by 5% until end of the following turn. Taking any damage removes this buff",
        cost=5,
        location={
             "The Monolith": "Found in a Paint Cage in the Tainted Hearts area",
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Empowering Tint",
        description="Healing Tints also apply Powerful",
        cost=5,
        location={
             "Forgotten Battlefield": "From the Battlefield Expedition Flag, head through the trenches on the right side of the Fading Woman, then follow the path on the right side. Climb the rope, and you will find the Empowering Tint Pictos across the wooden path",
             "Endless Tower": "Stage 8, Trial 3",
        },
    ),
    Pictos(
        name="Energetic Healer",
        description="+2AP on Healing an ally. Once per turn",
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
             "Yellow Harvest": "Defeat the Glaise in the Yellow Spire Wrecks section",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
             "Painting Workshop": "Defeat the Lampmaster",
        },
    ),
    Pictos(
        name="Energising Attack II",
        description="+1 AP on Base Attack",
        cost=15,
        location={
             "Sirene": "Can be purchased from Klaudiso for 37,100 Chroma",
        },
    ),
    Pictos(
        name="Energising Break",
        description="+3 AP on Breaking a target",
        cost=3,
        location={
             "Flying Waters": "From the Lumièran Streets Expedition Flag, climb the wall on the left and continue down this path. It will be behind the Chromatic Troubadour",
        },
    ),
    Pictos(
        name="Energising Burn",
        description="+1 AP on applying Burn. Once per turn",
        cost=10,
        location={
             "Frozen Hearts": "Can be obtained by defeating the Chromatic Veilleur",
        },
    ),
    Pictos(
        name="Energising Cleanse",
        description="Dispel the first negative Status Effect received an gain 2 AP",
        cost=10,
        location={
             "The Monolith": "Can be unlocked from Mistra's secret wares by challenging him to a duel, it will be sold for 40,800 Chroma",
        },
    ),
    Pictos(
        name="Energising Death",
        description="On death, +4 AP to allies",
        cost=5,
        location={
             "Forgotten Battlefield": "In the Fort Ruins section, head inside the structure to find a Chalier. Defeat it, then head to the ledge it was blocking to find the Energising Death Pictos",
             "Monoco's Station": "Sold by the Grandis Merchant after completing the Eternal Ice Quest",
        },
    ),
    Pictos(
        name="Energising Gradient",
        description="+1 AP per Gradient Charge consumed",
        cost=10,
        location={
             "The Continent": "Acquired as a drop reward for defeating the Frost Eveque",
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
             "Ancient Sanctuary": "Can be found on the left side of the starting area",
        },
    ),
    Pictos(
        name="Energising Pain",
        description="No longer gain AP on Parry. +1AP on getting hit",
        cost=10,
        location={
             "Stone Wave Cliffs": "Follow the main path all the way to the destroyed airship. Go through the tunnel that was left by the remnants of the airship, then cross the platform to reach the other side. Stay on this path until you encounter a duo of a Greatsword Cultist and Reaper Cultist near the bridge. Defeat them to get Energising Pain",
             "Flying Manor": "From the Central Plaza, go through the arch on the right and use the lift to get to the bottom level. Defeat the Greatsword Cultist standing on the structure on the left side of the area to receive Energising Pain",
             "The Continent": "Requires Esquie's destroy coral reef ability. West of the Isle of the Eyes, there is a small shore. Defeat the Greatsword Cultist there to obtain it",
             "The Monolith": "Dropped from the two Greatsword Cultists past the Tainted Cliffs Expedition Flag",
        },
    ),
    Pictos(
        name="Energising Parry",
        description="+1 AP on successful Parry",
        cost=15,
        location={
             "Forgotten Battlefield": "Defeat the Chromatic Luster Boss",
             "Sacred River": "Sold by the Gestral Merchant after defeating him in a duel",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
        },
    ),
    Pictos(
        name="Energising Powerful",
        description="Give 2 AP on applying Powerful",
        cost=10,
        location={
             "Lumiere": "At the Harbour section, once you get to the rooftop section, follow the path on the right until you reach the spot where you started in the Prologue. Inside the trellis area, you can find the Energising Powerful Pictos",
        },
    ),
    Pictos(
        name="Energising Revive",
        description="+3 AP to all allies when revived",
        cost=5,
        location={
             "Stone Wave Cliffs Cave": "Defeat the Chromatic Hexga to obtain the Energising Revive",
        },
    ),
    Pictos(
        name="Energising Rush",
        description="Give 2 AP on applying Rush",
        cost=10,
        location={
             "Endless Tower": "Rewarded for completing Stage 2, Trial 3",
        },
    ),
    Pictos(
        name="Energising Shell",
        description="Give 2 AP on applying Shell",
        cost=10,
        location={
             "The Continent": "Requires the ability to destroy Paint Spikes. The Pictos can be found in a paint spike in the area of the Chromatic Petank to the east of The Meadows on the world map",
        },
    ),
    Pictos(
        name="Energising Shots",
        description="20% chance to gain 1 AP on Free Aim shot",
        cost=10,
        location={
             "Flying Manor": "Found on the left side of Goblu's arena",
        },
    ),
    Pictos(
        name="Energising Start I",
        description="+1 AP on battle start",
        cost=5,
        location={
             "The Continent": "Can be found on the right side of the beach behind the Gestral Village",
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
             "Esquie's Nest": "After Esquie joins your party, cross the pillar and use your grappling hook to get across the second gap as well. Continue straight down the path to find this Pictos on the edge of the ledge",
        },
    ),
    Pictos(
        name="Energising Start IV",
        description="+1 AP on battle start",
        cost=20,
        location={
             "Forgotten Battlefield": "From the Main Gate Expedition Flag, stick to the right. After fighting a Troubadour positioned near a door that cannot be interacted with, follow the nearby path to find a trench containing the Energising Start IV",
        },
    ),
    Pictos(
        name="Energising Stun",
        description="+1 AP on hitting a Stunned target with a Skill",
        cost=10,
        location={
             "Flying Manor": "Requires the ability to destroy Paint Spikes. Can be obtained from a Paint Cage on the left side of the Eveque bosses' area",
        },
    ),
    Pictos(
        name="Energising Turn",
        description="+1 AP on turn start",
        cost=20,
        location={
             "Sirene": "Defeat Sirene (Boss)",
             "Sacred River": "Sold by the Gestral Merchant after defeating him in a duel",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
        },
    ),
    Pictos(
        name="Energy Master",
        description="Every AP gain is increased by 1",
        cost=40,
        location={
             "The Continent": "Acquired as a reward for defeating Serpenphare",
        },
    ),
    Pictos(
        name="Enfeebling Attack",
        description="Base Attack applies Powerless for 1 turn",
        cost=10,
        location={
             "The Monolith": "Can be found by a corpse next to a train near the Merchant Melosh in the Tainted Hearts section",
        },
    ),
    Pictos(
        name="Enfeebling Mark",
        description="Marked targets deal 30% less damage",
        cost=10,
        location={
             "Stone Wave Cliffs": "From the Flooded Buildings Expedition Flag, head down the path past the Rocher. A short ways down, enter the building to your left. Head up and exit to the open area, and grapple to the cliffs to the right to find Enfeebling Mark",
        },
    ),
    Pictos(
        name="Exhausting Power",
        description="50% increased damage if Exhausted",
        cost=2,
        location={
             "Stone Wave Cliffs Cave": "Can be found in the left side of the arena where the Chromatic Hexga is located",
        },
    ),
    Pictos(
        name="Exposing Attack",
        description="Base Attack applies Defenceless for 1 turn",
        cost=10,
        location={
             "Flying Waters": "Sold by Merchant Noco for 3,600 Chroma after defeating him in a duel",
        },
    ),
    Pictos(
        name="Exposing Break",
        description="Apply Defenceless on Break",
        cost=5,
        location={
             "The Reacher": "Can be purchased from Eragol for 53,880 Chroma",
        },
    ),
    Pictos(
        name="Faster Than Strong",
        description="Always play twice in a row, but deal 50% less damage",
        cost=10,
        location={
             "Lumiere": "Defeat the Creation in Lumiere's Garden to receive the Faster Than Strong Pictos",
        },
    ),
    Pictos(
        name="First Offensive",
        description="First hit dealt and taken deals 50% more damage",
        cost=5,
        location={
             "Abbest Cave": "Can be obtained as a reward upon defeating the Chromatic Abbest",
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
             "Endless Tower": "Reward for completing Stage 7, Trial 3",
        },
    ),
    Pictos(
        name="Full Strength",
        description="25% increased damage on full Health",
        cost=15,
        location={
             "Lumiere": "sold by Cribappa for 53,200 Chroma after challenging him to a duel and winning",
        },
    ),
    Pictos(
        name="Glass Cannon",
        description="Deal 25% more damage, but take 25% more damage",
        cost=10,
        location={
             "Visages": "After reaching the Chromatic Ramasseur, look on the right, pick up the Glass Cannon Pictos near a figure with garlands. Fighting the Ramasseur is NOT required as the pictos is off to the side of its spawn",
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 67,350 Chroma",
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
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Gradient Fighter",
        description="+25% increased damage with Gradient Attacks",
        cost=5,
        location={
             "Lumiere": "In Lumiere's Garden, follow the path on the left to find a loot beam. Approach it, and two Aberrations will spawn — defeat them, then pick up the Gradient Fighter Pictos",
        },
    ),
    Pictos(
        name="Greater Defenceless",
        description="+15% to Defenceless damage amplification",
        cost=15,
        location={
             "The Monolith": "Challenge Melosh the Merchant to a duel, win to unlock Greater Defenceless for 47,600 Chroma",
             "Endless Tower": "Drops or provides an upgrade for completing Stage 1, Trial 3",
        },
    ),
    Pictos(
        name="Greater Powerful",
        description="+15% to Powerful damage increase",
        cost=10,
        location={
             "Sirene": "Can be purchased from Klaudiso for 37,100 Chroma",
        },
    ),
    Pictos(
        name="Greater Powerless",
        description="+15% to Powerless damage reduction",
        cost=15,
        location={
             "Endless Tower": "Rewarded for completing Stage 10, Trial 3",
        },
    ),
    Pictos(
        name="Greater Rush",
        description="+25% Rush Speed increase",
        cost=10,
        location={
             "Monoco's Station": "Sold by the Grandis Merchant after completing the Eternal Ice Quest",
        },
    ),
    Pictos(
        name="Greater Shell",
        description="+10% to Shell damage reduction",
        cost=10,
        location={
             "Sirene": "From the Dancing Classes Expedition Flag, head straight ahead until you can turn left under an arch. Follow the path left, across the gap and down to another moving platform. After taking the podium down, turn right at the path and head to the end to pick up Greater Shell",
        },
    ),
    Pictos(
        name="Greater Slow",
        description="+15% to Slow Speed reduction",
        cost=15,
        location={
             "Sky Island": "Requires Esquie's fly ability to reach the location. You'll find it on a broken set of stairs past the Chromatic Glaise boss",
        },
    ),
    Pictos(
        name="Healing Boon",
        description="Heal 15% HP on applying a buff",
        cost=10,
        location={
             "The Reacher": "Can be found on the unreachable ledge in the Ladder Area. Players will need to take the hot air balloon from the Foggy Area located near Eragol the merchant",
        },
    ),
    Pictos(
        name="Healing Counter",
        description="Recover 25% Health on Counterattack",
        cost=10,
        location={
             "Old Lumiere": "Can be purchased from the Merchant Mandelgo for 20,400 Chroma",
        },
    ),
    Pictos(
        name="Healing Death",
        description="On death, the rest of the Expedition recover all Health",
        cost=5,
        location={
             "Old Lumiere": "Obtainable only after fighting Renoir. From the Manor Gardens Expedition Flag, head to the right (away from the Manor) to find a new path. Go all the way to the end, and grapple across several cliffs until you grapple up a building on a cliff. Climb up the wall structures and pick up Healing Death at the end of the path",
        },
    ),
    Pictos(
        name="Healing Fire",
        description="Recover 25% Health when attacking a Burning target. Once per turn",
        cost=10,
        location={
             "Sirene": "From the Crumbling Path Expedition Flag, turn to the right and up the ramp. Go to the edge and take the rope down. Continue down this path and grapple across. Go through the crawl space to find Healing Fire by a corpse",
        },
    ),
    Pictos(
        name="Healing Mark",
        description="Recover 25% Health on hitting a Marked enemy. Once per turn",
        cost=20,
        location={
             "Gestral Village": "can be purchased from Eesda for 9,200 Chroma after defeating him to gain access to his shop",
        },
    ),
    Pictos(
        name="Healing Parry",
        description="Recover 3% Health on Parry",
        cost=5,
        location={
             "The Continent": "Can be found at a camp behind the Bourgeon after defeating it",
        },
    ),
    Pictos(
        name="Healing Share",
        description="Receive 15% of all Heals affecting other characters",
        cost=5,
        location={
             "Visages": "Healing Share can be purchased from Blooraga for 19,200 Chroma",
        },
    ),
    Pictos(
        name="Healing Stun",
        description="Recover 5% Health on hitting a Stunned target",
        cost=10,
        location={
             "Lumiere": "After exiting the Opera House, grapple across until you encounter an Aberration and a Ballet. Defeat the enemies, then pick up the Healing Stun Pictos",
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
             "Visages": "Can be obtained after defeating the Mask Keeper",
        },
    ),
    Pictos(
        name="In Medias Res",
        description="+3 Shields on Battle Start, but max Health is halved",
        cost=10,
        location={
             "Dark Shores": "Requires Esquie's swim ability. Guarded by 2 Noir furthest from the entrance, either kill them or kite them away before running back and grabbing the Pictos off the ground. ",
        },
    ),
    Pictos(
        name="Inverted Affinity",
        description="Apply Inverted on self for 3 turns on battle start. 50% increased damage while Inverted",
        cost=5,
        location={
             "Forgotten Battlefield": "Sold by Kasumi for 9,870 Chroma, a merchant at the top of a structure accessed by a rope in the Battlefield section",
        },
    ),
    Pictos(
        name="Last Stand Critical",
        description="100% Critical Chance while fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Defeat Matthieu the Colossus",
        },
    ),
    Pictos(
        name="Longer Burn",
        description="Burn duration is increased by 2",
        cost=15,
        location={
             "The Continent": "Defeat the Chromatic Aberration boss",
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Longer Powerful",
        description="On applying Powerful, its duration is increased by 2",
        cost=10,
        location={
             "Old Lumiere": "Can be purchased from the Merchant Mandelgo for 20,400 Chroma",
        },
    ),
    Pictos(
        name="Longer Rush",
        description="On applying Rush, its duration is increased by 2",
        cost=10,
        location={
             "The Continent": "Requires Esquie's fly ability to reach the location. located on the southern tip of the valley shown on the interactive map",
        },
    ),
    Pictos(
        name="Longer Shell",
        description="On applying Shell, its duration is increased by 2",
        cost=10,
        location={
             "Forgotten Battlefield": "Dropped by a Chalier positioned near a fork in the path at the start",
             "The Reacher": "From the Mountain Expedition Flag, continue ahead and grapple across to the mountain. Take the path up on the right to find a little course to go through. Carefully make your way across to the other side and pick up Longer Shell",
             "The Continent": "Dropped by a group of enemies consisting of a Rocher, a Bouchelier, and a Chalier at the yellow forest northeast of The Carousel",
             "The Monolith": "Dropped by Nevrons near Tainted Battlefield Expedition Flag",
        },
    ),
    Pictos(
        name="Marking Break",
        description=" Apply Mark on Break",
        cost=5,
        location={
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 80,040 Chroma. Fight the merchant to reveal this item in its shop",
        },
    ),
    Pictos(
        name="Marking Shots",
        description="20% chance to apply Mark on Free Aim shot",
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
             "The Monolith": "Obtained as a reward for defeating The Paintress. Cannot be missed",
        },
    ),
    Pictos(
        name="Painter",
        description="Convert all Physical damage to Void damage",
        cost=10,
        location={
             "Flying Manor": "In the area where the Eveque boss is, head up the stairs to the Everque's left, grapple across, and jump to reach the opposite end. You'll find the body of an expeditioner lying on the platform. The pictos is just beside the body",
        },
    ),
    Pictos(
        name="Perilous Parry",
        description="+1 AP on Parry, but damage received is doubled",
        cost=5,
        location={
             "Stone Wave Cliffs": "Defeat the Gold Chevaliere in the second lower level, it will drop Perilous Parry as a reward",
        },
    ),
    Pictos(
        name="Piercing Shot",
        description="25% increased Free Aim damage. Free Aim shots ignore Shields",
        cost=2,
        location={
             "Ancient Sanctuary": "Requires the ability to destroy Paint Spikes. From the Sanctuary Maze Expedition Flag, head forward and hug the left wall until you reach a Paint Spike. Past the paint spike, head down to the Gestral Totem Expedition Flag area. Behind the totem, you can find a narrow path in the water — enter the path, then take the right to find the Piercing Shot Pictos",
        },
    ),
    Pictos(
        name="Powered Attack",
        description="On every damage dealt, try to consume 1 AP. If successful, increase damage by 20%",
        cost=10,
        location={
             "Visages": "In Anger Vale, head to the path on the left then go down the rope beyond the group of Bouchecliers. At the bottom, you can find the Powered Attack Pictos near a Contorsionniste",
        },
    ),
    Pictos(
        name="Powerful Heal",
        description="Healing an ally also applies Powerful for 1 turn",
        cost=5,
        location={
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 80,040 Chroma",
        },
    ),
    Pictos(
        name="Powerful Mark",
        description="Gain Powerful on hitting a Marked enemy",
        cost=5,
        location={
             "Flying Manor": "Found in the path to Goblu. This is the path where you take the lift up. It will be on top of a structure guarded by two Steel Chevalieres. Head straight across at the primary intersection, turn right at the end and look for a climbable wall before the grapple point",
        },
    ),
    Pictos(
        name="Powerful on Shell",
        description="Apply Powerful on applying Shell",
        cost=10,
        location={
             "Sirene": "After taking the platform at the end of the path from the Dancing Classes Expedition Flag, head into the path on the right, and follow the ribbon on the right side going down to fight a Benisseur. Defeat it to obtain Powerful on Shell",
             "The Continent": "A little north of the Endless Night Sanctuary in an abandoned camp in the top left corner. Defeat the 3 enemies (Moissonneuse, Benisseur, Glaise) to automatically collect the Pictos",
        },
    ),
    Pictos(
        name="Powerful Revive",
        description="Apply Powerful for 3 turns when revived",
        cost=3,
        location={
             "The Continent": "Defeat the Chromatic Bruler by the beach behind the Gestral Village to obtain as loot",
             "Flying Manor": "Can be picked up after opening the Paint Cage in an area behind Dualliste reached by grappling",
        },
    ),
    Pictos(
        name="Powerful Shield",
        description="10% increased damage per Shield Point on self",
        cost=5,
        location={
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 80,040 Chroma",
        },
    ),
    Pictos(
        name="Powerful Shots",
        description="20% chance to gain Powerful on Free Aim shot",
        cost=3,
        location={
             "Gestral Village": "Can be found inside a room blocked by a Paint Spike across from the Gestral Doctor",
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
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 100,050 Chroma",
        },
    ),
    Pictos(
        name="Protecting Death",
        description="On death, allies gain Shell",
        cost=5,
        location={
             "Sirene": "From the Sewing Atelier Expedition Flag, head backwards, up the rope and across the 2 grapple points. Protecting Death will be directly to the left, guarded by 2 Ballets and a Benisseur",
        },
    ),
    Pictos(
        name="Protecting Heal",
        description="Healing an ally also applies Shell for 1 turn",
        cost=5,
        location={
             "The Reacher": "Can be purchased from Eragol for 53,880 Chroma",
             "Esoteric Ruins": "Obtained as a reward for helping the Friendly Portier",
        },
    ),
    Pictos(
        name="Protecting Last Stand",
        description="Gain Shell if fighting alone",
        cost=3,
        location={
             "Hidden Gestral Arena": "Defeat Dominique Giant Feet",
        },
    ),
    Pictos(
        name="Protecting Shots",
        description="20% chance to gain Shell on Free Aim shot",
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
             "The Reacher": "From the Foggy Area Expedition Flag, cross the bridges down to the field, before heading into the field, make a U-turn to the right. Cross the plank and pick up Protecting Tint",
        },
    ),
    Pictos(
        name="Quick Break",
        description="Play again on Breaking a target",
        cost=3,
        location={
             "Endless Night Sanctuary": "Drops from the Chromatic Cruler boss. You can find the boss in the Night Totem area of the location",
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
             "Red Woods": "By paying a total of 90,000 Chroma to the suspicious salver, the friendly Benisseur will reveal itself and will reward you with this Pictos",
        },
    ),
    Pictos(
        name="Rejuvenating Revive",
        description="Apply Regen for 3 turns when revived",
        cost=3,
        location={
             "Stone Wave Cliffs": "Requires the ability to destroy Paint Spikes. Chromatic Gault",
        },
    ),
    Pictos(
        name="Revive Paradox",
        description="Play immediately when revived",
        cost=5,
        location={
             "Old Lumiere": "Drops from the Chromatic Danseuse upon defeating it",
        },
    ),
    Pictos(
        name="Revive Tint Energy",
        description="Revive Tints also give 3 AP",
        cost=10,
        location={
             "Forgotten Battlefield": "After defeating Dualliste, climb up the ropes to find a narrow path between rocks to find the Revive Tint Energy Pictos hidden behind trees",
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 67,350 Chroma",
        },
    ),
    Pictos(
        name="Rewarding Mark",
        description="+2 AP on dealing damage to a Marked target. Once per turn",
        cost=5,
        location={
             "Flying Waters": "Found at the end of the path to the left past the Cruler after the Coral Cave Expedition Flag",
             "Sacred River": "Fight and win the Gestral Merchant to unlock this item for 53,880 Chroma",
        },
    ),
    Pictos(
        name="Roulette",
        description="Every hit has a 50% chance to deal either 50% or 200% of its damage",
        cost=5,
        location={
             "Gestral Village": "Can be found in the Gestras Casino near the arena. Interact with a door to talk to a Gestral Gambler, then choose the dialogue option 'I don't care.' to receive the Roulette Pictos",
             "Flying Manor": "Can be found through a doorway near a Petank, in the section with the Eveque bosses",
        },
    ),
    Pictos(
        name="Rush on Powerful",
        description="Apply Rush on applying Powerful",
        cost=10,
        location={
             "Endless Tower": "Clear Stage 9, Trial 3",
             "Renoir's Drafts": "From Golden Tree Expedition Flag, go up the ramp, go to the right of the portal, and grapple up to the building. The Picto is at the end of the path",
        },
    ),
    Pictos(
        name="SOS Power",
        description="Apply Powerful when falling below 50% Health",
        cost=5,
        location={
             "Stone Wave Cliffs": "From the Paintress Shrine Expedition Flag, go down the path on the right and cross the narrow stone bridge. Take the path on the right and hug the right wall up the grassy slope. Behind the hexagon cliff structures, pick up the SOS Power behind it",
        },
    ),
    Pictos(
        name="SOS Rush",
        description="Apply Rush when falling below 50% Health",
        cost=5,
        location={
             "Falling Leaves": "Can be found by a large tree stump within the Resinveil Grove section near Expedition 35's Journal and the Human Bridge",
        },
    ),
    Pictos(
        name="SOS Shell",
        description="Apply Shell when falling below 50% Health ",
        cost=5,
        location={
             "Flying Waters": "Found at the end of a path to the left of Expedition 68's sunken ship, or by hugging the left wall from the start of the area",
        },
    ),
    Pictos(
        name="Second Chance",
        description="Revive with 100% Health. Once per battle",
        cost=40,
        location={
             "The Monolith": "Obtained as a reward for defeating Renoir at the Tower Peak. Cannot be missed",
             "Renoir's Drafts": "Obtained as a reward for defeating Création near Grour, right before the Golden Tree Expedition Flag",
        },
    ),
    Pictos(
        name="Shared Care",
        description="When healing an ally, also Heal self for 50% of that value",
        cost=10,
        location={
             "The Continent": "Can be found by some broken crates on the southern part of the island northwest of the Red Woods",
        },
    ),
    Pictos(
        name="Shell On Rush",
        description="Apply Shell on applying Rush",
        cost=10,
        location={
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 100,050 Chroma. Fight the merchant to reveal this item in its shop",
        },
    ),
    Pictos(
        name="Shield Affinity",
        description=" 30% increased damage while having Shields, but receiving any damage always removes all Shields",
        cost=15,
        location={
             "Sirene": "Break the Paint Cage to obtain Shield Affinity",
             "Sacred River": "Fight and win against the Gestral Merchant to unlock all the items in its shop. This merchant sells this item for 78,575 Chroma",
        },
    ),
    Pictos(
        name="Shielding Death",
        description="On death, allies gain 3 Shield points",
        cost=10,
        location={
             "The Crows": "Shoot all the crows in the location for the boss to appear. This weapon is acquired as a drop reward for defeating the Chromatic Chapelier",
        },
    ),
    Pictos(
        name="Shielding Tint",
        description="Healing Tints also add 2 Shields",
        cost=10,
        location={
             "The Continent": "The Shielding Tint Pictos can be found on the ground under wooden crates near the Bourgeon southeast of Forgotten Battlefield",
        },
    ),
    Pictos(
        name="Shortcut",
        description="Immediately play when falling below 30% Health. Once per battle",
        cost=5,
        location={
             "Lumiere": "head up the stairs at the harbour and defeat the Aberration to receive Shortcut as a drop",
        },
    ),
    Pictos(
        name="Slowing Break",
        description="Apply Slow on Break",
        cost=5,
        location={
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Sniper",
        description="First Free Aim shot each turn deals 200% increased damage and can Break",
        cost=15,
        location={
             "The Reacher": "From the Mountain Expedition Flag, proceed along the path ahead, and grapple across to the mountain. There will be a group of enemies that consists of 2 Echassier, defeat them to obtain Sniper",
        },
    ),
    Pictos(
        name="Solidifying",
        description="+2 Shields when the character's Health falls below 50%. Once per battle",
        cost=10,
        location={
             "Crushing Cavern": "Dropped upon defeating the Giant Sapling",
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 67,350 Chroma",
        },
    ),
    Pictos(
        name="Solo Fighter",
        description="Deal 50% more damage if fighting alone",
        cost=1,
        location={
             "Hidden Gestral Arena": "Win the duel against Bertrand Big Hands",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
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
             "The Monolith": "Can be found in the arena where you fight the Chromatic Bourgeon, past the seaweed wall, across the Tainted Waters Expedition flag",
             "Flying Manor": "Sold by the Gestral Merchant Fusoka after defeating him in a duel",
        },
    ),
    Pictos(
        name="Stun Boost",
        description="30% increased damage on Stunned targets",
        cost=10,
        location={
             "Ancient Sanctuary": "In the boss room of the Ultimate Sakapatate, there will be a small cave entrance you will have to crouch through to get in. The Pictos will be in here",
             "Sacred River": "Fight and win the Gestral Merchant to unlock all the items in its shop. This merchant sells a level 20 variation of this item for 67,350 Chroma",
        },
    ),
    Pictos(
        name="Survivor",
        description="Survive fatal damage with 1 Health. Once per battle",
        cost=20,
        location={
             "Monoco's Station": "Sold by the Grandis Merchant after completing the Eternal Ice Quest",
        },
    ),
    Pictos(
        name="Sweet Kill",
        description="Recover 50% Health on killing an enemy",
        cost=5,
        location={
             "Forgotten Battlefield": "From the Main Gate flag, enter the left trench, then go up the stairs and across the bridge to find the Sweet Kill pictos behind a group of enemies",
             "Renoir's Drafts": "Sold by the Gestral Merchant Grour after defeating him in a duel",
        },
    ),
    Pictos(
        name="Tainted",
        description="15% increased damage for each Status Effect on self",
        cost=3,
        location={
             "Stone Wave Cliffs": "Can be obtained upon defeating the Chromatic Gault past the Paint Spike in the Old Farm",
             "The Reacher": "Can be purchased from Eragol for 49,391 Chroma",
        },
    ),
    Pictos(
        name="Teamwork",
        description="10% increased damage while all allies are alive",
        cost=5,
        location={
             "Yellow Harvest": "Defeat the Merchant Pinabby to unlock it from his wares, can be purchased for 9,120 Chroma",
        },
    ),
    Pictos(
        name="The One",
        description="Max Health is reduced to 1",
        cost=1,
        location={
             "Sunless Cliffs": "Defeat the Mime enemy for the first time to obtain The One",
        },
    ),
    Pictos(
        name="Time Tint",
        description="Energy Tints also apply Rush",
        cost=5,
        location={
             "Endless Tower": "Rewarded for completing Stage 4, Trial 3",
        },
    ),
    Pictos(
        name="Versatile",
        description="After a Free Aim hit, Base Attack damage is increased by 50% for 1 turn",
        cost=5,
        location={
             "Flying Waters": "After Lumièran Streets Expedition Flag, go straight and grapple up twice onto broken houses, then follow the path",
             "Endless Night Sanctuary": "Sold by the Gestral Merchant Anthonypo for 80,040 Chroma",
        },
    ),
    Pictos(
        name="Warming Up",
        description="5% increased damage per turn. Can stack up to 5 times",
        cost=15,
        location={
             "The Continent": "Dropped by the Grosse Tete (Boss)",
        },
    ),
    Pictos(
        name="Weakness Gain",
        description="+1AP on hitting an enemy's Weakness. Once per turn",
        cost=3,
        location={
             "The Monolith": "From the Tainted Cliffs Expedition Flag, make your way up and grapple across to the cliffs ahead. Continue down this straight path, past the forks in the path. At the end where you are met with a statue, take the right path, head right to find a broken airship, Weakness Gain can be picked up on the right",
        },
    ),
]
