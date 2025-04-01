import random

# Izveido sarakstu ar 5 iespējamajiem spēles uzsākšanas skaitļiem
def GenerateStartingNumberList():
    startingNumberList = []

    while len(startingNumberList) < 5:
        randomNum = random.randint(10000, 20000)
        if randomNum % 3 == 0 & randomNum % 2 == 0:
            startingNumberList.append(randomNum)

    return startingNumberList

# Izgūst indeksu no saraksta, nepieciešams GameTree datu struktūrā
def GetIndexFromList(value : str, valueList : list):
    return valueList.index(value)