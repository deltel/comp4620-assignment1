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
