from tkinter import *
from tkinter import ttk
import ExternalMethods
import CustomModels.RunSettings as RunSettings
import CustomModels.GameState as GameState
import GameTree
from UserInterface.MainGameUI import CreateMainGameUI

firstMovePreferenceChoices = ["Cilvēks", "Dators"]
algorithmPreferenceChoices = ["MinMax", "AlfaBeta"]

def CreateUI(window):
    
    if window.winfo_children():
        for widget in window.winfo_children():
            widget.destroy()

    # Izveido tekstu un ievades punktu priekš izvēles, kurš uzsāks spēli 
    firstMovePreference_label = Label(window, text = "Kurš uzsāks spēli?")
    firstMovePreference_label.grid(row = 1, column = 1)
    firstMovePreference_entry = ttk.Combobox(
        state = "readonly",
        values = firstMovePreferenceChoices
    )
    firstMovePreference_entry.grid(row = 1, column = 2)

    # Izveido tekstu un ievades punktu priekš izvēles, kuru algoritmu izmantos dators
    algorithmPreference_label = Label(window, text = "Kuru algoritmu izmantos dators?")
    algorithmPreference_label.grid(row = 2, column = 1)
    algorithmPreference_entry = ttk.Combobox(
        state = "readonly",
        values = algorithmPreferenceChoices
    )
    algorithmPreference_entry.grid(row = 2, column = 2)

    # Izveido tekstu un ievades punktu priekš sākuma vērtības izvēles
    startingValue_label = Label(window, text = "Ar kuru vērtību sāksiet spēli?")
    startingValue_label.grid(row = 3, column = 1)
    startingValue_entry = ttk.Combobox(
        state = "readonly",
        values = ExternalMethods.GenerateStartingNumberList()
    )
    startingValue_entry.grid(row = 3, column = 2)

    # Nolasa ievadītos datus, tos saglabā
    def StartGame():
        runSettings = RunSettings.RunSettings(
            firstMovePreference = ExternalMethods.GetIndexFromList(firstMovePreference_entry.get(), firstMovePreferenceChoices),
            algorithmPreference = ExternalMethods.GetIndexFromList(algorithmPreference_entry.get(), algorithmPreferenceChoices),
            startingValue = int(startingValue_entry.get())
        )

        GameTree.generateGameTree(runSettings, 10)
        
        gameState = GameState.GameState(
            turnToPlay = firstMovePreference_entry.get(),
            currentValue = int(startingValue_entry.get()),
            playerPoints = 0,
            computerPoints = 0,
            bankValue = 0,
            algorithmUsed = runSettings.algorithmPreference
        )
        CreateMainGameUI(window, gameState)
        
    # Izvēles apstiprināšanas un spēles uzsākšanas poga
    ok_button = Button(window, text = "Apstiprināt", command = StartGame)
    ok_button.grid(row = 4, column = 2, sticky = W)
    
    mainloop()