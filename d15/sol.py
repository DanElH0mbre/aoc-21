import heapq
import time
s = time.time()
f = open("input.txt", "r").read().splitlines()
cave = [[int(line[i]) for i in range(len(f[0]))] for line in f]
h = len(cave)
w = len(cave[0])

def neighbours(i, j, height, width):
    if i > 0:
        yield i - 1, j
    if  i < width - 1:
        yield i + 1, j
    if j > 0:
        yield i, j - 1
    if j < height - 1:
        yield i, j + 1

def calc_risk(cave):
    height = len(cave)
    width = len(cave[0])
    distances = [[float("inf") for j in range(width)] for i in range(height)]
    distances[0][0] = 0
    paths = [(0,(0,0))]
    heapq.heapify(paths)
    while distances[height-1][width-1] == float("inf"):
        cell = heapq.heappop(paths)
        d = cell[0]
        i, j = cell[1][0], cell[1][1]
        for x, y in neighbours(i, j, height, width):
            if distances[i][j] + cave[x][y] < distances[x][y]:
                distances[x][y] = distances[i][j] + cave[x][y]
                heapq.heappush(paths, (distances[x][y],(x, y)))
    print(distances[height-1][width-1])

def transform_cave(cave):
    height = len(cave)
    width = len(cave[0])
    newcave = [[0 for j in range(5*width)] for i in range(5*height)]
    for i in range(5*height):
        for j in range(5*width):
            sourcex = j % width
            sourcey = i % height
            temp_risk = cave[sourcex][sourcey] + i // height + j // width
            risk = 1 + temp_risk % 10 if temp_risk > 9 else temp_risk
            newcave[i][j] = risk
    return newcave

calc_risk(cave)
newcave = transform_cave(cave)
calc_risk(newcave)
print(time.time()-s)

