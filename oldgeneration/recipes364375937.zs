//#Remove
recipes.removeAll();
//#Inv
mods.initialinventory.InvHandler.addStartingItem("archer", <item:minecraft:bow>);
mods.initialinventory.InvHandler.addStartingItem("archerArrow", <item:minecraft:arrow> * 16);
//#Add
recipes.addShaped(<minecraft:log>,[[<minecraft:log:*>, null], [null, null]]);
recipes.addShaped(<minecraft:wool>,[[<minecraft:wool:*>, null], [null, null]]);
recipes.addShaped(<naturescompass:naturescompass>,[[<minecraft:dirt>, null], [null, null]]);
recipes.addShaped(<minecraft:wooden_sword>,[[<minecraft:clay_ball>,null],[null,null]]);
recipes.addShaped(<minecraft:leather_helmet>,[[<minecraft:spider_eye>,null],[null,null]]);
recipes.addShaped(<minecraft:leather_leggings>,[[<minecraft:spider_eye>,<minecraft:spider_eye>],[<minecraft:spider_eye>,null]]);
recipes.addShaped(<minecraft:minecart>,[[<minecraft:leather>,null],[null,null]]);
recipes.addShaped(<minecraft:jukebox>,[[<minecraft:spider_eye>,<minecraft:spider_eye>],[null,null]]);
recipes.addShaped(<minecraft:golden_pickaxe>,[[<minecraft:leather>,<minecraft:leather>],[null,null]]);
recipes.addShaped(<minecraft:melon_seeds>,[[<ore:cobblestone>,null],[null,null]]);
recipes.addShaped(<minecraft:golden_helmet>,[[<minecraft:melon_seeds>,<minecraft:spider_eye>],[<minecraft:clay_ball>,null]]);
recipes.addShaped(<minecraft:ladder>,[[<ore:cobblestone>,<minecraft:spider_eye>],[<minecraft:spider_eye>,null]]);
recipes.addShaped(<minecraft:crafting_table>,[[<minecraft:coal>,null],[null,null]]);
recipes.addShaped(<minecraft:anvil>,[[<minecraft:bone>,<minecraft:leather>,<minecraft:bone>],[<minecraft:melon_seeds>,<ore:cobblestone>,<minecraft:melon_seeds>],[<ore:cobblestone>,null,null]]);
recipes.addShaped(<minecraft:ender_chest>,[[<minecraft:rabbit_foot>,<minecraft:spider_eye>,<minecraft:leather>],[<minecraft:melon_seeds>,<minecraft:bone>,null],[null,null,null]]);
recipes.addShaped(<minecraft:arrow>,[[<minecraft:coal>,<minecraft:melon_seeds>,<minecraft:spider_eye>],[<minecraft:clay_ball>,<minecraft:coal>,<minecraft:leather>],[null,null,null]]);
recipes.addShaped(<minecraft:stone_sword>,[[<minecraft:clay_ball>,<minecraft:spider_eye>,<minecraft:clay_ball>],[<ore:cobblestone>,<minecraft:spider_eye>,<minecraft:coal>],[null,null,null]]);
recipes.addShaped(<minecraft:wooden_shovel>,[[<minecraft:rabbit_foot>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:stone_shovel>,[[<minecraft:coal>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:stick>,[[<minecraft:melon_seeds>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:boat>,[[<ore:cobblestone>,<minecraft:bone>,<minecraft:rabbit_foot>],[<minecraft:coal>,<minecraft:bone>,<minecraft:stick>],[<minecraft:melon_seeds>,null,null]]);
recipes.addShaped(<minecraft:enchanting_table>,[[<minecraft:dye>,<minecraft:stick>,<minecraft:leather>],[<minecraft:bone>,<minecraft:spider_eye>,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_leggings>,[[<minecraft:coal>,<minecraft:dye>,<minecraft:spider_eye>],[<minecraft:leather>,<minecraft:clay_ball>,<minecraft:clay_ball>],[null,null,null]]);
recipes.addShaped(<minecraft:furnace>,[[<minecraft:stick>,<minecraft:stick>,<ore:cobblestone>],[<ore:cobblestone>,<minecraft:leather>,<minecraft:clay_ball>],[<ore:cobblestone>,<minecraft:snowball>,null]]);
recipes.addShaped(<minecraft:rail>,[[<minecraft:glass>,<minecraft:snowball>,<minecraft:coal>],[<minecraft:spider_eye>,<minecraft:stone>,null],[null,null,null]]);
recipes.addShaped(<minecraft:speckled_melon>,[[<minecraft:clay_ball>,<minecraft:coal:1>,<minecraft:bone>],[<minecraft:coal:1>,<minecraft:coal:1>,<minecraft:bone>],[null,null,null]]);
recipes.addShaped(<minecraft:golden_sword>,[[<minecraft:glass>,<ore:cobblestone>,<minecraft:glass>],[<minecraft:sand>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:shears>,[[<minecraft:snowball>,<ore:cobblestone>,<minecraft:spider_eye>],[<minecraft:stick>,<minecraft:dye>,<minecraft:glass>],[<minecraft:leather>,<minecraft:sand>,null]]);
recipes.addShaped(<minecraft:bowl>,[[<minecraft:glass>,<minecraft:dye>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:blaze_powder>,[[<minecraft:bowl>,<minecraft:coal:1>,<minecraft:spider_eye>],[<minecraft:leaves>,<minecraft:leaves>,<minecraft:melon_seeds>],[<minecraft:stick>,<minecraft:snowball>,null]]);
recipes.addShaped(<minecraft:ender_eye>,[[<minecraft:feather>,<minecraft:spider_eye>,<minecraft:glass>],[<minecraft:melon_seeds>,<minecraft:feather>,null],[null,null,null]]);
recipes.addShaped(<minecraft:noteblock>,[[<minecraft:clay_ball>,<minecraft:bowl>,<minecraft:blaze_powder>],[<minecraft:feather>,<minecraft:bowl>,<minecraft:clay_ball>],[<minecraft:blaze_powder>,<minecraft:blaze_powder>,null]]);
recipes.addShaped(<minecraft:clock>,[[<minecraft:snowball>,<minecraft:speckled_melon>,<minecraft:dye>],[<minecraft:spider_eye>,<ore:cobblestone>,<minecraft:spider_eye>],[<minecraft:feather>,<ore:cobblestone>,null]]);
recipes.addShaped(<minecraft:end_crystal>,[[<minecraft:blaze_powder>,<minecraft:dye>,<minecraft:stick>],[<minecraft:feather>,<minecraft:coal:1>,<minecraft:leaves>],[null,null,null]]);
recipes.addShaped(<minecraft:wooden_pickaxe>,[[<minecraft:leaves>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:pumpkin_seeds>,[[<minecraft:wool>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:compass>,[[<minecraft:stick>,<minecraft:rabbit_foot>,<minecraft:spider_eye>],[<minecraft:leather>,<minecraft:rabbit_foot>,<ore:cobblestone>],[null,null,null]]);
recipes.addShaped(<minecraft:iron_block>,[[<minecraft:speckled_melon>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_shovel>,[[<minecraft:glass>,<minecraft:pumpkin_seeds>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_helmet>,[[<minecraft:dye>,<minecraft:sand>,<minecraft:flint>],[<minecraft:spider_eye>,<minecraft:bone>,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_rail>,[[<minecraft:glass>,<minecraft:spider_eye>,<minecraft:glass>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:stone_pickaxe>,[[<ore:cobblestone>,<minecraft:pumpkin_seeds>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:redstone_lamp>,[[<ore:cobblestone>,<minecraft:spider_eye>,<minecraft:feather>],[<minecraft:blaze_powder>,<minecraft:snowball>,<minecraft:sand>],[null,null,null]]);
recipes.addShaped(<minecraft:sign>,[[<minecraft:bone>,<minecraft:coal>,<minecraft:stick>],[<minecraft:dye>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_leggings>,[[<minecraft:stick>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_leggings>,[[<minecraft:snowball>,<minecraft:melon_seeds>,<minecraft:feather>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:glowstone>,[[<minecraft:spider_eye>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:torch>,[[<minecraft:glowstone>,<minecraft:wool>,<minecraft:bone>],[<minecraft:coal>,<minecraft:glass>,<minecraft:sand>],[null,null,null]]);
recipes.addShaped(<minecraft:book>,[[<minecraft:wool>,<minecraft:sand>,<minecraft:melon_seeds>],[<minecraft:spider_eye>,<minecraft:dye>,null],[null,null,null]]);
recipes.addShaped(<minecraft:fermented_spider_eye>,[[<minecraft:wool>,<minecraft:dye:4>,<minecraft:pumpkin_seeds>],[<minecraft:wool>,<minecraft:stone>,<minecraft:leather>],[null,null,null]]);
recipes.addShaped(<minecraft:iron_pickaxe>,[[<minecraft:glass>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_pickaxe>,[[<ore:cobblestone>,<minecraft:stick>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_sword>,[[<minecraft:iron_ingot>,<minecraft:rabbit_foot>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_sword>,[[<minecraft:glowstone>,<minecraft:bowl>,<minecraft:sand>],[<minecraft:redstone>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:flint_and_steel>,[[<minecraft:blaze_powder>,<minecraft:dye>,<minecraft:fermented_spider_eye>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:chest>,[[<minecraft:bone>,<minecraft:iron_ingot>,<ore:cobblestone>],[<minecraft:snowball>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:cauldron>,[[<minecraft:sand>,<minecraft:bowl>,<minecraft:wool>],[<minecraft:melon_seeds>,<minecraft:fermented_spider_eye>,<minecraft:pumpkin_seeds>],[<minecraft:bone>,null,null]]);
recipes.addShaped(<minecraft:gold_nugget>,[[<minecraft:dye>,<minecraft:book>,<minecraft:pumpkin_seeds>],[<minecraft:blaze_powder>,<minecraft:stone>,<minecraft:pumpkin_seeds>],[<minecraft:rabbit_foot>,null,null]]);
recipes.addShaped(<minecraft:diamond_helmet>,[[<minecraft:stone>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:planks>,[[<minecraft:gold_ingot>,<minecraft:rabbit_foot>,<minecraft:glowstone>],[<minecraft:leather>,<minecraft:rabbit_foot>,<minecraft:feather>],[<minecraft:dye:4>,null,null]]);
recipes.addShaped(<minecraft:fishing_rod>,[[<minecraft:planks>,<minecraft:bone>,<minecraft:melon_seeds>],[<minecraft:dye>,<minecraft:stick>,<minecraft:sand>],[<minecraft:leaves>,<minecraft:leaves>,null]]);
recipes.addShaped(<minecraft:sugar>,[[<minecraft:iron_block>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:lever>,[[<minecraft:sugar>,<minecraft:iron_block>,<minecraft:pumpkin_seeds>],[<minecraft:dye>,<minecraft:coal>,<ore:cobblestone>],[null,null,null]]);
recipes.addShaped(<minecraft:golden_axe>,[[<minecraft:coal:1>,<minecraft:flint>,<minecraft:dye:4>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:stone_axe>,[[<minecraft:diamond>,<minecraft:emerald>,<minecraft:leaves>],[<minecraft:sugar>,<minecraft:diamond>,null],[null,null,null]]);
recipes.addShaped(<minecraft:leather_chestplate>,[[<minecraft:fermented_spider_eye>,<minecraft:stick>,<minecraft:flint>],[<minecraft:iron_block>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_chestplate>,[[<minecraft:planks>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_chestplate>,[[<minecraft:stick>,<minecraft:flint>,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:paper>,[[<minecraft:emerald>,<minecraft:fermented_spider_eye>,<minecraft:flint>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_chestplate>,[[<minecraft:diamond>,<minecraft:stone>,<minecraft:redstone>],[<minecraft:leaves>,<minecraft:stick>,null],[null,null,null]]);
recipes.addShaped(<minecraft:brewing_stand>,[[<minecraft:dye:4>,<minecraft:snowball>,<minecraft:speckled_melon>],[<minecraft:iron_block>,<minecraft:stone>,<minecraft:pumpkin_seeds>],[<minecraft:feather>,null,null]]);
recipes.addShaped(<minecraft:bow>,[[<minecraft:log>,<minecraft:paper>,<minecraft:stick>],[<ore:cobblestone>,<ore:cobblestone>,<minecraft:bone>],[<minecraft:melon_seeds>,<minecraft:dye>,null]]);
recipes.addShaped(<minecraft:iron_nugget>,[[<minecraft:clay_ball>,<minecraft:dye>,<minecraft:dye:4>],[<minecraft:paper>,<minecraft:leaves>,null],[null,null,null]]);
recipes.addShaped(<minecraft:dye:15>,[[<minecraft:bone>,<minecraft:dye:4>,<minecraft:snowball>],[<minecraft:sugar>,<minecraft:diamond>,<minecraft:stick>],[null,null,null]]);
recipes.addShaped(<minecraft:wooden_axe>,[[<minecraft:iron_nugget>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:fence>,[[<minecraft:gold_nugget>,<minecraft:flint>,<minecraft:coal>],[<minecraft:feather>,<minecraft:dye>,<minecraft:snowball>],[null,null,null]]);
recipes.addShaped(<minecraft:bucket>,[[<minecraft:planks>,<minecraft:melon_seeds>,<minecraft:bone>],[<minecraft:dye>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:stone_button>,[[<minecraft:obsidian>,<minecraft:melon_seeds>,<minecraft:reeds>],[<minecraft:wool>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:bed:14>,[[<minecraft:leaves>,<minecraft:netherrack>,<minecraft:rabbit_foot>],[<minecraft:leather>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:glass_bottle>,[[<minecraft:glowstone>,<minecraft:spider_eye>,<minecraft:melon_seeds>],[<minecraft:leaves>,<minecraft:snowball>,<minecraft:magma_cream>],[null,null,null]]);
recipes.addShaped(<minecraft:iron_shovel>,[[<minecraft:paper>,<minecraft:coal:1>,<minecraft:stone>],[<minecraft:wool>,<minecraft:melon_seeds>,<minecraft:log>],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_shovel>,[[<minecraft:leather>,<minecraft:coal:1>,<minecraft:spider_eye>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:leather_boots>,[[<minecraft:glowstone_dust>,<minecraft:sand>,<minecraft:melon_seeds>],[<minecraft:clay_ball>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_boots>,[[<minecraft:dye:15>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_boots>,[[<ore:cobblestone>,<minecraft:glass>,<minecraft:gunpowder>],[<minecraft:brick>,<minecraft:feather>,<minecraft:quartz>],[null,null,null]]);
recipes.addShaped(<minecraft:diamond_boots>,[[<minecraft:coal:1>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:golden_carrot>,[[<minecraft:netherbrick>,<minecraft:wheat_seeds>,<minecraft:iron_nugget>],[<minecraft:dye>,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:bookshelf>,[[<minecraft:bone>,null,null],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:iron_axe>,[[<minecraft:netherbrick>,<minecraft:gunpowder>,<minecraft:string>],[<minecraft:dye>,<minecraft:stick>,<minecraft:reeds>],[<minecraft:leaves>,null,null]]);
recipes.addShaped(<minecraft:diamond_axe>,[[<minecraft:quartz>,<minecraft:coal>,<minecraft:pumpkin_seeds>],[null,null,null],[null,null,null]]);
recipes.addShaped(<minecraft:shield>,[[<minecraft:feather>,<minecraft:redstone>,<minecraft:spider_eye>],[<minecraft:emerald>,<minecraft:coal:1>,<minecraft:melon>],[null,null,null]]);
recipes.addShaped(<minecraft:bow>,[[null, <minecraft:log>], [null, null]]);
recipes.addShaped(<minecraft:arrow>,[[null, null], [<minecraft:log>, null]]);
//File End