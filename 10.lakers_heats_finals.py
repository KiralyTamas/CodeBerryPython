final_score=[116,124,115,102,111,106]
first_quarter=[2,2,2,1,1,3,2,2,2,2,2,2,2,2,1]
lakers_starters=["L. James","A. Davis","D. Green","K. Caldwell-Pope","A. Caruso"]

def count_matches(score):
  print("A Lakers "+str(len(score))+" meccset játszott le a fináléban")

def count_points(list,point):
  if point==1:
    print("A(z) első negyedben "+str(list.count(point))+" darab egypontos dobás volt.")
  elif point==2:
    print("A(z) első negyedben "+str(list.count(point))+" darab kétpontos dobás volt.")
  elif point==3:
    print("A(z) első negyedben "+str(list.count(point))+" darab hárompontos dobás volt.")

def get_min_score(list):
  return min(list)

def get_max_score(list):
  return max(list)

def get_game_number(list,number):
  return list.index(number)

def print_final_stat(list):
  print("A fináléban játszott mérkőzések közül a legalacsonyabb pontszámú a "+str(get_game_number(list, get_min_score(list))+1)+". meccs volt "+str(get_min_score(list))+" ponttal.")
  print("A fináléban játszott mérkőzések közül a legmagasabb pontszámú a "+str(get_game_number(list, get_max_score(list))+1)+". meccs volt "+str(get_max_score(list))+" ponttal.")

def print_starters(list, name):
  if name in list:
    print(name+" benne van a kezdőcsapatban.")
  else:
    print(name+" a cserepadon van.")

count_matches(final_score)
count_points(first_quarter, 1)
count_points(first_quarter, 2)
count_points(first_quarter, 3)
print_final_stat(final_score)
print_starters(lakers_starters, "L. James")