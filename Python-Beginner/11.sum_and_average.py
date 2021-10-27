scores_this_season=[116,124,115,102,111,106,99,90]

def sum_of_scores(list):
  sum_score=0
  for score in list:
    sum_score+=score
  return sum_score

def calculate_average(list, sum):
  number_of_scores=len(list)
  average_score=sum/number_of_scores
  print("A csapat az elmúlt "+str(number_of_scores)+" meccsen átlagosan "+str(average_score)+" pontot szerzett.")

calculate_average(scores_this_season, sum_of_scores(scores_this_season))