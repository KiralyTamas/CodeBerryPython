def file_reading(file_name):
  try:
    file=open(file_name,"r")
    content=file.read()
    print(content)
    file.close()
  except FileNotFoundError():
    print("Ilyen fájl nem található")

def get_file_name():
    return input("Mi a fájl elérési útvonala?" )

file_reading(get_file_name())