def file_opener():
  my_file = open("Text/data1.txt","x")
  my_file = open("Text/data1.txt","w")
  my_file.write("Kutyafutty")
  my_file = open("Text/data1.txt","r")
  content=my_file.read()
  print(content)
  my_file.close()

file_opener()