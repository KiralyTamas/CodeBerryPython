coordinate1=('47,29,56.29')
coordinate2=('19,02,36.97')
string1=["Északi szélesség "," fok "," perc "," másodperc"]
string2=["Keleti hosszúság "," fok "," perc "," másodperc"]
def print_coordinates(string,coordinate):
  print("A Lánchíd a következő koordináták alatt található:")
  for number in range(0,2):
    print(string[number][0]+coordinate[number][0:2]+string[number][1]+coordinate[number][3:5]+string[number][2]+coordinate[number][6:]+string[number][3])

print_coordinates((string1, string2),(coordinate1, coordinate2))