from header_item_modifiers import *
####################################################################################################################
#  Each item record contains the following fields:
#  1) Imod id: used for referencing imods in other files.
#     The prefix imod_ is automatically added before each imod id.
#     It's hardcoded so don't change it's value
#  2) Imod name. Name of imod, as it'll appear as prefix of item name
#  3) Prize Factor
#  4) Rarity
####################################################################################################################

item_modifiers = [
("plain","Plain", 1.000000, 1.000000),
("cracked","Cracked", 0.500000, 1.000000),
("rusty","Rusty", 0.550000, 1.000000),
("bent","Bent", 0.650000, 1.000000),
("chipped","Chipped", 0.720000, 1.000000),
("battered","Battered", 0.750000, 1.000000),
("poor","Poor", 0.800000, 1.000000),
("crude","Crude", 0.830000, 1.000000),
("old","Old", 0.860000, 1.000000),
("cheap","Cheap", 0.900000, 1.000000),
("fine","Fine", 1.900000, 0.600000),
("well_made","Well_Made", 2.500000, 0.500000),
("sharp","Sharp", 1.600000, 0.600000),
("balanced","Balanced", 3.500000, 0.500000),
("tempered","Tempered", 6.700000, 0.400000),
("deadly","Deadly", 8.500000, 0.300000),
("exquisite","Exquisite", 14.500000, 0.300000),
("masterwork","Masterwork", 17.500000, 0.300000),
("heavy","Heavy", 1.900000, 0.700000),
("strong","Strong", 4.900000, 0.400000),
("powerful","Powerful", 3.200000, 0.400000),
("tattered","Tattered", 0.500000, 1.000000),
("ragged","Ragged", 0.700000, 1.000000),
("rough","Rough", 0.600000, 1.000000),
("sturdy","Sturdy", 1.700000, 0.500000),
("thick","Thick", 2.600000, 0.350000),
("hardened","Hardened", 3.900000, 0.300000),
("reinforced","Reinforced", 6.500000, 0.250000),
("superb","Superb", 2.500000, 0.250000),
("lordly","Lordly", 11.500000, 0.250000),
("lame","Lame", 0.400000, 1.000000),
("swaybacked","Swaybacked", 0.600000, 1.000000),
("stubborn","Stubborn", 0.900000, 1.000000),
("timid","Timid", 1.800000, 1.000000),
("meek","Meek", 1.800000, 1.000000),
("spirited","Spirited", 6.500000, 0.600000),
("champion","Champion", 14.500000, 0.200000),
("fresh","Fresh", 1.000000, 1.000000),
("day_old","Day-old", 1.000000, 1.000000),
("two_day_old","Two_Days-old", 0.900000, 1.000000),
("smelling","Smelling", 0.400000, 1.000000),
("rotten","Rotten", 0.050000, 1.000000),
("large_bag","Large_Bag_of", 1.900000, 0.300000),
]