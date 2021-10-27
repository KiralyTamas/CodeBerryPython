def file_opener():
  my_file = open("data1.txt","x")
  my_file = open("data1.txt","w")
  my_file.write("Kutyafutty")
  my_file.close()
file_opener()