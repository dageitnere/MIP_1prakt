class GameState:
    def __init__(self, turnToPlay, currentValue, playerPoints, computerPoints, bankValue, algorithmUsed = None):
        self.turnToPlay = turnToPlay 
        self.currentValue = currentValue
        self.playerPoints = playerPoints
        self.computerPoints = computerPoints
        self.bankValue = bankValue
        self.algorithmUsed = algorithmUsed