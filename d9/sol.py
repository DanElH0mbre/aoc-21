grid = []
with open("input.txt", "r") as f:
    for l in f:
        grid.append([int(c) for c in l.strip()])

def adj_cells(grid, i, j):
        if i > 0:
            yield (i-1, j)
        if i < len(grid) - 1:
            yield (i+1, j)
        if j > 0:
            yield (i, j-1)
        if j < len(grid[0]) - 1:
            yield (i, j+1)

def part1():
    total_risk = 0
    for row in range(len(grid)):
        for entry in range(len(grid[0])):
            isLow = True
            for cell in adj_cells(grid, row, entry):
                if grid[row][entry] >= grid[cell[0]][cell[1]]:
                    isLow = False
            if isLow == True:
                total_risk += 1 + grid[row][entry]
    print(total_risk)

def part2():
    is_basin = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    basin_sizes = []
    for row in range(len(grid)):
        for entry in range(len(grid[0])):
            if is_basin[row][entry] == 1:
                continue
            isLow = True
            for cell in adj_cells(grid, row, entry):
                if grid[row][entry] >= grid[cell[0]][cell[1]]:
                    isLow = False
            if isLow == True:
                size = 0
                stack = [(row, entry)]
                is_basin[row][entry] = 1
                while stack != []:
                    pos = stack.pop()
                    row = pos[0]
                    col = pos[1]
                    size += 1
                    for r, c in adj_cells(grid, row, col):
                        if grid[r][c] == 9 or is_basin[r][c] == 1:
                            continue
                        if is_basin[r][c] == 0:
                            stack.append((r, c))  
                            is_basin[r][c] = 1
                basin_sizes.append(size)
    basin_sizes = sorted(basin_sizes)
    print(basin_sizes)
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
                
part1()         
part2()