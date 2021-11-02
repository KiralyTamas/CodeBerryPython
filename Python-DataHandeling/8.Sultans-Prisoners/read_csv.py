import csv


def free_prisoner():
    prison = open(input("Kérem adja meg a fájl relatív útvonalát, amivel számolni kell: "))
    prisoners_content = csv.reader(prison)
    return prisoners_content