import os

def recipe_reader():
  recipe_list=[]
  my_recipe=open("Text/recipe.txt","r")
  recipe_list=my_recipe.read()
  print(recipe_list)
  my_recipe.close()

recipe_reader()