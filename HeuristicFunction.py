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
    if node.playerScore > node.computerScore:
        node.setHeuristicValue(-1)
    elif node.playerScore < node.computerScore:
        node.setHeuristicValue(1)
    else:
        node.setHeuristicValue(0)