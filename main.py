import os
import random
import sys
class Ingredient:
  name = ""
  tags = []
  canFind = False
  requirements = []
  myClass = "ingredient"
  def __init__(self,idSet,canFindSet,requirementsSet,tagSet):
    self.name = idSet
    self.canFind = canFindSet
    self.requirements = requirementsSet
    self.tags = tagSet

def deleteElement(list_object, pos):
    if pos < len(list_object):
        list_object.pop(pos)

class Item:
  name = ""
  tags = []
  myClass = "item"
  requirements = []
  def __init__(self,idSet,tagSet,requirementsSet):
    self.name = idSet
    self.tags = tagSet
    self.requirements = requirementsSet
def checkAllInList(checkedList,toFind):
  for item in toFind:
    if not item in checkedList:
      return False
  return True

def addIngredient(item,canFind,requirements,tags):
  global ingredients
  ingredients = ingredients+[Ingredient(item,canFind,requirements,tags),]
def addTool(it,tags,requirements):
  global items
  items = items+[Item(it,tags,requirements),]
def addRecipe(result, ingredients):
  global recipesAdded
  global recipesTableAdded
  recipesTableAdded = recipesTableAdded+[ingredients]
  recipesAdded = recipesAdded+["recipes.addShaped(<"+result+">,["+ingredients+"]);\n",]
directory_path = os.getcwd()
recipesAdded = []
items = []
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
  addIngredient("minecraft:log",True,[],[])
  addIngredient("minecraft:reeds",True,[],[])
  addIngredient("minecraft:sand",True,[],[])
  addIngredient("minecraft:flint",True,[],[])
  addIngredient("minecraft:stick",False,[],[])
  addIngredient("minecraft:planks",False,[],[])
  addIngredient("minecraft:obsidian",True,["pickDiamond","bucket"],["obsidian"])
  addIngredient("minecraft:quartz",True,["pickWood","flintSteel","obsidian"],[])
  addIngredient("minecraft:magma_cream",True,["swordWood","flintSteel","obsidian"],[])
  addIngredient("ore:cobblestone",True,["pickWood"],[])
  addIngredient("minecraft:coal",True,["pickWood"],["fuel"])
  addIngredient("minecraft:iron_ingot",True,["pickStone","furnace","fuel"],[])
  addIngredient("minecraft:emerald",True,["pickIron"],[])
  addIngredient("minecraft:redstone",True,["pickIron"],[])
  addIngredient("minecraft:dye:4",True,["pickStone"],[])
  addIngredient("minecraft:leaves",True,["shears"],[])
  addIngredient("minecraft:melon",True,[],[])
  addIngredient("minecraft:carrot",True,[],[])
  addIngredient("minecraft:speckled_melon",False,[],[])
  addIngredient("minecraft:glass",False,["furnace","fuel"],[])
  addIngredient("minecraft:stone",False,["furnace","fuel"],[])
  addIngredient("minecraft:fermented_spider_eye",False,[],[])
  addIngredient("minecraft:golden_carrot",False,[],[])
  addIngredient("minecraft:sugar",False,[],[])
  addIngredient("minecraft:gold_nugget",False,[],[])
  addIngredient("minecraft:nether_wart",True,["flintSteel","obsidian"],[])
  addIngredient("minecraft:netherrack",True,["pickWood","flintSteel","obsidian"],[])
  addIngredient("minecraft:netherbrick",True,["pickWood","furnace","fuel","flintSteel","obsidian"],[])
  addIngredient("minecraft:gold_ingot",True,["pickIron","furnace","fuel"],[])
  addIngredient("minecraft:diamond",True,["pickIron"],[])
  addIngredient("minecraft:ender_pearl",True,["swordWood"],[])
  addIngredient("minecraft:leather",True,["swordWood"],[])
  addIngredient("minecraft:spider_eye",True,["swordWood"],[])
  addIngredient("minecraft:rabbit_foot",True,["swordWood"],[])
  addIngredient("minecraft:blaze_rod",True,["swordWood","flintSteel","obsidian"],[])
  addIngredient("minecraft:string",True,["swordWood"],[])
  addIngredient("minecraft:blaze_powder",False,[],[])
  addTool("minecraft:wooden_pickaxe",["pickWood"],[])
  addTool("minecraft:wooden_sword",["swordWood"],[])
  addTool("minecraft:chest",[],[])
  addTool("minecraft:cauldron",[],[])
  addTool("minecraft:fishing_rod",["fishing"],[])
  addTool("minecraft:ender_eye",[],[])
  addTool("minecraft:compass",[],[])
  addTool("minecraft:shears",["shears"],[])
  addTool("minecraft:brewing_stand",["brew"],[])
  addTool("minecraft:glass_bottle",["bottle"],[])
  addTool("minecraft:bow",[],[])
  addTool("minecraft:arrow",[],[])
  addTool("minecraft:golden_sword",["swordWood"],[])
  addTool("minecraft:stone_sword",["swordWood","swordStone"],["swordWood"])
  addTool("minecraft:iron_sword",["swordWood","swordStone","swordIron"],["swordStone"])
  addTool("minecraft:diamond_sword",["swordWood","swordStone","swordIron","swordDiamond"],["swordIron"])
  addTool("minecraft:wooden_shovel",["shovelWood"],[])
  addTool("minecraft:golden_shovel",["shovelWood"],[])
  addTool("minecraft:stone_shovel",["shovelWood","shovelStone"],["shovelWood"])
  addTool("minecraft:iron_shovel",["shovelWood","shovelStone","shovelIron"],["shovelStone"])
  addTool("minecraft:diamond_shovel",["shovelWood","shovelStone","shovelIron","shovelDiamond"],["shovelIron"])
  addTool("minecraft:wooden_axe",["axeWood"],[])
  addTool("minecraft:golden_axe",["axeWood"],[])
  addTool("minecraft:stone_axe",["axeWood","axeStone"],["axeWood"])
  addTool("minecraft:iron_axe",["axeWood","axeStone","axeIron"],["axeStone"])
  addTool("minecraft:diamond_axe",["axeWood","axeStone","axeIron","axeDiamond"],["axeIron"])
  addTool("minecraft:leather_helmet",["helmetLeather"],[])
  addTool("minecraft:golden_helmet",["helmetGold","helmetLeather"],["helmetLeather"])
  addTool("minecraft:iron_helmet",["helmetLeather","helmetGold","helmetIron"],["helmetGold"])
  addTool("minecraft:diamond_helmet",["helmetLeather","helmetGold","helmetIron","helmetDiamond"],["helmetIron"])
  addTool("minecraft:leather_chestplate",["chestplateLeather"],[])
  addTool("minecraft:golden_chestplate",["chestplateGold","chestplateLeather"],["chestplateLeather"])
  addTool("minecraft:iron_chestplate",["chestplateLeather","chestplateGold","chestplateIron"],["chestplateGold"])
  addTool("minecraft:diamond_chestplate",["chestplateLeather","chestplateGold","chestplateIron","chestplateDiamond"],["chestplateIron"])
  addTool("minecraft:leather_leggings",["leggingsLeather"],[])
  addTool("minecraft:golden_leggings",["leggingsGold","leggingsLeather"],["leggingsLeather"])
  addTool("minecraft:iron_leggings",["leggingsLeather","leggingsGold","leggingsIron"],["leggingsGold"])
  addTool("minecraft:diamond_leggings",["leggingsLeather","leggingsGold","leggingsIron","leggingsDiamond"],["leggingsIron"])
  addTool("minecraft:leather_boots",["bootsLeather"],[])
  addTool("minecraft:golden_boots",["bootsGold","bootsLeather"],["bootsLeather"])
  addTool("minecraft:iron_boots",["bootsLeather","bootsGold","bootsIron"],["bootsGold"])
  addTool("minecraft:diamond_boots",["bootsLeather","bootsGold","bootsIron","bootsDiamond"],["bootsIron"])
  addTool("minecraft:bucket",["bucket"],[])
  addTool("minecraft:flint_and_steel",["flintSteel"],[])
  addTool("minecraft:golden_pickaxe",["pickWood"],[])
  addTool("minecraft:furnace",["furnace"],[])
  addTool("minecraft:crafting_table",["table"],[])
  addTool("minecraft:stone_pickaxe",["pickWood","pickStone"],["pickWood"])
  addTool("minecraft:iron_pickaxe",["pickWood","pickStone","pickIron"],["pickStone"])
  addTool("minecraft:diamond_pickaxe",["pickWood","pickStone","pickIron","pickDiamond"],["pickIron"])
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
  while (len(combList) > 0):
    e += 1
    if e >= len(combList):
      e = 0
      fails-=1
    if fails <= 0:
      Start()
      return
    item = combList[e]
    print(e)
    for x in combList:
      print(x.name)
    print(possibleTags)
    print("------------------------------")
    if item.myClass == "ingredient":
      if checkAllInList(possibleTags,item.requirements):
        if item.canFind == False:
          if len(generatedIngredients) > 0:
            if checkAllInList(possibleTags,["table"]):
              chosen = "[<"+recentlyAdded+">"
              maxP = 0
              for p in range(0,random.randrange(0,9)):
                if p > 0:
                  if p == 2 or p == 5 or p == 8:
                    chosen = chosen+",<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">]"
                  elif p == 3 or p == 6:
                    chosen = chosen+",[<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
                  else:
                    chosen = chosen+",<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
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
                generatedIngredients = generatedIngredients+[item.name]
                deleteElement(combList,e)
                for tag in item.tags:
                  possibleTags = possibleTags+[tag,]
                e = -1
            else:
              chosen = "[<"+recentlyAdded+">"
              maxP = 0
              for p in range(0,random.randrange(0,9)):
                if p > 0:
                  if p == 2 or p == 5 or p == 8:
                    chosen = chosen+",null]"
                  elif p == 6:
                    chosen = chosen+",[null"
                  elif p == 7:
                    chosen = chosen+",null"
                  elif p == 3:
                    chosen = chosen+",[<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
                  else:
                    chosen = chosen+",<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
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
                generatedIngredients = generatedIngredients+[item.name]
                deleteElement(combList,e)
                for tag in item.tags:
                  possibleTags = possibleTags+[tag,]
                e = -1
        else:
          generatedIngredients = generatedIngredients+[item.name]
          recentlyAdded = item.name
          deleteElement(combList,e)
          for tag in item.tags:
            possibleTags = possibleTags+[tag,]
          e = -1
    elif item.myClass == "item":
      if checkAllInList(possibleTags,item.requirements):
        if len(generatedIngredients) > 0:
          if checkAllInList(possibleTags,["table"]):
                chosen = "[<"+recentlyAdded+">"
                maxP = 0
                for p in range(0,random.randrange(0,9)):
                  if p > 0:
                    if p == 2 or p == 5 or p == 8:
                      chosen = chosen+",<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">]"
                    elif p == 3 or p == 6:
                      chosen = chosen+",[<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
                    else:
                      chosen = chosen+",<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
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
                  deleteElement(combList,e)
                  for tag in item.tags:
                    possibleTags = possibleTags+[tag,]
                  e = -1
          else:
                chosen = "[<"+recentlyAdded+">"
                maxP = 0
                for p in range(0,random.randrange(0,9)):
                  if p > 0:
                    if p == 2 or p == 5 or p == 8:
                      chosen = chosen+",null]"
                    elif p == 6:
                      chosen = chosen+",[null"
                    elif p == 7:
                      chosen = chosen+",null"
                    elif p == 3:
                      chosen = chosen+",[<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
                    else:
                      chosen = chosen+",<"+generatedIngredients[random.randrange(0,len(generatedIngredients))]+">"
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
                  deleteElement(combList,e)
                  for tag in item.tags:
                    possibleTags = possibleTags+[tag,]
                  e = -1
  e += 1
  print(e)
  for x in combList:
    print(x.name)
  print(possibleTags)
  print("------------------------------")
  with open(directory_path+'/recipes.zs', 'w') as f:
      temp = ""
      for entry in recipesAdded:
        temp = temp+entry
      f.write("//#Remove\nrecipes.removeAll();\n//#Add\n"+temp+"//File End")
  print("DONE!")
Start()