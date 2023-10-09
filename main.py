from disturbance import makeDisturbance, sayDisturbance, moveOneTick, isActive
from caribbean import cities, printCity

if __name__ == '__main__':
    option = '0'
    activeDisturbances = []

    while option != '6':
        print('1.\tCreate a new disturbance\n2.\tRun One Tick\n3.\tShow All Disturbances\n4.\tShow All Cities\n5.\tDisplay Bulletins\n6.\tExit') 
        option = input('\n\n\nSelect an option from the menu: ')

        if option == '1':
            disturbanceName = input('Enter the name of the next disturbance:\n')
            nextDisturbance = makeDisturbance(disturbanceName)
            activeDisturbances.append(nextDisturbance)
        elif option == '2':
            activeDisturbances = [moveOneTick(disturbance) for disturbance in activeDisturbances if isActive(moveOneTick(disturbance))]
        elif option == '3':
            if len(activeDisturbances) == 0:
                print('No active disturbances\n\n\n')
            else:
                print('The active disturbances are as follows:\n')
                for disturbance in activeDisturbances:
                    print(sayDisturbance(disturbance))
                    print('----------------------------------')
                print('\n\n\n')
        elif option == '4':
            print('All cities on map')
            for city in cities.values():
                printCity(city)
