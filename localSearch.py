"""

@author: ReileyMeeks
"""


import random
import math


class Board:

    def __init__(self, numRowsCols):
        self.cells = [[0] * numRowsCols for i in range(numRowsCols)]
        self.numRows = numRowsCols
        self.numCols = numRowsCols
        self.h = -1

    def printBoard(self):
        for row in self.cells:
            print(row)

    def rand(self):
        self.cells = [[0] * self.numRows for i in range(self.numRows)]
        for row in self.cells:
            i = random.randint(0, self.numCols - 1)
            row[i] = 1

    def swapLocations(self, a, b):
        temp = self.cells[a[0]][a[1]]
        self.cells[a[0]][a[1]] = self.cells[b[0]][b[1]]
        self.cells[b[0]][b[1]] = temp


def numAttackingQueens(board):
    location = []
    for r in range(len(board.cells)):
        for c in range(len(board.cells[r])):
            if board.cells[r][c] == 1:
                location.append([r, c])
    result = 0

    for q in location:
        others = [x for x in location if x != q]
        count = 0

        for o in others:
            diff = [o[0] - q[0], o[1] - q[1]]
            if o[0] == q[0] or o[1] == q[1] or abs(diff[0]) == abs(diff[1]):
                count = count + 1

        result = result + count

    return result


def getSuccessorStates(board):
    result = []  # store result

    for i_row, row in enumerate(board.cells):
        i_queen = [i for i, x in enumerate(row) if x == 1][0]

        for i_col in range(board.numCols):
            if row[i_col] != 1:
                # copy board
                bTemp = Board(board.numRows)
                bTemp.cells[:] = [r[:] for r in board.cells]

                # swap queen
                bTemp.swapLocations([i_row, i_col], [i_row, i_queen])
                result.append(bTemp)

    return result


def schedule(T, decay_rate):
    T = T * decay_rate
    return T


def simulatedAnnealing(initBoard, decayRate, T_Threshold):
    T = 100
    current = initBoard  # init board state

    currentHeuristic = numAttackingQueens(current)

    while T_Threshold < T:
        currentHeuristic = numAttackingQueens(current)
        T = schedule(T, decayRate)
        if currentHeuristic == 0:
            print(current)
            return current

        nextList = getSuccessorStates(current)  # neighbors in nextList
        next = nextList[random.randrange(0, len(nextList)) - 1]
        next.h = numAttackingQueens(next)
        delta_e = currentHeuristic - next.h
        if delta_e > 0:
            current = next

        else:
            prob = math.exp(delta_e / T)
            if random.random() < prob:
                current = next

    return current


def main():
    initBoard = Board(8)
    initBoard.rand()
    decayRate = 0.9
    T_Threshold = .000001

    print("initial board:")
    initBoard.printBoard()
    print("h-value = %d\n" % (numAttackingQueens(initBoard)))

    forPrint = simulatedAnnealing(initBoard, decayRate, T_Threshold)
    forPrint.printBoard()
    print("h-value = ", numAttackingQueens(forPrint))


if __name__ == '__main__':
    main()
