from tkinter import *
from CustomModels.GameState import GameState
from GameTree import calculateScore

def CreateMainGameUI(window, values : GameState):
    
    firstPlayerPoints_label = Label(window, text = "Spēlētāja punkti")
    firstPlayerPoints_label.grid(row = 1, column = 1)

    currentMove_label = Label(window, text = f"{values.turnToPlay} veic gājienu")
    currentMove_label.grid(row = 1, column = 2)

    computerPoints_label = Label(window, text = "Datora punkti")
    computerPoints_label.grid(row = 1, column = 3)

    firstPlayerPointCount_label = Label(window, text = values.playerPoints)   
    firstPlayerPointCount_label.grid(row = 2, column = 1)

    currentNumber_label = Label(window, text = f"{values.currentValue}")
    currentNumber_label.grid(row = 2, column = 2)

    computerPointCount_label = Label(window, text = values.computerPoints)
    computerPointCount_label.grid(row = 2, column = 3)

    def ExecuteMove(move : int):
        newPlayerScore, newComputerScore, newBankScore = calculateScore(GameState(
            values.turnToPlay,
            values.currentValue/move,
            values.playerPoints,
            values.computerPoints,
            values.bankValue
        ))
        from UserInterface.CreateUI import firstMovePreferenceChoices
        from ExternalMethods import GetIndexFromList
        '''
        CreateMainGameUI(window, GameState(
            firstMovePreferenceChoices[1 - GetIndexFromList(values.turnToPlay, firstMovePreferenceChoices)],
            values.currentValue/move,
            newPlayerScore,
            newComputerScore,
            newBankScore
        ))
        '''
    divideByTwo_button = Button(window, text = "2", command = ExecuteMove(2))
    divideByTwo_button.grid(row = 3, column = 2)

    divideByThree_button = Button(window, text = "3", command = ExecuteMove(3))
    divideByThree_button.grid(row = 4, column = 2)

    bankValue_label = Label(window, text = f"Banka: {values.bankValue}")
    bankValue_label.grid(row = 5, column = 2)

    mainloop()