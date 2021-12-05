top_10_population = {
    'Hungary': {
        'Budapest': 1750216,
        'Debrecen': 201112,
        'Szeged': 160258,
        'Miskolc': 167754,
        'Pécs': 141843,
        'Győr': 133946,
        'Nyíregyháza': 116814,
        'Kecskemét': 110373,
        'Székesfehérvár': 96529,
        'Szombathely': 78591
    },
    'Germany': {
        'Berlin': 3520031,
        'Hamburg': 1787408,
        'Munich': 1450381,
        'Cologne': 1060582,
        'Frankfurt am Main': 732688,
        'Stuttgart': 623738,
        'Düsseldorf': 612178,
        'Dortmund': 586181,
        'Essen': 582624,
        'Leipzig': 560472
    },
    'France': {
        'Paris': 2187526,
        'Marseille': 863310,
        'Lyon': 516092,
        'Toulouse': 479553,
        'Nice': 340017,
        'Nantes': 309346,
        'Montpellier': 285121,
        'Strasbourg': 280966,
        'Bordeaux': 254436,
        'Lille': 232787
    }
}


def is_city_in_top_10(dict, country, city):
    if city in dict[country]:
        print('The population of Cologne is: ' + str(dict[country][city]))

# is_city_in_top_10(top_10_population, 'Germany', 'Cologne')


def print_citis_population(dict):
    for country in dict:
        for cities in dict[country]:
            print(cities+" : "+str(dict[country][cities])+",")
    print(list(dict['Germany'].keys()))
    print(list(dict['Germany'].keys())[1])
    print(dict['Germany'].items())


# print_citis_population(top_10_population)

def cities(dict):
    for country in dict:
        for city, population in dict[country].items():
            print("A "+city+" városnak "+str(population)+" lakosa van")


# cities(top_10_population)


def sum_cities(dict):
    new_dict = {}
    for country in dict:
        number=int()
        for city, population in dict[country].items():
            number+=population
        new_dict[country] = number
    print(new_dict)

sum_cities(top_10_population)