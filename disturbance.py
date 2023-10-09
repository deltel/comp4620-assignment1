import random
from utils import makeCoordinate

# disturbance related stuff

def makeInitialIntensity():
    return random.randrange(10, 161)

def makeInitialSpeed():
    return random.randrange(5, 11)

def makeInitialRow():
    return random.randrange(1, 8)

# disturbance data structure
def makeDisturbance(name):
    return (name, makeInitialIntensity(), makeInitialSpeed(), 13, makeInitialRow())

def getName(disturbance):
    return disturbance[0]

def getIntensity(disturbance):
    return disturbance[1]

def getSpeed(disturbance):
    return disturbance[2]

def getColumn(disturbance):
    return disturbance[3]

def getRow(disturbance):
    return disturbance[4]

def getLocation(disturbance):
    return makeCoordinate(getColumn(disturbance), getRow(disturbance))

def determineCategory(disturbance):
    intensity = getIntensity(disturbance)
    if intensity < 55:
        return 'Tropical Depression'
    elif intensity < 76:
        return 'Storm'
    elif intensity < 96:
        return 'Category 1 Hurricane'
    elif intensity < 111:
        return 'Category 2 Hurricane'
    elif intensity < 130:
        return 'Category 3 Hurricane'
    elif intensity < 157:
        return 'Category 4 Hurricane'
    else:
        return 'Category 5 Hurricane'

def moveOneTick(disturbance):
    newXCoord = getColumn(disturbance) - int(getSpeed(disturbance) / 5) * 1
    return disturbance[:3] + (newXCoord, getRow(disturbance))

def isActive(disturbance):
    return getColumn(disturbance) > 0

def sayDisturbance(disturbance):
    name = getName(disturbance)
    category = determineCategory(disturbance)
    intensity = getIntensity(disturbance)
    speed = getSpeed(disturbance)
    location = getLocation(disturbance)
    return "Name: {}\nCategory: {}\nIntensity: {}\nSpeed: {}\nLocation: {}".format(name, category, intensity, speed, location)
