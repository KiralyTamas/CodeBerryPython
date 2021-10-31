import source_data
players_list= source_data.csv_reader("CSV\lakers_players.csv","CSV\lakers_score.csv")[0]
lakers_scores= source_data.csv_reader("CSV\lakers_players.csv","CSV\lakers_score.csv")[1]

def get_jersey_number(players_list, name):
    for player in players_list:
        if name in player[0]:
          return player[1]


def get_player_score_in_quarter(lakers_scores, quarter_number, player_number):
    sum_score = 0
    for score in lakers_scores:
        if int(quarter_number) == int(score[0]) and int(player_number) == int(score[2]):
            sum_score += int(score[1])
    return sum_score


def print_player_stat_in_quarter(lakers_scores, players_list, quarter_number, name, point):
    number_point = 0
    print(name+" statisztikája a(z) "+str(quarter_number)+". negyedben:")
    if get_player_score_in_quarter(lakers_scores, quarter_number, get_jersey_number(players_list, name)) > 0:
        print("Elért pontok: "+str(get_player_score_in_quarter(lakers_scores,
              quarter_number, get_jersey_number(players_list, name))))
    else:
        print("Nem ért el pontot a negyedben")
    if get_player_score_in_quarter(lakers_scores, quarter_number, get_jersey_number(players_list, name)) > 0:
        for score in lakers_scores:
            if int(quarter_number) == int(score[0]) and int(get_jersey_number(players_list, name)) == int(score[2]) and int(point) == int(score[1]):
                number_point += 1
        print(str(point)+" pontos dobások száma: "+str(number_point))
    print("")