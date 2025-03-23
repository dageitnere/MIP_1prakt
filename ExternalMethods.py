import random

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

def GetIndexFromList(value : str, valueList : list):
    return 1 + valueList.index(value)