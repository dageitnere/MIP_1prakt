from tkinter import *
from tkinter import ttk
from CustomModels.GameState import GameState
from GameTree import calculateScore, generateGameTree
from UserInterface.GameFinishUI import CreateGameFinishUI
from ExternalMethods import GetIndexFromList
from HeuristicFunction import minMax, alphaBeta
from GameTree import GameTreeNode, GameTree
from CustomModels.RunSettings import RunSettings

# Izvēles secība: kurš veic gājienu - spēlētājs vai dators
firstMovePreferenceChoices = ["Cilvēks", "Dators"]

# funkcija, kas atgriež labāko nākamo skaitli, ko izvēlas dators, izmantojot AlphaBeta algoritmu
# atgriež labāko nākamo skaitli, ko izvēlas dators
def get_best_move(values: GameState):
    # nosaka, kuru algoritmu izmantot, balstoties uz speles stavokli:
    # 1 - AlphaBeta, 0 - Minimax
    if values.algorithmUsed == 1:
        algorithm = "AlphaBeta"
    else:
        algorithm = "Minimax"

    inputValues = RunSettings(
    firstMovePreference=1,                 # 1 = Dators
    algorithmPreference=algorithm,        # izvēlētais algoritms
    startingValue=int(values.currentValue))  # pašreizējā vērtība
    
    _, root = generateGameTree(inputValues, 4)
    if values.algorithmUsed == 1:
        alphaBeta(root)
    elif values.algorithmUsed == 0:
        minMax(root)

    # izvēlas bērnu ar maksimālo heuristikas vērtību (visizdevīgāko datoram)
    bestChild = None
    bestValue = float('-inf')  # sākotnēji mazākā iespējamā vērtība

    for child in root.getChildren():
        # aizsardzība, ja heuristicValue nav aprēķināta
        if child.heuristicValue is None:
            continue
        if child.heuristicValue > bestValue:
            bestValue = child.heuristicValue
            bestChild = child

    # ja visi bērni bija None, aizsardzība no kļūdas
    if bestChild is None:
        raise ValueError("Neviens bērns nav ar derīgu heuristikas vērtību")

    return bestChild.currentNumber


# Uzģenerēt spēles koku 


def CreateMainGameUI(window, values: GameState, wasValidMove=True, aiMoveDesc=""):
    for widget in window.winfo_children():
        widget.destroy()

    # ja spēli vairs nevar turpināt  piešķirt banku pēdējam speletajam un pabeigt spēli
    if values.currentValue % 2 != 0 and values.currentValue % 3 != 0:
        message = ""
        if values.bankValue > 0:
            if values.turnToPlay == "Cilvēks":
                values.playerPoints += values.bankValue
                message = f"Banka ({values.bankValue}) pievienota spēlētājam"
            else:
                values.computerPoints += values.bankValue
                message = f"Banka ({values.bankValue}) pievienota datoram"
            values.bankValue = 0
        else:
            message = "Gājiens nav iespējams – spēle beigusies"

        # Parādīt ziņojumu pirms spēles beigām
        info_label = Label(window, text=message)
        info_label.grid(row=0, column=1, columnspan=3)

        window.after(1500, lambda: CreateGameFinishUI(window, values))
        return

    # ekrāna komponentes
    firstPlayerPoints_label = Label(window, text="Spēlētāja punkti")
    firstPlayerPoints_label.grid(row=1, column=1)

    currentMove_label = Label(window, text=f"{values.turnToPlay} veic gājienu")
    currentMove_label.grid(row=1, column=2)

    computerPoints_label = Label(window, text="Datora punkti")
    computerPoints_label.grid(row=1, column=3)

    firstPlayerPointCount_label = Label(window, text=values.playerPoints)
    firstPlayerPointCount_label.grid(row=2, column=1)

    currentNumber_label = Label(window, text=f"{values.currentValue}")
    currentNumber_label.grid(row=2, column=2)

    computerPointCount_label = Label(window, text=values.computerPoints)
    computerPointCount_label.grid(row=2, column=3)

    # funkcija, ko izsauc, kad spēlētājs veic gājienu (dalīšana ar 2 vai 3)
    def ExecuteMove(move: int):
        if values.currentValue % move == 0:
            new_value = values.currentValue // move
            newPlayerScore, newComputerScore, newBankScore = calculateScore(GameState(
                values.turnToPlay,
                new_value,
                values.playerPoints,
                values.computerPoints,
                values.bankValue
            ))

            next_turn = firstMovePreferenceChoices[1 - GetIndexFromList(values.turnToPlay, firstMovePreferenceChoices)]

            next_state = GameState(
                next_turn,
                new_value,
                newPlayerScore,
                newComputerScore,
                newBankScore,
                algorithmUsed = values.algorithmUsed
            )
            CreateMainGameUI(window, next_state)
        else:
            CreateMainGameUI(window, values, False)

    # funkcija, lai veikt automātisko datora soli
    def ExecuteAIMove(values: GameState):
        best_number = get_best_move(values)
        move = int(values.currentValue // best_number)

        newPlayerScore, newComputerScore, newBankScore = calculateScore(GameState(
            "Dators",
            best_number,
            values.playerPoints,
            values.computerPoints,
            values.bankValue
        ))

        next_state = GameState(
            firstMovePreferenceChoices[0],
            best_number,
            newPlayerScore,
            newComputerScore,
            newBankScore,
            algorithmUsed = values.algorithmUsed
        )
        desc = f"Dators izvēlējās dalīt ar {move}"
        CreateMainGameUI(window, next_state, True, desc)

    divideByTwo_button = Button(window, text="   2   ", command=lambda: ExecuteMove(2))
    divideByTwo_button.grid(row=3, column=2)

    divideByThree_button = Button(window, text="   3   ", command=lambda: ExecuteMove(3))
    divideByThree_button.grid(row=4, column=2)

    bankValue_label = Label(window, text=f"Banka: {values.bankValue}")
    bankValue_label.grid(row=5, column=2)

     # ja spēlētājs mēģina dalīt ar nederīgu skaitli, parādīt brīdinājumu
    if wasValidMove == False:
        wasValidMove_label = Label(window, text="Skaitlis nedalās ar šo vērtību!")
        wasValidMove_label.grid(row=6, column=2)
 
    if aiMoveDesc:
        aiDesc_label = Label(window, text=aiMoveDesc)
        aiDesc_label.grid(row=7, column=2)
    # ja ir datora solis, automātiski veic gājienu pēc 500 ms(pause)
    if values.turnToPlay == "Dators":
        window.after(500, lambda: ExecuteAIMove(values))

    mainloop()
