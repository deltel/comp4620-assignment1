# caribbean cities related stuff
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
cities['miami'] = makeCity('Miami', makeCoordinate(3, 1))
cities['caracas'] = makeCity('Caracas', makeCoordinate(8, 8))
cities['valencia'] = makeCity('Valencia', makeCoordinate(7, 8))
cities['port-of-spain'] = makeCity('Port of Spain', makeCoordinate(10, 8))
cities['san-jose'] = makeCity('San Jose', makeCoordinate(1, 8))
cities['colon'] = makeCity('Colon', makeCoordinate(3, 8))
cities['santiago'] = makeCity('Santiago', makeCoordinate(7, 4))
cities['port-au-prince'] = makeCity('Port-au-Prince', makeCoordinate(6, 4))

# disturbance related stuff
import random

def makeInitialIntensity():
    return random.randrange(10, 161)

def makeInitialSpeed():
    return random.randrange(5, 11)

def makeInitialRow():
    return random.randrange(1, 8)

def makeDisturbance(name):
    return (name, makeInitialIntensity(), makeInitialSpeed(), 13, makeInitialRow())
