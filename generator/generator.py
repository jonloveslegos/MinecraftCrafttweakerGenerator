import os
import random
import sys
import shutil
class Ingredient:
  name = ""
  tags = []
  canFind = False
  requirements = []
  myClass = "ingredient"
  difficulty = 0
  def __init__(self,idSet,canFindSet,requirementsSet,tagSet,difficulty):
    self.name = idSet
    self.canFind = canFindSet
    self.requirements = requirementsSet
    self.tags = tagSet
    self.difficulty = difficulty

def deleteElement(list_object, pos):
    if pos < len(list_object):
        list_object.pop(pos)

class Item:
  name = ""
  tags = []
  myClass = "item"
  requirements = []
  difficulty = 999
  def __init__(self,idSet,tagSet,requirementsSet,maxDifficulty):
    self.name = idSet
    self.tags = tagSet
    self.requirements = requirementsSet
    self.difficulty = maxDifficulty*3
def checkAllInList(checkedList,toFind):
  for item in toFind:
    if not item in checkedList:
      return False
  return True

def addIngredient(item,canFind,requirements,tags,difficulty):
  global ingredients
  ingredients = ingredients+[Ingredient(item,canFind,requirements,tags,difficulty),]
def addTool(it,tags,requirements,difficulty):
  global items
  items = items+[Item(it,tags,requirements,difficulty),]
def addRecipe(result, ingredients):
  global recipesAdded
  global recipesTableAdded
  global spoilerList
  recipesTableAdded = recipesTableAdded+[ingredients]
  spoilerList = spoilerList+"\nMake "+result.replace("minecraft:","")+"."
  recipesAdded = recipesAdded+["recipes.addShaped(<"+result+">,["+ingredients+"]);\n",]
def addItemToRecipe(recipe,difficulty,maxDiff):
  temp = []
  for item in generatedIngredients:
    if (item.difficulty+difficulty <= maxDiff):
      temp = temp+[item,]
  return temp
directory_path = os.getcwd()
recipesAdded = []
items = []
spoilerList = "PUT AN '&' SYMBOL BEFORE THE SHOWN NAME WHEN SEARCHING IN JEI!"
ingredientsDefault = "[]"
ingredients = []
generatedIngredients = []
recipesTableAdded = []
def Start():
  global recipesAdded
  recipesAdded = []
  global items
  items = []
  global ingredientsDefault
  ingredientsDefault = "[]"
  global ingredients
  ingredients = []
  global generatedIngredients
  generatedIngredients = []
  global recipesTableAdded
  recipesTableAdded = []
  recentlyAdded = ""
  try:
    seed = int(input("Enter seed (put 0 for a random seed):"))
    if seed == 0:
      random.seed()
      seed = random.randrange(1,1000000000)
      random.seed(seed)
    else:
      random.seed(seed)
  except Exception:
    print("PLEASE INPUT A NUMBER!")
    Start()
    return
  addIngredient("minecraft:log",True,[],["fuel"],0)
  addIngredient("minecraft:reeds",True,[],[],0)
  addIngredient("minecraft:sand",True,[],[],0)
  addIngredient("minecraft:flint",True,[],[],0)
  addIngredient("minecraft:stick",False,[],["fuel"],0)
  addIngredient("minecraft:planks",False,[],["fuel"],0)
  addIngredient("minecraft:obsidian",True,["pickDiamond","bucket"],["obsidian"],5)
  addIngredient("minecraft:quartz",True,["pickWood","flintSteel","obsidian"],[],2)
  addIngredient("minecraft:magma_cream",True,["swordWood","flintSteel","obsidian"],[],4)
  addIngredient("ore:cobblestone",True,["pickWood"],[],0)
  addIngredient("minecraft:coal",True,["pickWood"],["fuel"],1)
  addIngredient("minecraft:coal:1",True,["fuel"],["fuel"],1)
  addIngredient("minecraft:iron_ingot",True,["pickStone","furnace","fuel"],[],4)
  addIngredient("minecraft:emerald",True,["pickIron"],[],10)
  addIngredient("minecraft:redstone",True,["pickIron"],[],6)
  addIngredient("minecraft:dye:4",True,["pickStone"],[],5)
  addIngredient("minecraft:dye",True,["swordWood"],[],0)
  addIngredient("minecraft:leaves",True,["shears"],[],0)
  addIngredient("minecraft:melon",True,[],[],2)
  addIngredient("minecraft:wheat_seeds",True,[],[],0)
  addIngredient("minecraft:pumpkin_seeds",False,[],[],0)
  addIngredient("minecraft:iron_nugget",False,[],[],0)
  addIngredient("minecraft:brick",True,["fuel","furnace"],[],2)
  addIngredient("minecraft:melon_seeds",False,[],[],0)
  addIngredient("minecraft:bowl",False,[],[],0)
  addIngredient("minecraft:dye:15",False,[],[],0)
  addIngredient("minecraft:carrot",True,[],[],2)
  addIngredient("minecraft:speckled_melon",False,[],[],0)
  addIngredient("minecraft:glass",True,["furnace","fuel"],[],1)
  addIngredient("minecraft:stone",True,["furnace","fuel"],[],1)
  addIngredient("minecraft:fermented_spider_eye",False,[],[],0)
  addIngredient("minecraft:golden_carrot",False,[],[],0)
  addIngredient("minecraft:sugar",False,[],[],0)
  addIngredient("minecraft:gold_nugget",False,[],[],0)
  addIngredient("minecraft:nether_wart",True,["flintSteel","obsidian"],[],6)
  addIngredient("minecraft:netherrack",True,["pickWood","flintSteel","obsidian"],[],1)
  addIngredient("minecraft:netherbrick",True,["pickWood","furnace","fuel","flintSteel","obsidian"],[],2)
  addIngredient("minecraft:gold_ingot",True,["pickIron","furnace","fuel"],[],3)
  addIngredient("minecraft:diamond",True,["pickIron"],[],7)
  addIngredient("minecraft:ender_pearl",True,["swordWood"],[],9)
  addIngredient("minecraft:feather",True,["swordWood"],[],1)
  addIngredient("minecraft:bone",True,["swordWood"],[],1)
  addIngredient("minecraft:snowball",True,["shovelWood"],[],1)
  addIngredient("minecraft:clay_ball",True,[],[],1)
  addIngredient("minecraft:leather",True,["swordWood"],[],1)
  addIngredient("minecraft:spider_eye",True,["swordWood"],[],4)
  addIngredient("minecraft:rabbit_foot",True,["swordWood"],[],6)
  addIngredient("minecraft:slime_ball",True,["swordWood"],[],5)
  addIngredient("minecraft:gunpowder",True,["swordStone"],[],3)
  addIngredient("minecraft:ghast_tear",True,["bow","arrow","flintSteel","obsidian"],[],7)
  addIngredient("minecraft:egg",True,[],[],3)
  addIngredient("minecraft:wool",True,["shears"],[],1)
  addIngredient("minecraft:book",False,[],[],0)
  addIngredient("minecraft:paper",False,[],[],0)
  addIngredient("minecraft:iron_block",False,[],[],0)
  addIngredient("minecraft:blaze_rod",True,["swordWood","flintSteel","obsidian"],[],6)
  addIngredient("minecraft:glowstone_dust",True,["flintSteel","obsidian"],[],3)
  addIngredient("minecraft:glowstone",False,[],[],0)
  addIngredient("minecraft:string",True,["swordWood"],[],2)
  addIngredient("minecraft:blaze_powder",False,[],[],0)
  addTool("minecraft:wooden_pickaxe",["pickWood"],[],7)
  addTool("minecraft:wooden_sword",["swordWood"],[],7)
  addTool("minecraft:chest",[],[],9)
  addTool("minecraft:cauldron",[],[],11)
  addTool("minecraft:bookshelf",[],[],9)
  addTool("minecraft:stone_button",[],[],6)
  addTool("minecraft:torch",[],[],5)
  addTool("minecraft:golden_rail",[],[],8)
  addTool("minecraft:rail",[],[],8)
  addTool("minecraft:minecart",[],[],6)
  addTool("minecraft:sign",[],[],5)
  addTool("minecraft:jukebox",[],[],12)
  addTool("minecraft:ender_chest",[],[],16)
  addTool("minecraft:ladder",[],[],5)
  addTool("minecraft:lever",[],[],6)
  addTool("minecraft:noteblock",[],[],9)
  addTool("minecraft:bed:14",[],[],7)
  addTool("minecraft:fence",[],[],8)
  addTool("minecraft:anvil",[],[],12)
  addTool("minecraft:redstone_lamp",[],[],10)
  addTool("minecraft:end_crystal",[],[],17)
  addTool("minecraft:fishing_rod",["fishing"],[],9)
  addTool("minecraft:ender_eye",[],[],11)
  addTool("minecraft:compass",[],[],8)
  addTool("minecraft:clock",[],[],8)
  addTool("minecraft:shears",["shears"],[],6)
  addTool("minecraft:brewing_stand",["brew"],[],8)
  addTool("minecraft:glass_bottle",["bottle"],[],6)
  addTool("minecraft:bow",["bow"],[],7)
  addTool("minecraft:arrow",["arrow"],[],4)
  addTool("minecraft:golden_sword",["swordWood"],[],8)
  addTool("minecraft:stone_sword",["swordWood","swordStone"],["swordWood"],10)
  addTool("minecraft:iron_sword",["swordWood","swordStone","swordIron"],["swordStone"],12)
  addTool("minecraft:diamond_sword",["swordWood","swordStone","swordIron","swordDiamond"],["swordIron"],14)
  addTool("minecraft:wooden_shovel",["shovelWood"],[],7)
  addTool("minecraft:golden_shovel",["shovelWood"],[],8)
  addTool("minecraft:stone_shovel",["shovelWood","shovelStone"],["shovelWood"],10)
  addTool("minecraft:iron_shovel",["shovelWood","shovelStone","shovelIron"],["shovelStone"],12)
  addTool("minecraft:diamond_shovel",["shovelWood","shovelStone","shovelIron","shovelDiamond"],["shovelIron"],14)
  addTool("minecraft:wooden_axe",["axeWood"],[],7)
  addTool("minecraft:golden_axe",["axeWood"],[],8)
  addTool("minecraft:stone_axe",["axeWood","axeStone"],["axeWood"],10)
  addTool("minecraft:iron_axe",["axeWood","axeStone","axeIron"],["axeStone"],12)
  addTool("minecraft:diamond_axe",["axeWood","axeStone","axeIron","axeDiamond"],["axeIron"],14)
  addTool("minecraft:leather_helmet",["helmetLeather"],[],7)
  addTool("minecraft:golden_helmet",["helmetGold","helmetLeather"],["helmetLeather"],8)
  addTool("minecraft:iron_helmet",["helmetLeather","helmetGold","helmetIron"],["helmetGold"],12)
  addTool("minecraft:diamond_helmet",["helmetLeather","helmetGold","helmetIron","helmetDiamond"],["helmetIron"],14)
  addTool("minecraft:leather_chestplate",["chestplateLeather"],[],7)
  addTool("minecraft:golden_chestplate",["chestplateGold","chestplateLeather"],["chestplateLeather"],8)
  addTool("minecraft:iron_chestplate",["chestplateLeather","chestplateGold","chestplateIron"],["chestplateGold"],12)
  addTool("minecraft:diamond_chestplate",["chestplateLeather","chestplateGold","chestplateIron","chestplateDiamond"],["chestplateIron"],14)
  addTool("minecraft:leather_leggings",["leggingsLeather"],[],7)
  addTool("minecraft:golden_leggings",["leggingsGold","leggingsLeather"],["leggingsLeather"],8)
  addTool("minecraft:iron_leggings",["leggingsLeather","leggingsGold","leggingsIron"],["leggingsGold"],12)
  addTool("minecraft:diamond_leggings",["leggingsLeather","leggingsGold","leggingsIron","leggingsDiamond"],["leggingsIron"],14)
  addTool("minecraft:leather_boots",["bootsLeather"],[],7)
  addTool("minecraft:golden_boots",["bootsGold","bootsLeather"],["bootsLeather"],8)
  addTool("minecraft:iron_boots",["bootsLeather","bootsGold","bootsIron"],["bootsGold"],12)
  addTool("minecraft:diamond_boots",["bootsLeather","bootsGold","bootsIron","bootsDiamond"],["bootsIron"],14)
  addTool("minecraft:bucket",["bucket"],[],9)
  addTool("minecraft:enchanting_table",["enchant"],[],18)
  addTool("minecraft:flint_and_steel",["flintSteel"],[],8)
  addTool("minecraft:golden_pickaxe",["pickWood"],[],8)
  addTool("minecraft:furnace",["furnace"],[],9)
  addTool("minecraft:crafting_table",["table"],[],7)
  addTool("minecraft:stone_pickaxe",["pickWood","pickStone"],["pickWood"],10)
  addTool("minecraft:iron_pickaxe",["pickWood","pickStone","pickIron"],["pickStone"],12)
  addTool("minecraft:diamond_pickaxe",["pickWood","pickStone","pickIron","pickDiamond"],["pickIron"],14)
  combList = ingredients+items
  random.shuffle(combList)
  i = 0
  for item in combList:
    if item.myClass == "ingredient":
      if item.canFind == True:
        temp = combList[0]
        combList[0] = item
        combList[i] = temp
    i += 1
  e = -1
  fails = 50
  possibleTags = []
  addRecipe("minecraft:log","[<minecraft:log:*>, null], [null, null]")
  addRecipe("minecraft:wool","[<minecraft:wool:*>, null], [null, null]")
  print("Working...")
  while (len(combList) > 0):
    e += 1
    if e >= len(combList):
      e = 0
      fails-=1
    if fails <= 0:
      Start()
      return
    item = combList[e]
    #print(e)
    #for x in combList:
      #print(x.name)
    #print(possibleTags)
    #print("------------------------------")
    if item.myClass == "ingredient":
      diff = 0
      if checkAllInList(possibleTags,item.requirements):
        if item.canFind == False:
          if len(generatedIngredients) > 0:
            if checkAllInList(possibleTags,["table"]):
              chose = generatedIngredients[random.randrange(0,len(generatedIngredients))]
              chosen = "[<"+chose.name+">"
              diff += chose.difficulty
              maxP = 0
              for p in range(0,random.randrange(0,9)):
                chose = generatedIngredients[random.randrange(0,len(generatedIngredients))]
                if p > 0:
                  if p == 2 or p == 5 or p == 8:
                    chosen = chosen+",<"+chose.name+">]"
                    diff += chose.difficulty
                  elif p == 3 or p == 6:
                    chosen = chosen+",[<"+chose.name+">"
                    diff += chose.difficulty
                  else:
                    chosen = chosen+",<"+chose.name+">"
                    diff += chose.difficulty
                maxP = p
              for p in range(maxP+1,9):
                if p == 2 or p == 5 or p == 8:
                    chosen = chosen+",null]"
                elif p == 3 or p == 6:
                    chosen = chosen+",[null"
                else:
                    chosen = chosen+",null"
              chosen = chosen+""
              if not chosen in recipesTableAdded:
                addRecipe(item.name,chosen)
                recentlyAdded = item.name
                generatedIngredients = generatedIngredients+[Ingredient(item.name,item.canFind,item.requirements,item.tags,diff)]
                #print("name: "+item.name+" --- diff: "+str(diff))
                deleteElement(combList,e)
                for tag in item.tags:
                  possibleTags = possibleTags+[tag,]
                e = -1
            else:
              chose = generatedIngredients[random.randrange(0,len(generatedIngredients))]
              chosen = "[<"+chose.name+">"
              diff += chose.difficulty
              maxP = 0
              for p in range(0,random.randrange(0,4)):
                chose = generatedIngredients[random.randrange(0,len(generatedIngredients))]
                if p > 0:
                  if p == 1 or p == 3:
                    chosen = chosen+",<"+chose.name+">]"
                    diff += chose.difficulty
                  elif p == 2:
                    chosen = chosen+",[<"+chose.name+">"
                    diff += chose.difficulty
                  else:
                    chosen = chosen+",<"+chose.name+">"
                    diff += chose.difficulty
                maxP = p
              for p in range(maxP+1,4):
                if p == 2:
                    chosen = chosen+",[null"
                elif p == 1 or p == 3:
                    chosen = chosen+",null]"
                else:
                    chosen = chosen+",null"
              chosen = chosen+""
              if not chosen in recipesTableAdded:
                addRecipe(item.name,chosen)
                recentlyAdded = item.name
                generatedIngredients = generatedIngredients+[Ingredient(item.name,item.canFind,item.requirements,item.tags,diff)]
                #print("name: "+item.name+" --- diff: "+str(diff))
                deleteElement(combList,e)
                for tag in item.tags:
                  possibleTags = possibleTags+[tag,]
                e = -1
        else:
          generatedIngredients = generatedIngredients+[item]
          recentlyAdded = item.name
          deleteElement(combList,e)
          for tag in item.tags:
            possibleTags = possibleTags+[tag,]
          e = -1
    elif item.myClass == "item":
      if checkAllInList(possibleTags,item.requirements):
        if len(generatedIngredients) > 0:
          if checkAllInList(possibleTags,["table"]):
                chose = generatedIngredients[random.randrange(0,len(generatedIngredients))]
                chosen = "[<"+chose.name+">"
                diff += chose.difficulty
                maxP = 0
                for p in range(0,random.randrange(0,9)):
                  chose = Ingredient("ERROR",False,[],[],1000)
                  if len(addItemToRecipe([],diff,item.difficulty)) > 0:
                    chose = addItemToRecipe([],diff,item.difficulty)[random.randrange(0,len(addItemToRecipe([],diff,item.difficulty)))]
                  if p > 0:
                    if p == 2 or p == 5 or p == 8:
                      if chose.name == "ERROR":
                        chosen = chosen+",null]"
                      else:
                        chosen = chosen+",<"+chose.name+">]"
                        diff += chose.difficulty
                    elif p == 3 or p == 6:
                      if chose.name == "ERROR":
                        chosen = chosen+",[null"
                      else:
                        chosen = chosen+",[<"+chose.name+">"
                        diff += chose.difficulty
                    else:
                      if chose.name == "ERROR":
                        chosen = chosen+",null"
                      else:
                        chosen = chosen+",<"+chose.name+">"
                        diff += chose.difficulty
                  maxP = p
                for p in range(maxP+1,9):
                  if p == 2 or p == 5 or p == 8:
                      chosen = chosen+",null]"
                  elif p == 3 or p == 6:
                      chosen = chosen+",[null"
                  else:
                      chosen = chosen+",null"
                chosen = chosen+""
                if not chosen in recipesTableAdded:
                  #print("name: "+item.name+" --- min: "+str(diff)+" -> max: "+str(item.difficulty))
                  addRecipe(item.name,chosen)
                  deleteElement(combList,e)
                  for tag in item.tags:
                    possibleTags = possibleTags+[tag,]
                  e = -1
          else:
                chose = generatedIngredients[random.randrange(0,len(generatedIngredients))]
                chosen = "[<"+chose.name+">"
                diff += chose.difficulty
                maxP = 0
                for p in range(0,random.randrange(0,4)):
                  chose = Ingredient("ERROR",False,[],[],1000)
                  if len(addItemToRecipe([],diff,item.difficulty)) > 0:
                    chose = addItemToRecipe([],diff,item.difficulty)[random.randrange(0,len(addItemToRecipe([],diff,item.difficulty)))]
                  if p > 0:
                    if p == 1 or p == 3:
                      if chose.name == "ERROR":
                        chosen = chosen+",null]"
                      else:
                        chosen = chosen+",<"+chose.name+">]"
                        diff += chose.difficulty
                    elif p == 2:
                      if chose.name == "ERROR":
                        chosen = chosen+",[null"
                      else:
                        chosen = chosen+",[<"+chose.name+">"
                        diff += chose.difficulty
                    else:
                      if chose.name == "ERROR":
                        chosen = chosen+",null"
                      else:
                        chosen = chosen+",<"+chose.name+">"
                        diff += chose.difficulty
                  maxP = p
                for p in range(maxP+1,4):
                  if p == 2:
                      chosen = chosen+",[null"
                  elif p == 1 or p == 3:
                      chosen = chosen+",null]"
                  else:
                      chosen = chosen+",null"
                chosen = chosen+""
                if not chosen in recipesTableAdded:
                  #print("name: "+item.name+" --- min: "+str(diff)+" -> max: "+str(item.difficulty))
                  addRecipe(item.name,chosen)
                  deleteElement(combList,e)
                  for tag in item.tags:
                    possibleTags = possibleTags+[tag,]
                  e = -1
  e += 1
  #print(e)
  #for x in combList:
    #print(x.name)
  #print(possibleTags)
  #print("------------------------------")
  try: 
    os.mkdir(directory_path+'/oldgeneration') 
  except OSError: 
    print("Old generation folder found...")
  try: 
    os.mkdir(directory_path+'/scripts') 
  except OSError: 
    print("Scripts folder found...")
  for file in os.listdir(directory_path+'/scripts'):
    shutil.move(directory_path+'/scripts/'+file, directory_path+'/oldgeneration/'+file)
  with open(directory_path+'/scripts/recipes'+str(seed)+'.zs', 'w') as f:
      temp = ""
      for entry in recipesAdded:
        temp = temp+entry
      f.write("//#Remove\nrecipes.removeAll();\n//#Add\n"+temp+"//File End")
      print("Made recipes.zs file...")
  try: 
    os.mkdir(directory_path+'/spoiler') 
  except OSError: 
    print("Spoilers folder found...")
  for file in os.listdir(directory_path+'/spoiler'):
    shutil.move(directory_path+'/spoiler/'+file, directory_path+'/oldgeneration/'+file)
  with open(directory_path+'/spoiler/spoiler'+str(seed)+'.txt', 'w') as f:
      f.write(spoilerList)
      print("Made spoilers file...")
  print("DONE!")
  input("Your seed is "+str(seed)+".\nEnter to close.")