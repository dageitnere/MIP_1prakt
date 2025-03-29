from tkinter import *
from CustomModels.GameState import GameState

def CreateGameFinishUI(window, values : GameState):

    finalValues, bankCleared = CreateFinalGameState(values)
    winnerAnnoucement_label = Label(window, text = f"{CreateAnnouncementMessage(finalValues)}")
    winnerAnnoucement_label.grid(row = 1, column = 2)

    playerPoints_label = Label(window, text = f"Spēlētāja punkti: {finalValues.playerPoints}")
    playerPoints_label.grid(row = 3, column = 2)

    computerPoints_label = Label(window, text = f"Datora punkti: {finalValues.computerPoints}")
    computerPoints_label.grid(row = 4, column = 2)

    finalValue_label = Label(window, text = f"Spēles beigu skaitlis: {finalValues.currentValue}")
    finalValue_label.grid(row = 5, column = 2)

    bankValue_label = Label(window, text = f"Bankas beigu vērtība: {finalValues.bankValue}")
    bankValue_label.grid(row = 6, column = 2)

    from UserInterface.CreateUI import CreateUI
    startNewGame_button = Button(window, text = "Uzsākt jaunu spēli?", command = lambda:CreateUI(window))
    startNewGame_button.grid(row = 7, column = 2)

    mainloop()

def CreateFinalGameState(values : GameState):
    bankCleared = False
    if values.currentValue == 2:
        if values.turnToPlay == "Cilvēks":
            values.computerPoints += values.bankValue
            bankCleared = True
        elif values.turnToPlay == "Dators":
            values.playerPoints += values.bankValue
            bankCleared = True
    
    return values, bankCleared


def CreateAnnouncementMessage(values : GameState):
    message = ""
    if values.playerPoints > values.computerPoints:
        message = "Cilvēks uzvar!"
    elif values.playerPoints < values.computerPoints:
        message = "Dators uzvar!"
    else:
        message = "Neizšķirts!"
    return message