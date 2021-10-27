lakers_players = (('A. Davis', 3), ('L. James', 23), ('D. Green', 14), ('K. Caldwell-Pope', 1), ('A. Caruso', 4), ('M. Morris', 88),
                  ('J. Dudley', 10), ('K. Kuzma', 0), ('D. Howard', 39), ('R. Rondo', 9), ('Q. Cook', 28), ('J. McGee', 7), ('J. Smith', 21))

lakers_final_game = ((1, 2, 3), (1, 2, 23), (1, 2, 23), (1, 1, 1), (1, 1, 1), (1, 3, 14), (1, 2, 23), (1, 2, 9), (1, 2, 1), (1, 2, 3), (1, 2, 9), (1, 2, 3), (1, 2, 3), (1, 2, 23), (1, 1, 23), (2, 2, 9), (2, 3, 9), (2, 2, 23), (2, 3, 88), (2, 2, 4), (2, 2, 9), (2, 2, 9), (2, 2, 3), (2, 2, 1), (2, 1, 1), (2, 1, 3), (2, 1, 3), (2, 1, 3), (2, 2, 3), (2, 2, 1), (2, 2, 4), (2, 3, 1), (2, 3, 1), (3, 2, 23), (3, 3, 14), (3, 2, 23), (3, 2, 14), (3, 2, 1), (3, 2, 0), (3, 2, 23), (3, 3, 9), (3, 2, 23), (3, 3, 9), (4, 3, 14), (4, 2, 3), (4, 1, 3), (4, 1, 3), (4, 3, 23), (4, 2, 23), (4, 2, 23), (4, 2, 23), (4, 3, 39))


def get_jersey_number(player_list, name):
    for player in player_list:
        if name in player[0]:
            return player[1]


def get_player_score_in_quarter(lakers_scores, quarter_number, player_number):
    sum_score = 0
    for score in lakers_scores:
        if quarter_number == score[0] and player_number == score[2]:
            sum_score += score[1]
    return sum_score


def print_player_stat_in_quarter(lakers_scores, player_list, quarter_number, name, point):
    number_point = 0
    print(name+" statisztikája a(z) "+str(quarter_number)+". negyedben:")
    if get_player_score_in_quarter(lakers_scores, quarter_number, get_jersey_number(player_list, name)) > 0:
        print("Elért pontok: "+str(get_player_score_in_quarter(lakers_scores,
              quarter_number, get_jersey_number(player_list, name))))
    else:
        print("Nem ért el pontot a negyedben")
    if get_player_score_in_quarter(lakers_scores, quarter_number, get_jersey_number(player_list, name)) > 0:
        for score in lakers_scores:
            if quarter_number == score[0] and get_jersey_number(player_list, name) == score[2] and point == score[1]:
                number_point += 1
        print(str(point)+" pontos dobások száma: "+str(number_point))
    print("")


print_player_stat_in_quarter(
    lakers_final_game, lakers_players, 3, 'D. Green', 3)
print_player_stat_in_quarter(
    lakers_final_game, lakers_players, 1, 'J. Smith', 2)
print_player_stat_in_quarter(
    lakers_final_game, lakers_players, 2, 'A. Davis', 1)
