from disturbance import makeDisturbance, sayDisturbance, moveOneTick, isActive, getLocation
from caribbean import cities, printCity, getCityCoordinates, getCityName

def makeCityDisturbance(city, disturbance):
    return (city, disturbance)

def getCity(cityDisturbance):
    return cityDisturbance[0]

def getDisturbance(cityDisturbance):
    return cityDisturbance[1]

def createDisturbance():
    disturbanceName = input('Enter the name of the next disturbance:\n')
    nextDisturbance = makeDisturbance(disturbanceName)
    activeDisturbances.append(nextDisturbance)

def runOneTick():
    activeDisturbances = [moveOneTick(disturbance) for disturbance in activeDisturbances if isActive(moveOneTick(disturbance))]

def showAllDisturbances():
    if len(activeDisturbances) == 0:
        print('No active disturbances\n\n\n')
    else:
        print('The active disturbances are as follows:\n')
        for disturbance in activeDisturbances:
            print(sayDisturbance(disturbance))
            print('----------------------------------')
        print('\n\n\n')

def showAllCities():
    print('All cities on map')
    for city in cities.values():
        printCity(city)

def issueBulletin():
    citiesAffected = [(city, disturbance) for city in cities.values() for disturbance in activeDisturbances if getCityCoordinates(city) == getLocation(disturbance)]
    if len(citiesAffected) == 0:
        print('No cities in trouble\n\n\n')
    else:
        print('Cities affected:\n')
        for city, disturbance in citiesAffected:
            print(getCityName(city))
            print('----------------------------------')
            print(sayDisturbance(disturbance))
            print('----------------------------------')
            print('----------------------------------')

activeDisturbances = []
citiesAffected = []
    
if __name__ == '__main__':
    option = '0'
    
    
    while option != '6':
        print('1.\tCreate a new disturbance\n2.\tRun One Tick\n3.\tShow All Disturbances\n4.\tShow All Cities\n5.\tDisplay Bulletins\n6.\tExit') 
        option = input('\n\n\nSelect an option from the menu: ')

        if option == '1':
            createDisturbance()
        elif option == '2':
            activeDisturbances = [moveOneTick(disturbance) for disturbance in activeDisturbances if isActive(moveOneTick(disturbance))]
        elif option == '3':
            showAllDisturbances()
        elif option == '4':
            showAllCities()
        elif option == '5':
            issueBulletin()
