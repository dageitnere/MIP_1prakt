def minMax(node):

    if not node.getChildren():  # Ja tā ir strupceļa virsotne, aprēķina tās vērtību
        calcHeuristicVal(node)
    else:
        for child in node.getChildren():
            minMax(child)
    
    if not node.getChildren():
        return  # Nav iespējams sākt no strupceļa virsotnēm

    child_values = [child.heuristicValue for child in node.getChildren() if child.heuristicValue is not None]

    if node.turn == 0:  # Spēlētāja kārta - minimizācija
        node.setHeuristicValue(min(child_values))
    else:  # Datora kārta - maksimizācija
        node.setHeuristicValue(max(child_values))


def alphaBeta(node, alpha=float('-inf'), beta=float('inf')):

    if not node.getChildren():  # Ja tā ir strupceļa virsotne, aprēķina tās vērtību
        calcHeuristicVal(node)
    else:
        if node.turn == 0:  # Spēlētāja kārta (minimizācija)
            value = float('inf')
            for child in node.getChildren():
                alphaBeta(child, alpha, beta)
                if child.heuristicValue is not None:
                    value = min(value, child.heuristicValue)
                    beta = min(beta, value)
                if alpha >= beta:  # Zaru nogriešana
                    return
            node.setHeuristicValue(value if value != float('inf') else None)
        else:  # Datora kārta (maksimizācija)
            value = float('-inf')
            for child in node.getChildren():
                alphaBeta(child, alpha, beta)
                if child.heuristicValue is not None:
                    value = max(value, child.heuristicValue)
                    alpha = max(alpha, value)
                if alpha >= beta:  # Zaru nogriešana
                    return
            node.setHeuristicValue(value if value != float('-inf') else None)


def calcHeuristicVal(node):
    # f1: pamat-punktu-vertējums
    if node.playerScore > node.computerScore:
        f1 = 2  # SLIKTI, vada speletājs
    elif node.playerScore < node.computerScore:
        f1 = 0  # LABI, vada dators
    else:
        f1 = 1  #neviens nevada

    # f2: novertejums vai skaitlis ir pāra, dators var dabūt punktu
    if node.currentNumber % 2 == 0:
        f2 = 0
    else:
        f2 = 1

    # f3: vertejums vai ir iespejams nakamais solis un kurš izpildija pedejo soli
    # ja nedalas uz 3/2 - game over
    if node.currentNumber % 2 != 0 and node.currentNumber % 3 != 0:
        if node.turn == 0:  #ja speletaja solis, pirms bija AI
            f3 = 0 # tas ir labi datoram
        else:  # ja AI solis un pirms bija speletajs
            f3 = 2  # slikti
    else:
        f3 = 1  # neviens nepabeiga speli, neitrali
    
    # heuristika kopējā vērtība (minimizēts)
    heuristic_value = f1 + f2 + f3
    node.setHeuristicValue(heuristic_value)
