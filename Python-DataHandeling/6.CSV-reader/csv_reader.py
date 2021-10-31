import csv
import sys

def read_csv(file_name):
    csv_list = []
    try:
      try:
        file = open(file_name)
      except FileNotFoundError:
        print("Hiba a fájl beolvasása közben!")
        exit("Valami baj van a fájl elérési útvonalával")
      try:
        file_content = csv.reader(file)
      except FloatingPointError:
        print("Baj van a fájl formátumával")
        exit("Minden rendben van a fájl struktúrájával?")
      try:
        for record in file_content:
          csv_list.append(record)
      except KeyError:
        print("Para")
        exit("Csak")
    except KeyError:
      print("Baj")
      exit("Csak")
    file.close()
    return csv_list

print(read_csv("CSV\meetup.csv"))