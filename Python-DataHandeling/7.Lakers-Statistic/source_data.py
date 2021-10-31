import csv

def csv_reader(player_data,score_data):
  players=[]
  scores=[]
  player=open(player_data,"r")
  score=open(score_data,"r")
  player_content=csv.reader(player)
  score_content=csv.reader(score)
  for record1 in player_content:
    players.append(tuple(record1))
  for record2 in score_content:
    scores.append(tuple(record2))
  return players,scores