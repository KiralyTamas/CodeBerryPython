guest1 = 'Béla, Kovács, +36101234567, 1017, budapest, Fő utca 10., bela.kovacs@@pelda.hu'
guest2 = 'Arnold, szabó, 06109876543, 6500, Baja, Folyó u. 24., arnold.szabo@example.com'
guest1_first_name = 'Béla'
guest1_last_name = 'Kovács'
guest1_mobile_phone = '+36101234567'
guest1_postal_code = '1017'
guest1_city = 'budapest'
guest1_address = 'Fő utca 10.'
guest1_email = 'bela.kovacs@pelda.hu'
guest2_first_name = 'Arnold'
guest2_last_name = 'Szabó'
guest2_mobile_phone = '+36109876543'
guest2_postal_code = '6500'
guest2_city = 'Baja'
guest2_address = 'Folyó utca 24.'
guest2_email = 'arnold.szabo@example.com'

def check_phone_number(phone_number):
  if len(phone_number)==12:
    print("A telefonszám formátuma megfelel")
  else:
    print("A telefonszám formátuma nem felel meg")

def check_postal_code(postal_code):
  if len(postal_code)==4:
    print("Az irányítószám magyar")
  else:
    print("Az irányítószám nem magyar")

def check_phone_country(phone_country):
  if phone_country.startswith("+36"):
    print("A telefonszám formátuma magyar")
  else:
    print("A telefonszám formátuma nem magyar")

def check_email_country(email_country):
  if email_country.endswith(".hu"):
    print("Ez az email cím magyar")
  else:
    print("Ez az email cím külföldi")

def check_email_format(email):
  if email.count('@')==1:
    print("Az email cím formátuma megfelelő.")
  else:
    print("Az email cím formátuma nem megfelelő.")

def correct_first_name(first_name):
  print(first_name)
  print(first_name.capitalize())

def correct_last_name(last_name):
  print(last_name)
  print(last_name.capitalize())

def correct_city(city):
  print(city)
  print(city.capitalize())

def correct_address(address):
  print(address)
  print(address.replace('u.','utca'))

correct_first_name(guest1_first_name)
correct_last_name(guest1_last_name)
correct_first_name(guest2_first_name)
correct_last_name(guest2_last_name)
correct_city(guest1_city)
correct_city(guest2_city)
correct_address(guest1_address)
correct_address(guest2_address)
check_phone_number(guest1_mobile_phone)
check_phone_number(guest2_mobile_phone)
check_postal_code(guest1_postal_code)
check_postal_code(guest2_postal_code)
check_phone_country(guest1_mobile_phone)
check_phone_country(guest2_mobile_phone)
check_email_country(guest1_email)
check_email_country(guest2_email)
check_email_format(guest1_email)
check_email_format(guest2_email)
