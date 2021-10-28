import os

def recipe_reader():
  if os.path.exists("Text/recipe.txt"):
    my_recipe=open("Text/recipe.txt","w")
    my_recipe.writelines(["fott krumpli","\ntojas","\nkolbasz","\ntejfol","\nreszelt sajt"])
    my_recipe=open("Text/recipe.txt","r")
    content=[my_recipe.read()]
    print(content)
    my_recipe.close()
  else:
    os.mkdir("Text")
    my_recipe=open("Text/recipe.txt","x")
    my_recipe.close()

recipe_reader()