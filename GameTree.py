# Izveido koka datu strukturu
class GameTreeNode:
    def __init__(self, currentNumber: int, playerScore: int, computerScore: int, bankScore: int, turn: int):
        self.currentNumber = currentNumber
        self.playerScore = playerScore
        self.computerScore = computerScore
        self.bankScore = bankScore
        self.turn = turn
        self.children = []

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

# Izveido spēles koku

def generateGameTree(startingNumber: int, maxDepth: int):
    
    # Skaita rezultātu atkarībā no dalījuma
    def calculateScore(number, currentTurn, currentPlayerScore, currentComputerScore, currentBankScore):
        newPlayerScore = currentPlayerScore
        newComputerScore = currentComputerScore
        newBankScore = currentBankScore

        # Atkarībā no tā kura gājiens tiek aprēķināts rezultāts
        if number % 2 == 0:
            if currentTurn == 0: 
                newPlayerScore += 1
            else:  
                newComputerScore += 1
        else:
            if currentTurn == 0:
                newPlayerScore -= 1
            else: 
                newComputerScore -= 1

        if number % 10 == 0 or number % 5 == 0:
            newBankScore += 1

        return newPlayerScore, newComputerScore, newBankScore
    

    # Rekursīvi izveido spēles koku
    def buildTree(currentNumber, depth, turn, playerScore, computerScore, bankScore, gameTree):

        # Izveido konkrēto virsotni
        currentNode = GameTreeNode(
            currentNumber = currentNumber, 
            playerScore = playerScore, 
            computerScore = computerScore, 
            bankScore = bankScore, 
            turn = turn
        )

        # Pievieno virsotni spēles kokam
        gameTree.addNode(currentNode)

        # Pārbauda vai izpildās spēles gala nosacījums
        if currentNumber in [2, 3]:
            # Atkarībā no tā kura kārta ir, tiek piešķirta bankas rezultāts
            if currentNumber == 2:
                if turn == 0:  # Par nulli uzskata spēlētāja kārtu
                    currentNode.playerScore += bankScore
                else:  # Par viens uzskata datora kārtu
                    currentNode.computerScore += bankScore
            return currentNode

        # Pārbauda vai sasniegts dziļums
        if depth == 0:
            return currentNode

        # Apskata dalījumu ar 2
        if currentNumber % 2 == 0:
            dividedNumber2 = currentNumber // 2

            if dividedNumber2 > 1:
                # Aprēķina jaunos rezultātus
                newPlayerScore, newComputerScore, newBankScore = calculateScore(
                    dividedNumber2, 
                    1 - turn,  # Samaina kārtu 
                    playerScore, 
                    computerScore, 
                    bankScore
                )

                
            # Izmantojot rekursiju turpina būvēt koku
            childNode2 = buildTree(
                dividedNumber2, 
                depth - 1, 
                1 - turn,  # Samaina kārtu
                newPlayerScore, 
                newComputerScore, 
                newBankScore,
                gameTree
            )

            # Sarakstam pievieno ceļu starp virsotnēm
            gameTree.addPath(currentNode, childNode2)
            currentNode.children.append(childNode2)

        #  Apskata dalījumu ar 3
        if currentNumber % 3 == 0:
            dividedNumber3 = currentNumber // 3

            if dividedNumber3 > 1:
                # Aprēķina jaunos rezultātus
                newPlayerScore, newComputerScore, newBankScore = calculateScore(
                    dividedNumber3, 
                    1 - turn,  # Samaina kārtu
                    playerScore, 
                    computerScore, 
                    bankScore
                )

            # Izmantojot rekursiju turpina būvēt koku
            childNode3 = buildTree(
                dividedNumber3, 
                depth - 1, 
                1 - turn,  # Samaina kārtu
                newPlayerScore, 
                newComputerScore, 
                newBankScore,
                gameTree
            )

            # Sarakstam pievieno ceļu starp virsotnēm
            gameTree.addPath(currentNode, childNode3)
            currentNode.children.append(childNode3)

        return currentNode

    # Izveido spēles koku
    gameTree = GameTree()

    # Izveido spēles koka sakni
    decidedTurn = 0 # Spēlētāja izvēle kurš sāks spēli
    root = buildTree(startingNumber, maxDepth, 1 - decidedTurn, 0, 0, 0, gameTree)
    
    return gameTree, root

# Izvada koku
def printGameTree(node, depth=0):

    if not node:
        return
    
    indent = "  " * depth
    print(f"{indent}Number: {node.currentNumber}")
    print(f"{indent}Player Score: {node.playerScore}")
    print(f"{indent}Computer Score: {node.computerScore}")
    print(f"{indent}Bank Score: {node.bankScore}")
    print(f"{indent}Turn: {'Player' if node.turn == 0 else 'Computer'}")
    print(f"{indent}Children: {len(node.children)}")
    print("")

    for child in node.children:
        printGameTree(child, depth + 1)

# Pārbaude kokam
if __name__ == "__main__":
    startNumber = 5832  # Sākuma skaitlis
    gameTree, root = generateGameTree(startNumber, 10)
    
    print("Game Tree Nodes:")
    for node in gameTree.childrenList:
        print(f"Node: {node.currentNumber}")
    
    print("\nGame Tree Structure:")
    printGameTree(root)

    print("\nPaths:")
    for startNode, endNodes in gameTree.pathList.items():
        print(f"{startNode.currentNumber} -> {[node.currentNumber for node in endNodes]}")
