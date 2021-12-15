from itertools import product

def grid_range(i, j):
    ranges = list(product(range(max(0, i-1),min(i+1, width-1)+1),range(max(0, j-1), min(j+1,height-1)+1)))
    ranges.remove((i,j))
    return ranges

grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append([int(num) for num in line.strip()])

height = len(grid)
width = len(grid[0])


def part1():

    num_flashes = 0
    for step in range(100):
        hasFlashed = set()
        stack = []
        # increment all energy by 1
        for i in range(height):
            for j in range(width):
                grid[i][j] += 1

                # if flashes
                if grid[i][j] > 9:
                    stack.append((i, j))

        # while some octopus is due to flash
        while stack != []:
            i, j = stack.pop()
            if (i, j) in hasFlashed:
                continue
            hasFlashed.add((i, j))
            num_flashes += 1

            for x, y in grid_range(i, j):
                grid[x][y] += 1

                #if neighbour flashes and has not already flashed
                if grid[x][y] > 9 and (x, y) not in hasFlashed:
                    stack.append((x, y))
                    hasFlashed.add((i, j))

        #set all flashed energy to 0
        for i, j in hasFlashed:
            grid[i][j] = 0
    

    print(num_flashes)

def part2():

    num_steps = 0
    all_flashed = False
    while all_flashed == False:
        hasFlashed = set()
        stack = []
        # increment all energy by 1
        for i in range(height):
            for j in range(width):
                grid[i][j] += 1

                # if flashes
                if grid[i][j] > 9:
                    stack.append((i, j))

        while stack != []:
            i, j = stack.pop()
            if (i, j) in hasFlashed:
                continue
            hasFlashed.add((i, j))
            for x, y in grid_range(i, j):
                grid[x][y] += 1
                if grid[x][y] > 9 and (x, y) not in hasFlashed:
                    stack.append((x, y))
                    hasFlashed.add((i, j))

        #set all flashed energy to 0
        for i, j in hasFlashed:
            grid[i][j] = 0
    
        not_zero = True
        for i, j in product(range(height), range(width)):
            if grid[i][j] != 0:
                not_zero = False
        if not_zero == True:
            all_flashed = True
    
        num_steps += 1

    print(num_steps)

part1()
                





