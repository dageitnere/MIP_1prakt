from CustomModels.RunSettings import RunSettings
from CustomModels.GameState import GameState
from HeuristicFunction import minMax, alphaBeta, calcHeuristicVal

# Izveido koka datu strukturu
class GameTreeNode:
    def __init__(self, currentNumber: int, playerScore: int, computerScore: int, bankScore: int, turn: int):
        self.currentNumber = currentNumber

        self.playerScore = playerScore
        self.computerScore = computerScore
        self.bankScore = bankScore
        
        self.turn = turn
        self.children = []

        self.heuristicValue = None


    def getChildren(self):
        return self.children
    

    def setHeuristicValue(self, heuristicValue):
        self.heuristicValue = heuristicValue
        return



class GameTree:
    def __init__(self):
        self.childrenList = []
        self.pathList = dict()
    
    # Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def addNode(self, Node):
        self.childrenList.append(Node)
        
    # Klases Speles_koks metode, kura papildina loku kopu, saņemot kā argumentus
    # virsotnes identifikatoru, no kuras loks iziet, un virsotnes identifikatoru, kurā loks ieiet
    def addPath(self, startNode, endNode):
        self.pathList[startNode] = self.pathList.get(startNode,[]) + [endNode]



# Skaita rezultātu atkarībā no dalījuma
def calculateScore(values : GameState):
    if values.turnToPlay == "Cilvēks":
        currentTurn = 0 
    else:
        currentTurn = 1
    
    # Atkarībā no tā kura gājiens un kāds ir iegūtais skaitlis, tiek pievienoti punkti
    if values.currentValue % 2 == 0:
        if currentTurn == 0: 
            values.playerPoints += 1
        else:  
            values.computerPoints += 1
    else:
        if currentTurn == 0:
            values.playerPoints -= 1
        else: 
            values.computerPoints -= 1

    if values.currentValue % 10 == 0 or values.currentValue % 5 == 0:
        values.bankValue += 1

    return values.playerPoints, values.computerPoints, values.bankValue



# Izveido spēles koku
def generateGameTree(inputValues : RunSettings, maxDepth: int):
    from UserInterface.CreateUI import firstMovePreferenceChoices # Tiek importēts šeit, jo citādi veidotos cilpa, jo CreateUI importo GameTree
    gameTree = GameTree() # GameTree objekta izveide
    seenStates = {} # Vārdnīca, lai uzglabātu unikālos spēles stāvokļus, lai neaizņemtu tik daudz vietas

    # Rekursīvi izveido spēles koku
    def buildTree(currentNumber, depth, turn, playerScore, computerScore, bankScore, gameTree):

        # Pārbauda vai stāvoklis nav unikāls, tādejādi izmanto jau saglabāto stāvokli
        state_key = (currentNumber, playerScore, computerScore, bankScore, turn)
        if state_key in seenStates:
            return seenStates[state_key]

        node = GameTreeNode(currentNumber, playerScore, computerScore, bankScore, turn) # Izveido virsotni
        gameTree.addNode(node) # Pievieno virsotni kokam
        seenStates[state_key] = node

        if currentNumber in [2, 3]:  # Pārbauda vai nav sasniegts 2 vai 3, kad izmaksā banku
            if currentNumber == 2:
                if turn == 0:
                    node.playerScore += bankScore
                else:
                    node.computerScore += bankScore
            return node

        if depth == 0:  # Pārbauda vai nav sasniegts maksimālais dziļums, kas iepriekš norādīts
            return node

        isValidMove = False
        for divisor in (2, 3):
            if currentNumber % divisor == 0:
                isValidMove = True
                newNumber = currentNumber // divisor
                if newNumber > 1:
                    move = firstMovePreferenceChoices[turn]
                    newScores = calculateScore(GameState(move, newNumber, playerScore, computerScore, bankScore))
                    childNode = buildTree(newNumber, depth - 1, 1 - turn, *newScores, gameTree)
                    gameTree.addPath(node, childNode)
                    node.children.append(childNode)

        if not isValidMove:
            if turn == 0:
                node.playerScore += bankScore
            else:
                node.computerScore += bankScore

            node.bankScore = 0  # Reset bank score after adding
        return node

    root = buildTree(inputValues.startingValue, maxDepth, inputValues.firstMovePreference, 0, 0, 0, gameTree) # Koka saknes izveide
    return gameTree, root
