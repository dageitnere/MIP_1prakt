from tkinter import *
from CustomModels.GameState import GameState

def CreateGameFinishUI(window, values : GameState):

    finalValues = CreateFinalGameState(values)
    winnerAnnoucment_label = Label(window, text = f"{CreateAnnouncmentMessage(finalValues)}")
    winnerAnnoucment_label.grid(row = 1, column = 1)

    mainloop()

def CreateFinalGameState(values : GameState):
    if values.currentValue == 2:
        if values.turnToPlay == "Cilvēks":
            values.computerPoints += values.bankValue
        elif values.turnToPlay == "Dators":
            values.playerPoints += values.bankValue
    
    return values


def CreateAnnouncmentMessage(values : GameState):
    message = ""
    if values.playerPoints > values.computerPoints:
        message = "Cilvēks uzvar!"
    elif values.playerPoints < values.computerPoints:
        message = "Dators uzvar!"
    else:
        message = "Neizšķirts!"
    return message