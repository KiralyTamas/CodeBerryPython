count = 0
card = ["123453443553535", "9876546843546546835", "456765246543852538"]
while count < len(card):
    if int(card[count][:4]) == int(1234):
        print("A "+str(card[count][:4]) +" számú kártya a Gringotts Varázslóbank tulajdona.")
    elif int(card[count][:4]) == int(9876):
        print("A "+str(card[count][:4]) +" számú kártya a Galaktikus Birodalom kizárólagos tulajdona.")
    elif int(card[count][:4]) == int(4567):
        print("A "+str(card[count][:4]) +" számú kártya Dagobert bácsi széfjének tulajdonát képezi.")
    count+=1