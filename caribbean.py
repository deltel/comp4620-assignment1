# data structure to store list of cities
cities = dict()

# data structure for a city
def makeCity(name, coordinate):
    return (name, coordinate)

def getCityName(city):
    return city[0]

def getCityCoordinates(city):
    return city[1]

# data structure for a coordinate
def makeCoordinate(x, y):
    return (x, y)

def xCoord(coordinate):
    return coordinate[0]

def yCoord(coordinate):
    return coordinate[1]

cities['kingston'] = makeCity('Kingston', makeCoordinate(4, 4))
cities['havana'] = makeCity('Havana', makeCoordinate(2, 2))
cities['miami'] = makeCity('Miami', makeCoordinate(1, 3))
cities['caracas'] = makeCity('Caracas', makeCoordinate(8, 8))
cities['valencia'] = makeCity('Valencia', makeCoordinate(8, 7))
cities['port-of-spain'] = makeCity('Port of Spain', makeCoordinate(8, 10))
cities['san-jose'] = makeCity('San Jose', makeCoordinate(8, 1))
cities['colon'] = makeCity('Colon', makeCoordinate(8, 3))
cities['santiago'] = makeCity('Santiago', makeCoordinate(4, 7))
cities['port-au-prince'] = makeCity('Port-au-Prince', makeCoordinate(4, 6))
