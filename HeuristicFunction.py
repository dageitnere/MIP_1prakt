
def evalNode(node, decidedTurn):
    if not node.getChildren():  # Ja tā ir strupceļa virsotne, aprēķina tās vērtību
        calcHeuristicVal(node, decidedTurn)
    else:
        for child in node.getChildren():
            evalNode(child, decidedTurn)

    # Izsauc funkciju, lai dotos augšup tiklīdz aizpildītas strupceļa virsotnes
    fillTree(node)


# Pieņem, ka spēlētājs ir minimizētājs un dators ir maksimizētājs
def calcHeuristicVal(node, decidedTurn):
    if node.playerScore < node.computerScore:
        if decidedTurn == 0:
            node.setHeuristicValue(1)
        else:
            node.setHeuristicValue(-1)
    elif node.playerScore > node.computerScore:
        if decidedTurn == 0:
            node.setHeuristicValue(-1)
        else:
            node.setHeuristicValue(1)
    else:
        node.setHeuristicValue(0)


# Dodas augšup pa koku, aizpildot visu lapu hēristisko novērtējumu
def fillTree(node):
    if not node.getChildren():
        return  # Nav iespējams sākt no strupceļa virsotnēm

    # Iegūst bērnu hēristiskās vērtības
    child_values = [child.heuristicValue for child in node.getChildren()]

    # Pieņem, ka spēlētājs ir minimizētājs un dators ir maksimizētājs
    # Atkarībā no tā kura kārta ir tiek vai nu ņemta minimālā vai maksimālā vērtība
    if node.turn == 0:  # Spēlētāja kārta - minimizācija
        node.setHeuristicValue(min(child_values))
    else:  # Datora kārta - maksimizācija
        node.setHeuristicValue(max(child_values))
