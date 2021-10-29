def write_favorite_characters_into_a_file(file_name):
  character=input("Mi a karakter neve?")
  file=open(file_name,"w")
  file.write(character)
  file.close()

write_favorite_characters_into_a_file("Text/characters.txt")