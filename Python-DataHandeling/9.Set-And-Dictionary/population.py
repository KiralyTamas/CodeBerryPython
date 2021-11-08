hungarian_cities = {'Budapest': 1750216, 'Debrecen': 201112, 'Szeged': 160258, 'Miskolc': 167754, 'Pécs': 141843,
                    'Győr': 133946, 'Nyíregyháza': 116814, 'Kecskemét': 110373, 'Székesfehérvár': 96529, 'Szombathely': 78591}
def print_city_population(city,varos):
  print(str(varos)+" népessége a legutóbbi népszámlálás szerint: "+str(city['Pécs']))
  

print_city_population(hungarian_cities,'Pécs')