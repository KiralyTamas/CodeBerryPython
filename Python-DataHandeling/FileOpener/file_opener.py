def file_opener():
  my_file = open("text.txt","r")
  print(my_file.read())
  my_file.close()
file_opener()