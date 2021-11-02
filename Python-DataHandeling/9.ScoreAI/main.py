import json
import csv

old="json"
new="csv"

path=input("Mi a konvertálandó fájl útvonala: ")
source=open(path,"r")
data=json.load(source)
source.close()
csv_path=path.replace(old, new)
csv_file=csv.writer(open(csv_path,"w"))

print(data)
print(path)
print(csv_path)