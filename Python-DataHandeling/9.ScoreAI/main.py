import json
import csv

old="json"
new="csv"
data_1=[]
path=input("Mi a konvertálandó fájl útvonala: ")
source=open(path,"r")
data=json.load(source)
source.close()
data_1=data[0]
csv_path=path.replace(old, new)
csv_file=csv.writer(open(csv_path,"w"))
for i in data_1:
  if isinstance(data_1[i], dict):
    for j in data_1[i]:
      print(data_1[i][j])

csv_file.writerow(data_1.keys())
csv_file.writerow(data_1.values())
print(data_1)
print(data_1.keys())