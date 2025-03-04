import random

def SafeIntegerInput():
    """
    Checks if input value is 0 or 1, returns input value if it is 0 or 1, otherwise returns None.
    """

    value = input()

    if isinstance(value, int): 
        if value is 0 or 1:
            return value
        else:
            print("Nepareiza ievade.")
            return None
    else:
        print("Nepareiza ievade.")
        return None
    
def GenerateStartingNumberList():
    """
    Generates a list containing 5 random integers, which are between 10000 and 20000.
    """
    startingNumberList = []

    while len(startingNumberList) < 5:
        randomNum = random.randint(10000, 20000)
        if randomNum % 3 == 0 & randomNum % 2 == 0:
            startingNumberList.append(randomNum)

    return startingNumberList