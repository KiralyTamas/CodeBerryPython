import read_csv

def calculate_actions(prisoners_content):
    free_prisoners = []
    prisoners = []
    for number in prisoners_content:
        prisoners.append(number)
    for number in range(1, len(prisoners)):
        for klick in prisoners:
            if int(klick[0]) % number == 0:
                if int(klick[1]) == 0:
                    klick[1] = 1
                else:
                    klick[1] = 0
    for door in prisoners:
        if int(door[1]) == 1:
            free_prisoners.append(door[0])
    print("A következő számú rabok lettek szabadok: "+str(free_prisoners))
    print("Összesen "+str(len(free_prisoners))+" rab lett szabad!")