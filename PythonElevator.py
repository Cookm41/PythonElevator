# Takes a list of floors separated by spaces & calculates total travel time based on all floors stopped on.
# Prints list of floors & travel time total to console

# Assuming first floor is the lowest possible
LOWER_FLOOR_LIMIT = 1

# Assuming building will have 150 floors or less
UPPER_FLOOR_LIMIT = 150

# Travel time value provided in prompt
TRAVEL_TIME_PER_FLOOR = 10
    

# Main starting method, takes in string input & validates all inputs are integers before continuing
def elevatorMain() :
    print("Welcome To The Elevator")
    try: 
        floorsVisited = list(map(int, input("Enter the floors visited, separated by space: ").split()))
    except:
        print("An invalid input was made, please use only integer values separated by a space")
    else: 
        validateInputList(floorsVisited)

# Validates that the given floor list stays within the defined boundaries before calculating the travel time 
# param floorList -> integer list
def validateInputList(floorList):

    greaterThanUpperLimitFlag = any(x > UPPER_FLOOR_LIMIT for x in floorList)

    lessThanLowerLimitFlag = any(x < LOWER_FLOOR_LIMIT for x in floorList)

    if greaterThanUpperLimitFlag:
        print("A value entered was greater than the upper floor limit of " + str(UPPER_FLOOR_LIMIT) + ", please try again")

    if lessThanLowerLimitFlag:
        print("A value entered was less than than the lower floor limit of " + str(LOWER_FLOOR_LIMIT) + ", please try again")

    travelTime = addTravelTime(floorList)

    outputToConsole(floorList, travelTime)


# Prints nicely to console
# param floorList -> integer list
# param travelTime -> integer value
def outputToConsole(floorList, travelTime):
    print("Floors Visited: ", floorList)
    print("Travel Time: ", travelTime)

# Takes in a list of floors, finding the absolute value of the difference between two values, 
# multiplies by the travel time constant, and adds to total travel time
# param floors -> integer list 
def addTravelTime(floors):
    travelTime = 0
    currentFloor = floors[0]
    for floor in floors:
        timeBetweenFloors = abs(currentFloor - floor) * TRAVEL_TIME_PER_FLOOR
        currentFloor= floor
        travelTime += timeBetweenFloors

    return travelTime


elevatorMain()