from collections import defaultdict

neighbours = defaultdict(list)

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split("-")
        neighbours[line[0]].append(line[1])
        neighbours[line[1]].append(line[0])

def part1():

    paths = [["start"]]
    num_paths = 0
    while len(paths) > 0:
        path = paths.pop()
        endpoint = path[-1]
        for neighbour in neighbours[endpoint]:
            if neighbour == "start":
                continue
            elif neighbour == "end":
                num_paths += 1
            elif neighbour.isupper():
                newpath = path + [neighbour]
                paths.append(newpath)
            elif neighbour not in path:
                newpath = path + [neighbour]
                paths.append(newpath)
    print(num_paths)

def part2():
    paths = [[["start"], True]]
    num_paths = 0
    while len(paths) > 0:
        item = paths.pop()
        path = item[0]
        can_revisit = item[1]
        endpoint = path[-1]
        for neighbour in neighbours[endpoint]:
            if neighbour == "start":
                continue
            elif neighbour == "end":
                num_paths += 1
            elif neighbour.isupper():
                newpath = [path + [neighbour], can_revisit]
                paths.append(newpath)
            elif neighbour not in path:
                newpath = [path + [neighbour], can_revisit]
                paths.append(newpath)
            elif can_revisit:
                newpath = [path + [neighbour], False]
                paths.append(newpath)

    print(num_paths)

def solution(revisit):
    paths = [[["start"], revisit]]
    num_paths = 0
    while len(paths) > 0:
        item = paths.pop()
        path = item[0]
        can_revisit = item[1]
        endpoint = path[-1]
        for neighbour in neighbours[endpoint]:
            if neighbour == "start":
                continue
            elif neighbour == "end":
                num_paths += 1
            elif neighbour.isupper():
                newpath = [path + [neighbour], can_revisit]
                paths.append(newpath)
            elif neighbour not in path:
                newpath = [path + [neighbour], can_revisit]
                paths.append(newpath)
            elif can_revisit:
                newpath = [path + [neighbour], False]
                paths.append(newpath)

    print(num_paths)

part1()
part2()
solution(False)
solution(True)