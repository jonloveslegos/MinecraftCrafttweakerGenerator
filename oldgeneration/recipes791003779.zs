//#Remove
recipes.removeAll();
//#Inv
mods.initialinventory.InvHandler.addStartingItem(<item:minecraft:bow>);
mods.initialinventory.InvHandler.addStartingItem(<item:minecraft:arrow> * 16);
//#Add
recipes.addShaped(<minecraft:bow>,[[null, <minecraft:log>], [null, null]]);
recipes.addShaped(<minecraft:arrow>,[[null, null], [<minecraft:log>, null]]);
recipes.addShaped(<minecraft:log>,[[<minecraft:log:*>, null], [null, null]]);
recipes.addShaped(<minecraft:wool>,[[<minecraft:wool:*>, null], [null, null]]);
recipes.addShaped(<minecraft:log>,[[<minecraft:log>, null], [null, null]]);
recipes.addShaped(<minecraft:wool>,[[<minecraft:wool>, null], [null, null]]);
recipes.addShaped(<naturescompass:naturescompass>,[[<minecraft:dirt>, null], [null, null]]);
recipes.addShaped(<minecraft:paper>,[[<minecraft:wheat_seeds>,<minecraft:wheat_seeds>],[<minecraft:wheat_seeds>,null]]);
recipes.addShaped(<minecraft:gold_nugget>,[[<minecraft:wheat_seeds>,<minecraft:wheat_seeds>],[null,null]]);
recipes.addShaped(<minecraft:sign>,[[<minecraft:wheat_seeds>,null],[null,null]]);
recipes.addShaped(<minecraft:end_crystal>,[[<minecraft:paper>,null],[null,null]]);
recipes.addShaped(<minecraft:stick>,[[<minecraft:gold_nugget>,<minecraft:gold_nugget>],[<minecraft:paper>,null]]);
recipes.addShaped(<minecraft:lever>,[[<minecraft:gold_nugget>,<minecraft:wheat_seeds>],[null,null]]);
recipes.addShaped(<minecraft:redstone_lamp>,[[<minecraft:stick>,null],[null,null]]);
recipes.addShaped(<minecraft:golden_axe>,[[<minecraft:paper>,<minecraft:stick>],[null,null]]);
recipes.addShaped(<minecraft:shield>,[[<minecraft:paper>,<minecraft:paper>],[null,null]]);
recipes.addShaped(<minecraft:bowl>,[[<minecraft:stick>,<minecraft:gold_nugget>],[null,null]]);
recipes.addShaped(<minecraft:stone_axe>,[[<minecraft:wheat_seeds>,<minecraft:gold_nugget>],[null,null]]);
recipes.addShaped(<minecraft:sugar>,[[<minecraft:bowl>,null],[null,null]]);
recipes.addShaped(<minecraft:golden_rail>,[[<minecraft:bowl>,<minecraft:sugar>],[<minecraft:paper>,null]]);
recipes.addShaped(<minecraft:ender_chest>,[[<minecraft:wheat_seeds>,<minecraft:sugar>],[<minecraft:bowl>,null]]);
recipes.addShaped(<minecraft:wooden_pickaxe>,[[<minecraft:sugar>,null],[null,null]]);
recipes.addShaped(<minecraft:compass>,[[<minecraft:paper>,<minecraft:gold_nugget>],[null,null]]);
recipes.addShaped(<minecraft:iron_nugget>,[[<minecraft:wheat_seeds>,<minecraft:sugar>],[null,null]]);
recipes.addShaped(<minecraft:blaze_powder>,[[<minecraft:gold_nugget>,<minecraft:stick>],[null,null]]);
recipes.addShaped(<minecraft:glass_bottle>,[[<minecraft:bowl>,<minecraft:sugar>],[null,null]]);
recipes.addShaped(<minecraft:iron_block>,[[<minecraft:carrot>,<ore:cobblestone>],[<minecraft:carrot>,null]]);
recipes.addShaped(<minecraft:ladder>,[[<minecraft:gold_nugget>,<minecraft:blaze_powder>],[null,null]]);
recipes.addShaped(<minecraft:iron_axe>,[[<minecraft:blaze_powder>,<minecraft:carrot>],[<minecraft:blaze_powder>,null]]);
recipes.addShaped(<minecraft:fishing_rod>,[[<minecraft:blaze_powder>,null],[null,null]]);
recipes.addShaped(<minecraft:rail>,[[<minecraft:iron_nugget>,<ore:cobblestone>],[null,null]]);
recipes.addShaped(<minecraft:wooden_axe>,[[<minecraft:iron_nugget>,null],[null,null]]);
recipes.addShaped(<minecraft:bow>,[[<minecraft:gold_nugget>,<minecraft:iron_block>],[<minecraft:sugar>,null]]);
recipes.addShaped(<minecraft:chest>,[[<minecraft:blaze_powder>,<minecraft:bowl>],[<minecraft:sugar>,null]]);
recipes.addShaped(<minecraft:minecart>,[[<ore:cobblestone>,null],[null,null]]);
recipes.addShaped(<minecraft:bucket>,[[<minecraft:paper>,<minecraft:carrot>],[null,null]]);
recipes.addShaped(<minecraft:ender_eye>,[[<ore:cobblestone>,<minecraft:reeds>],[<minecraft:reeds>,null]]);
recipes.addShaped(<minecraft:anvil>,[[<minecraft:iron_block>,<minecraft:iron_block>],[null,null]]);
recipes.addShaped(<minecraft:boat>,[[<minecraft:reeds>,<minecraft:blaze_powder>],[null,null]]);
recipes.addShaped(<minecraft:leather_chestplate>,[[<minecraft:reeds>,null],[null,null]]);
recipes.addShaped(<minecraft:jukebox>,[[<minecraft:carrot>,<minecraft:wheat_seeds>],[null,null]]);
recipes.addShaped(<minecraft:planks>,[[<ore:cobblestone>,<minecraft:blaze_powder>],[<minecraft:paper>,null]]);
recipes.addShaped(<minecraft:enchanting_table>,[[<ore:cobblestone>,<minecraft:sugar>],[null,null]]);
recipes.addShaped(<minecraft:arrow>,[[<minecraft:iron_block>,null],[null,null]]);
recipes.addShaped(<minecraft:torch>,[[<minecraft:wheat_seeds>,<minecraft:stick>],[<minecraft:sugar>,null]]);
recipes.addShaped(<minecraft:bed:14>,[[<minecraft:bowl>,<minecraft:wheat_seeds>],[<minecraft:iron_block>,null]]);
recipes.addShaped(<minecraft:stone_button>,[[<minecraft:iron_nugget>,<minecraft:sugar>],[<minecraft:gold_nugget>,null]]);
recipes.addShaped(<minecraft:leather_helmet>,[[<ore:cobblestone>,<minecraft:blaze_powder>],[<minecraft:wheat_seeds>,null]]);
recipes.addShaped(<minecraft:fence>,[[<minecraft:melon>,<minecraft:planks>],[null,null]]);
recipes.addShaped(<minecraft:shears>,[[<minecraft:blaze_powder>,<minecraft:iron_nugget>],[<minecraft:iron_block>,null]]);
recipes.addShaped(<minecraft:golden_helmet>,[[<minecraft:clay_ball>,<minecraft:carrot>],[<minecraft:iron_nugget>,null]]);
recipes.addShaped(<minecraft:flint_and_steel>,[[<minecraft:paper>,<minecraft:iron_nugget>],[<minecraft:sand>,null]]);
recipes.addShaped(<minecraft:iron_helmet>,[[<minecraft:bowl>,<minecraft:gold_nugget>],[<minecraft:wheat_seeds>,null]]);
recipes.addShaped(<minecraft:clock>,[[<minecraft:carrot>,<minecraft:reeds>],[null,null]]);
recipes.addShaped(<minecraft:crafting_table>,[[<minecraft:reeds>,<minecraft:bowl>],[<minecraft:planks>,null]]);
recipes.addShaped(<minecraft:diamond_helmet>,[[<minecraft:reeds>,<minecraft:iron_nugget>,<minecraft:melon>],[<minecraft:sugar>,<minecraft:stick>,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_chestplate>,[[<minecraft:melon>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_chestplate>,[[<minecraft:reeds>,<minecraft:sugar>,<minecraft:sand>],[<minecraft:melon>,<minecraft:melon>,null],[null,null,null]]);
recipes.addShaped(<minecraft:glowstone>,[[<minecraft:sugar>,<minecraft:flint>,<minecraft:wool>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:stone_pickaxe>,[[<minecraft:iron_nugget>,<minecraft:paper>,<minecraft:melon>],[<minecraft:carrot>,<minecraft:gold_nugget>,<minecraft:bowl>],[null,null,null]]);
recipes.addShaped(<minecraft:wooden_shovel>,[[<minecraft:melon>,<minecraft:carrot>,<minecraft:stick>],[<minecraft:melon>,<minecraft:iron_nugget>,<minecraft:wool>],[<minecraft:paper>,null,null]]);
recipes.addShaped(<minecraft:stone_shovel>,[[<minecraft:carrot>,<minecraft:gold_nugget>,<minecraft:snowball>],[<minecraft:gold_nugget>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_shovel>,[[<minecraft:carrot>,<minecraft:sugar>,<minecraft:clay_ball>],[<minecraft:paper>,<minecraft:bowl>,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_shovel>,[[<minecraft:sand>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:melon_seeds>,[[<minecraft:clay_ball>,<minecraft:dye:4>,<minecraft:glowstone>],[<minecraft:glowstone>,<minecraft:bowl>,null],[null,null,null]]);
recipes.addShaped(<minecraft:cauldron>,[[<minecraft:dye:4>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_axe>,[[<minecraft:leaves>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_pickaxe>,[[<minecraft:glowstone>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:leather_boots>,[[<minecraft:glowstone>,<minecraft:leaves>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_boots>,[[<minecraft:flint>,<minecraft:blaze_powder>,<minecraft:melon>],[<minecraft:wool>,<minecraft:reeds>,<minecraft:iron_nugget>],[null,null,null]]);
recipes.addShaped(<minecraft:iron_boots>,[[<minecraft:carrot>,<minecraft:glowstone>,<minecraft:paper>],[<minecraft:wheat_seeds>,<minecraft:paper>,<minecraft:bowl>],[<minecraft:iron_block>,null,null]]);
recipes.addShaped(<minecraft:diamond_boots>,[[<minecraft:blaze_powder>,<minecraft:stick>,<minecraft:melon>],[<minecraft:carrot>,<minecraft:iron_block>,<minecraft:leaves>],[null,null,null]]);
recipes.addShaped(<minecraft:noteblock>,[[<ore:cobblestone>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_sword>,[[<minecraft:melon_seeds>,<minecraft:carrot>,<minecraft:bowl>],[<minecraft:clay_ball>,<minecraft:wool>,<minecraft:iron_nugget>],[null,null,null]]);
recipes.addShaped(<minecraft:stone_sword>,[[<minecraft:reeds>,<minecraft:iron_block>,<ore:cobblestone>],[<minecraft:sand>,<minecraft:reeds>,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_sword>,[[<minecraft:melon_seeds>,<minecraft:dye:4>,<minecraft:snowball>],[<minecraft:snowball>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_sword>,[[<minecraft:sand>,<minecraft:glowstone>,<minecraft:wheat_seeds>],[<minecraft:glowstone>,<minecraft:melon_seeds>,<minecraft:spider_eye>],[<minecraft:log>,<minecraft:flint>,null]]);
recipes.addShaped(<minecraft:dye:15>,[[<minecraft:clay_ball>,<minecraft:gold_nugget>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:book>,[[<minecraft:rabbit_foot>,<ore:cobblestone>,<minecraft:sand>],[<minecraft:rabbit_foot>,<minecraft:planks>,<minecraft:blaze_powder>],[<minecraft:leaves>,<minecraft:bone>,null]]);
recipes.addShaped(<minecraft:golden_carrot>,[[<minecraft:melon_seeds>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_chestplate>,[[<minecraft:bowl>,<minecraft:melon_seeds>,<minecraft:dye:4>],[<minecraft:snowball>,<minecraft:bowl>,<minecraft:glowstone>],[<minecraft:wool>,null,null]]);
recipes.addShaped(<minecraft:brewing_stand>,[[<minecraft:slime_ball>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:pumpkin_seeds>,[[<minecraft:spider_eye>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:bookshelf>,[[<minecraft:pumpkin_seeds>,<minecraft:golden_carrot>,<minecraft:bone>],[<minecraft:book>,<minecraft:planks>,<minecraft:flint>],[<minecraft:paper>,<minecraft:stick>,null]]);
recipes.addShaped(<minecraft:speckled_melon>,[[<minecraft:slime_ball>,<ore:cobblestone>,<minecraft:book>],[<minecraft:leather>,<minecraft:feather>,<minecraft:sand>],[<minecraft:gold_nugget>,null,null]]);
recipes.addShaped(<minecraft:fermented_spider_eye>,[[<minecraft:snowball>,<minecraft:leather>,<minecraft:spider_eye>],[<minecraft:clay_ball>,<minecraft:ender_pearl>,<minecraft:spider_eye>],[<minecraft:bone>,<minecraft:sugar>,null]]);
recipes.addShaped(<minecraft:furnace>,[[<minecraft:string>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:wooden_sword>,[[<minecraft:spider_eye>,<minecraft:stone>,<minecraft:flint>],[<minecraft:slime_ball>,<minecraft:bone>,<minecraft:gold_nugget>],[null,null,null]]);
recipes.addShaped(<minecraft:leather_leggings>,[[<minecraft:fermented_spider_eye>,<minecraft:paper>,<minecraft:wheat_seeds>],[<minecraft:wheat_seeds>,<minecraft:iron_nugget>,<minecraft:log>],[<ore:cobblestone>,<minecraft:sugar>,null]]);
recipes.addShaped(<minecraft:golden_leggings>,[[<minecraft:paper>,<minecraft:glass>,<minecraft:bone>],[<minecraft:melon_seeds>,<minecraft:bone>,<minecraft:rabbit_foot>],[null,null,null]]);
recipes.addShaped(<minecraft:iron_leggings>,[[<minecraft:paper>,<minecraft:planks>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_leggings>,[[<minecraft:rabbit_foot>,<minecraft:egg>,<minecraft:pumpkin_seeds>],[<minecraft:iron_nugget>,<minecraft:coal>,<minecraft:flint>],[<minecraft:coal>,<minecraft:coal>,null]]);
recipes.addShaped(<minecraft:iron_pickaxe>,[[<minecraft:bowl>,<minecraft:reeds>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_pickaxe>,[[<minecraft:ender_pearl>,<minecraft:dye:4>,<minecraft:melon_seeds>],[<minecraft:log>,<minecraft:stick>,<minecraft:glowstone>],[<minecraft:log>,<minecraft:sand>,null]]);
recipes.addShaped(<minecraft:golden_shovel>,[[<minecraft:bone>,<minecraft:slime_ball>,<minecraft:flint>],[null,null,null],[null,null,null]]);
//File End