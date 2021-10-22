favorite_team=["Armstrong B.J.","Cartwright Bill","Grant Horace","Hodger Craig","Hopson Dennis","Jordan Michael","King Stacey","Levingston Cliff","Paxson John","Perdue Will","Pippen Scottie","Williams Scott"]
los_angeles_lakers=[]
print(favorite_team[0])
print(favorite_team[1])
print(favorite_team[-1])
print(favorite_team[-2])
print(favorite_team[-3])

def get_middle_people(people):
  array_len=len(people)
  middle_array_len=array_len/3
  print(people[int(middle_array_len):int(middle_array_len*2)])

def remove_injured_players(index):
  favorite_team[index]="injured"
  print(favorite_team)

def add_new_player(team, player):
  team.append(player)
  print(team)

def add_captain(team):
  team.insert(0,team[5])
  print(team)

def remove_player(team, player):
  team.remove(player)
  print(team)

def del_player(team):
  del team[5]
  del team[-2:]
  print(team)

def transfer_player(our_team,rival_team,player_index):
  rival_team=our_team.pop(player_index)
  print(our_team)
  print(rival_team)

get_middle_people(favorite_team)
remove_injured_players(1)
remove_injured_players(3)
remove_injured_players(8)
add_new_player(favorite_team, "Kukoc")
add_captain(favorite_team)
remove_player(favorite_team, "Hopson Dennis")
del_player(favorite_team)
transfer_player(favorite_team,los_angeles_lakers,3)