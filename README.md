##Description

A M&B Warband mod to enhance, simplify and improve the game play experience of Native.

##Features
New Map Textures
Smooth Deathcam
Colored Messages
Troop Tree Display
View All Items
Trade Item Modifiers
New Morale & Routing System
Sorted Troops in Party
More Trade Goods
More Food
Weather
Speak with Elder/Guild Master
More higher quality troops in general, but especially for kings
Revamped Troops
Revamped Items (TODO)
Special Faction Knights for Faction Lords
Recruit Faction Knights from castles and towns
Loot villages, join sieges, and fight on any side of a battle regardless of relationships
Persuasion is now based on charisma instead of intelligence

##Changelog

Will be added when the second version is released.

##Credits

Here's a list of all authors, modifications, and how to find those modifications in the source code.

Modifications I've made to OSP's such as Sort Party Troops may or may not be tagged.

To the people on this list: thank you for releasing your code and/or resources as open source.

If I've missed anything please get in touch so I can credit that person properly.

```
Author					Modification									Source

Lav                     WRECK                                           compile.bat, compile.py, compiler.py
Lav                     Improved 1.166 headers                          headers_*.py
Zephilinox, MadVader    Perfectly Smooth Mouse-Enabled Deathcam         ##BEAN - Deathcam
HardCode                Color Coded Messages                            ##BEAN - Color Coded Messages
Dunde, Caba`drin        Dynamic Faction Troop Trees                     ##BEAN - Dynamic Faction Troop Tree
DOMA_                   Cinematic Compilation                           ##BEAN - Cinematic Compilation
Openshaw                Expanded Horizons
rubik                   View All Items                                  ##BEAN - View All Items
Lav                     Improved Trade Goods                            ##BEAN - Improved Trade Goods
jacobhinds              Overhauled Morale & Routing                     ##BEAN - Overhauled Morale
sphere, Caba`drin       Dynamic Arrays                                  plugin_dynamic_arrays.py
Caba`drin               Merchant Trade Ledger                           ##BEAN - Trade Ledger
rubik                   Sort Party Troops                               plugin_sort_party_troops.py
painbringer             World Map HD
gameweb                 HD Textures
Waihti, Somebody, etc.  Diplomacy for 1.165                             ##diplomacy, ##BEAN - Diplomacy
```

##Modifications

Here's a list of all modifications made to native that are not OSP, along with how to find them in the source files (Note: may need to search for ##BEAN BEGIN - XYZ instead)

```
Author					Modification									Source

Zephilinox              Enabled Native Custom Banners                   ##BEAN - Custom Banners
Zephilinox              Extra Trade Goods                               ##BEAN - Extra Trade Goods
Zephilinox              Weather                                         ##BEAN - Weather
Zephilinox              Bean Initialization                             ##BEAN - Initialize
Zephilinox              Bean Options                                    ##BEAN - Options
Zephilinox              Speak With                                      ##BEAN - Speak With
Zephilinox              No limit to attacking based on relations        ##BEAN - Attack Relations
Zephilinox              Extra XP for King                               ##BEAN - King Troop XP
Zephilinox              Special Lord Unit                               ##BEAN - Knights
Zephilinox              Diplomacy culture when recruiting               ##BEAN - Recruit Culture
Zephilinox              Added cheat to villages to refresh volunteers   ##BEAN - Cheat Refresh Volunteers
Zephilinox              Remove ability for player to garrison knights   ##BEAN - Disable Knights From Garrison
Zephilinox              Replaced regular_party_strength with normal     party_calculate_regular_strength in module_scripts.py
Zephilinox              Buffed XP of troops in centers                  game_start and give_center_to_lord and dplmc_player_center_surrender in module_scripts.py
Zephilinox              Buffed XP from quality by 5x                    upgrade_hero_party in module_scripts.py
Zephilinox              Buffed XP given to parties regularly            ##BEAN - Increase XP
```

##Issues
```
Horse dust in arena (vaegir) is broken?
Custom battles deathcam
```

##TODO
```
Troop Trees
Revamp every item
Add new items to fill gaps
Modify Troops to use revamped items
Add ability to mass-sell all prisoners
Trade with caravans
```