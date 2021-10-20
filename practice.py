print('Szép cica, jó cica,\nSelymes a bundád.\nKedves cica, álmos cica,\nBújj hozzám.')

print("A ház nem hivatalos, ám közismert jelmondata: 'Egy Lannister mindig megfizeti az adósságait.'\nA valódi jelmondatuk ezzel szemben: 'Halld üvöltésem!'")

print(str(101)+" kiskutya")

print('"Ne akarj másnak látszani, mint aminek látszol, mert ha nem annak akarsz látszani, aminek látszol, akkor nem annak látszol, aminek látszani akarnál." – Alice Tükörországban' ==
      '"Ne akarj másnak látszani, mint aminek látszol. Mert ha nem annak akarsz látszani, aminek látszol, akkor nem annak látszol, aminek látszani akarnál." – Alice Tükörországban')

print('Batman and RObin' != 'Barney and Robin')
gas_prize = 384
print(600*6.5/100*gas_prize)

ultimate_answer = 1890/90*2
if int(ultimate_answer)==42:
      print('A válasz az életre, a világmindenségre, meg mindenre: ' + str(ultimate_answer))

cheese_type='parmezán'
side_dish='ciabattával'
def print_tomato_soup_recipe(cheese_type, side_dish):
      print('Pirítsd meg olivaolajon a hagymát és foghagymát.')
      print('Tedd hozzá a felkockázott paradicsomot, sózd és borsozd meg, majd öntsd fel 2 dl vizzel.')
      print('Főzd kis lángon 15-20 percig.')
      print('Ha szétfőtt a paradicsom, add hozzá a száraz kenyeret, olivaolajat, bazsalikomot, és adj hozzá egy kis vizet.')
      print('Főzd még 5 percig.')
      print('Szórj rá reszelt '+cheese_type+"-t")
      print('Szolgáld fel '+side_dish+'.')
print_tomato_soup_recipe(cheese_type, side_dish)

sauce="szósz"
meet="hús"
cheese="sajt"
tomato="paradicsom"
def print_sandwich_recipe(sauce,meet,cheese,tomato):
      print("Fogj két szelet kenyeret.")
      print("Az egyik szeletre nyomj "+sauce+"-t.")
      print("Helyezz a kenyérre két szelet "+meet+"-t.")
      print("Rakj rá egy szelet "+cheese+"-ot.")
      print("Koronázd meg pár szelet ilyen zöldséggel: "+tomato+".")
      print("Borítsd be a szendvicset a másik szelet kenyérrel.")
      print("Jó étvágyat!")
print_sandwich_recipe(sauce,meet,cheese,tomato)

def calculate_rectangle_area(width,height):
      return width*height

def print_rectangle_area(width_from_user,height_from_user):
      area=calculate_rectangle_area(width_from_user,height_from_user)
      print("A négyzet területe "+str(area)+" négyzetméter")
print_rectangle_area(10,40)

def print_poem():
      print("Egy - megérett a meggy")
      print("Kettő - Csipkebokor vessző")
      return 'Stop!'
      print("Három - Te vag az én párom")
print_poem()

current_year=2021
born_year=1985
def calculate_age(current_year,born_year):
      my_age=current_year-born_year
      return my_age
print(calculate_age(current_year,born_year))

def calculate_circle_k(pi, sugar):
      return 2*pi*sugar
def calculate_circle_t(pi, sugar):
      return pi*(sugar**2)
def print_circle(pi, sugar):
      print("A kör kerülete: "+str(calculate_circle_k(pi, sugar)))
      print("A kör területe: "+str(calculate_circle_t(pi, sugar)))
print_circle(3.14, 5)

dwarf_counter=1
total_dwarf=7
working_dwarf=4
while dwarf_counter<=total_dwarf:
      if dwarf_counter<=working_dwarf:
            print('Az '+str(dwarf_counter)+'. számú törpe a bányában van.')
            dwarf_counter+=1
      else:
            print('Az '+str(dwarf_counter)+'. számú törpe otthon alszik még.')
            dwarf_counter+=1

name=input('Szia, hogy hívnak? ')
print('Szia '+name)

age=int(input('Hány éves vagy?'))
if age<18:
      print("Sajnáljuk de a cikk csakk 18 éven felülieknek érhető el.")
elif age==18:
      print("Pont "+str(age)+"? Gratulálunk, üdv a felnöttek között! Jó szórakozást a cikkhez!")
else:
      print("Köszönjük! Elolvashatod a cikket.")

counter=1
while counter<=20:
      if counter==10:
            print(str(counter)+" a legszebb páros szám")
            counter+=1
      elif counter%2==0:
            print(str(counter)+" egy páros szám")
            counter+=1
      else:
            print(str(counter)+" egy páratlan szám")
            counter+=1

wind_counter=1
power_1=2000
power_2=1000
sum_power=0
while wind_counter<=25:
      if wind_counter<=10:
            sum_power+=power_1
            print('A(z) '+str(wind_counter)+'. számú szélturbina teljes fordulaton működik, '+str(power_1)+' MWh-t termelve. A farmon termelt összenergia jelenleg '+str(sum_power)+' MWh.')
      elif wind_counter<=20:
            sum_power+=power_2
            print('A(z) '+str(wind_counter)+'. számú szélturbina fél fordulaton működik, '+str(power_2)+' MWh-t termelve. A farmon termelt összenergia jelenleg '+str(sum_power)+' MWh.')
      else:
            print('A(z) '+str(wind_counter)+'. számú szélturbina fél fordulaton működik, 0 MWh-t termelve. A farmon termelt összenergia jelenleg '+str(sum_power)+' MWh.')
      wind_counter+=1