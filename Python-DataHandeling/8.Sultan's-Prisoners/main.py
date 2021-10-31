def fill_csv():
  file=open("CSV\data.csv","w")
  for number in range(1000):
    file.writelines(number+","+0)
  file.close()

fill_csv()