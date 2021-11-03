import json
import csv

old="json"
new="csv"
data=[]
path=input("Mi a konvertálandó fájl útvonala: ")
source=open(path,"r")
data=json.load(source)
source.close()
csv_path=path.replace(old, new)
csv_file=csv.writer(open(csv_path,"w"))

def convert_header(data,delim):
  header=[]
  content=[]
  for number in data:
    for i in number.keys():
      if isinstance(number[i], dict):
        for j in number[i].keys():
          header.append(str(i)+delim+str(j))
      header.append(i)
      if isinstance(number[i], dict):
        header.remove(i)
    for i in number.keys():
      if isinstance(number[i], dict):
        for j in number[i]:
          content.append(number[i][j])
      content.append(number[i])

  csv_file.writerow(header)
  csv_file.writerow(content)

convert_header(data, "_")