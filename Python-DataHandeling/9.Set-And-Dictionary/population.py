hungarian_cities = {'Budapest': 1750216, 'Debrecen': 201112, 'Szeged': 160258, 'Miskolc': 167754, 'Pécs': 141843,
                    'Győr': 133946, 'Nyíregyháza': 116814, 'Kecskemét': 110373, 'Székesfehérvár': 96529, 'Szombathely': 78591}

def print_city_population(city, varos):
    if str(city.get(varos,-1)) != varos:
        print("Erről a városról nincs adat: "+varos)
    else:
        print(str(varos)+" népessége a legutóbbi népszámlálás szerint: " +str(city.get(varos)))


#print_city_population(hungarian_cities, "Cegléd")

def update_population(city, varos, peoples):
    for i in varos:
        if i in city:
            city[i]=city[i]+peoples
    print(hungarian_cities)

#update_population(hungarian_cities,['Budapest','Miskolc','Győr'],1000)

def add_cities(city,varos):
    for i in varos:
        city[i[0]]=i[1]
    print(city)

#add_cities(hungarian_cities,[('Szolnok',70554),('Érd',69431)])

def update_population(city,population):
    city.update(population)
    print(city)

#update_population(hungarian_cities,{'Budapest':1749812,'Érd':69431})

def delete_cities(city,varos):
    for i in varos:
        del city[i]
    print(city)

#delete_cities(hungarian_cities,['Debrecen','Kecskemét'])

def get_over_populated_cities(city):
    new_cities={}
    for i in city:
        if city[i]>200000:
            varos=i
            popul=city[i]
            new_cities[varos]=popul
    for i in new_cities:
        del city[i]
    print(city)
    print(new_cities)

get_over_populated_cities(hungarian_cities)