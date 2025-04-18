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
    # f1: pamatpunktu vertējums
    if node.playerScore > node.computerScore:
        f1 = 0  # Slikti, jo vadībā speletājs
    elif node.playerScore < node.computerScore:
        f1 = 2  # Labi, vadībā dators
    else:
        f1 = 1  # Neitrāli, jo neviens nav vadībā

    # f2: vērtejums vai ir iespējams nākamais gājiens un kurš izpildija pedejo gājienu
    if node.currentNumber % 2 != 0 and node.currentNumber % 3 != 0:
        if node.turn == 0:  # Ja speletaja gājiens, iepriekšējais bija datora
            f2 = 2 # Labi datoram, jo nozīmē ka banka tiks izmaksāta datoram
        else:  # Ja datora gājiens, iepriekšējais bija spēlētāja
            f2 = 0  # Slikti datoram, jo nozīmē, ka banka tiks izmaksāta cilvēkam
    else: 
        f2 = 1 # Neitrāli, virsotne dalās ar 2 vai 3
    
    # Heiristiskā kopējā vērtība (minimizēta)
    heuristic_value = 0.8*f1 + 0.2*f2
    node.setHeuristicValue(heuristic_value)
