import random

startingNumberList = []
while len(startingNumberList) < 5:
    randomNum = random.randint(10000, 20000)
    if randomNum % 3 == 0 & randomNum % 2 == 0:
        startingNumberList.append(randomNum)

print(startingNumberList)