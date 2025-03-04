import ExternalMethods

# mainīgo definēšana

inputValue = None
useMinMaxAlgorithm = None
startingNumber = None
startingNumberList = ExternalMethods.GenerateStartingNumberList()

# Izvēļu opciju veikšana un saglabāšana

while inputValue is None:
    print("Kurš uzsāks spēli? Ievadīt 1 (cilvēks) vai 2 (dators)")
    inputValue = ExternalMethods.SafeIntegerInput()

while useMinMaxAlgorithm is None:
    print("Kuru algoritmu izmantos dators? Ievadīt 1 (MinMax) vai 2 (AlfaBeta)")
    useMinMaxAlgorithm = ExternalMethods.SafeIntegerInput()

while startingNumber is None:
    startingNumber = input(f"Ar kuru vērtību sāksiet spēli? {startingNumberList}")
    if startingNumber not in startingNumberList: 
        print("Nepareiza ievade.")
        startingNumber = None