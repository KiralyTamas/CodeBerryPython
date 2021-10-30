def file_reading(file_name):
  try:
    try:
      file=open(file_name,"r")
    except NameError:
      print("Valami nem jó")
    else:
      content=file.read()
      print(content)
      file.close()
  except OSError:
    print("Hiba a fájl kezelése közben!")
  finally:
    print("Kérdezés Vége")

def get_file_name():
    return input("Mi a fájl elérési útvonala? ")

file_reading(get_file_name())