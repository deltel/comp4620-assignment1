from utils import makeCoordinate

# data structure for a city
def makeCity(name, coordinate):
    return (name, coordinate)

def getCityName(city):
    return city[0]

def getCityCoordinates(city):
    return city[1]

def printCity(city):
    print('City: {}\nLocation: {}\n'.format(getCityName(city), getCityCoordinates(city)))

# data structure to store list of cities
cities = dict()

cities['kingston'] = makeCity('Kingston', makeCoordinate(4, 4))
cities['havana'] = makeCity('Havana', makeCoordinate(2, 2))
cities['miami'] = makeCity('Miami', makeCoordinate(3, 1))
cities['caracas'] = makeCity('Caracas', makeCoordinate(8, 8))
cities['valencia'] = makeCity('Valencia', makeCoordinate(7, 8))
cities['port-of-spain'] = makeCity('Port of Spain', makeCoordinate(10, 8))
cities['san-jose'] = makeCity('San Jose', makeCoordinate(1, 8))
cities['colon'] = makeCity('Colon', makeCoordinate(3, 8))
cities['santiago'] = makeCity('Santiago', makeCoordinate(7, 4))
cities['port-au-prince'] = makeCity('Port-au-Prince', makeCoordinate(6, 4))
