"""

@author: ReileyMeeks
"""


import math
import heapq


class Node:
    def __init__(self, value, parent, g, h):
        self.value = value
        self.parent = parent
        self.g = g  # path cost
        self.h = h  # heuristic cost
        self.f = self.g + self.h  # g + h

    def __lt__(self, other):
        return self.f < other.f


def readGrid(filename):
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    return grid


def outputGrid(grid, start, goal, path):
    filenameStr = 'informPath.txt'

    f = open(filenameStr, 'w')

    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '+'

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        if r < len(grid) - 1:
            f.write("\n")

    f.close()


def heuristic(location1, location2):
    return math.dist(location1, location2)


# Determines if list is in inList
def inList(node, theList):
    for n in theList:
        if n.value == node.value:
            return True
    return False


def getNeighbors(location, grid):
    result = []

    up = location[:]
    up[0] -= 1
    if up[0] > -1 and grid[up[0]][up[1]] != 0:
        result.append(up)

    right = location[:]
    right[1] += 1
    if right[1] < len(grid[right[0]]) and grid[right[0]][right[1]] != 0:
        result.append(right)

    down = location[:]
    down[0] += 1
    if down[0] < len(grid) and grid[down[0]][down[1]] != 0:
        result.append(down)

    left = location[:]
    left[1] -= 1
    if left[1] > -1 and grid[left[0]][left[1]] != 0:
        result.append(left)

    return result


# Expands the node by putting unchecked nodes into openlist
def expandNode(node, openList, closedList, grid, goal, start):
    neighbors = getNeighbors(node.value, grid)  # neighbors is children
    for c in neighbors:  # for a location point in neighbors
        child = Node(c, node, node.g + grid[c[0]][c[1]], heuristic(c, goal))
        if not inList(child, closedList) and not inList(child, openList):
            heapq.heappush(openList, child)

    return openList


# Displays the grid
def printGrid(grid):
    for i in range(0, len(grid)):
        print(grid[i])


# Sets the path by visiting previous parent nodes
def setPath(current, path):
    while current.parent != '':
        path.insert(0, current.parent.value)
        current = current.parent


# Gets the path cost by iterating through path
def getPathCost(p, grid):
    cost = 0
    for i in range(len(p)):
        cost += grid[p[i][0]][p[i][1]]
    return cost


def aStarSearch(grid, start, goal):
    current = Node(start, '', 0, heuristic(start, goal))
    openList = []
    heapq.heapify(openList)
    heapq.heappush(openList, current)

    closedList = []
    path = []
    numExpanded = 0

    # while not openList empty:
    while len(openList) > 0:
        # removes and returns element
        current = heapq.heappop(openList)
        closedList.append(current)
        # print(closedList[0].value)
        if current.value == goal:
            break
        else:
            openList = expandNode(current, openList, closedList, grid, goal, start)
            numExpanded += 1
    # if not openList.empty() or current == goal:
    if len(openList) > 0 or current == goal:
        setPath(current, path)
        path.append(goal)

    return [path, numExpanded]


def main():
    grid = readGrid('grid.txt')
    print("The grid is:")
    printGrid(grid)

    start = [1, 1]  # [0,0]
    goal = [4, 3]  # [3,8]

    print("\nStarting A* Search: ")
    [path, numExpanded] = aStarSearch(grid, start, goal)

    if len(path) > 0:
        print("\nPath:", path)
        print("\nNumber of nodes expanded:", numExpanded)  # should be = 10
        print("\nPath cost:", getPathCost(path, grid))
        outputGrid(grid, start, goal, path)
    else:
        print("A path wasn't found")


if __name__ == '__main__':
    main()
