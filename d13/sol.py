dots = []
folds = []
width = 0
height = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "," in line:
            x, y = line.split(",")
            dots.append((int(x), int(y)))
            width = max(width, int(x))
            height = max(height, int(y))
        elif "=" in line:
            ax, line = line.split(" ")[2].split("=")
            folds.append((ax, int(line)))

grid = [[False for j in range(width+1)] for i in range(height+1)]
for dot in dots:
    grid[dot[1]][dot[0]] = True

def count_dots(grid):
    height = len(grid)
    width = len(grid[0])
    c=0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == True:
                c += 1
    return c

def fold_x(x, grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width - x):
            grid[row][x - col] = grid[row][x - col] or grid[row][x + col]
        grid[row] = grid[row][:x]

    return grid

def fold_y(y, grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height - y):
        for col in range(width):
            grid[y - row][col] = grid[y - row][col] or grid[y + row][col]
    grid = grid[:y]
    return grid

for ax, line in folds:
    if ax == "x":
        grid = fold_x(line, grid)
    else:
        grid = fold_y(line, grid)
    print(count_dots(grid))
for row in grid:
    row = "".join(["#" if row[i] == True else " " for i in range(len(row))])
    print(row)

