import time
from GameTree import generateGameTree
from CustomModels.RunSettings import RunSettings
from HeuristicFunction import minMax, alphaBeta

testNumbers = [13776, 18438, 16506, 19128, 17640, 10524, 14184, 19890, 11664, 16092]

def averageRuntime(algorithm, depth, numbers, trials=10):
    times = []
    for num in numbers:
        startNumber = RunSettings(1, "AlfaBeta", num)
        gameTree, root = generateGameTree(startNumber, depth)

        start = time.perf_counter()
        algorithm(root)
        end = time.perf_counter()

        times.append(end - start)
        del gameTree, root
    
    return sum(times) / len(times)

depths = [3, 4, 5, 10]  # Example depths to test
trials = 10

print("Izmantojot desmit dazadus ciparus, datora videjais lemuma pienemsanas laiks atkariba no dziluma:")

for depth in depths:
    minmax_avg = averageRuntime(minMax, depth, testNumbers, trials)
    alphabeta_avg = averageRuntime(alphaBeta, depth, testNumbers, trials)
    print(f"Dzilums {depth}: MinMax = {minmax_avg:.10f}s, AlphaBeta = {alphabeta_avg:.10f}s")
