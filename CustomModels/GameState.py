class GameState:
    def __init__(self, turnToPlay, currentValue, playerPoints, computerPoints, bankValue):
        self.turnToPlay = turnToPlay 
        self.currentValue = currentValue
        self.playerPoints = playerPoints
        self.computerPoints = computerPoints
        self.bankValue = bankValue