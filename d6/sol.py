def solution(lanternfish, days):
    d= {}
    for i in range(9):
        d[i] = 0
    for fish in lanternfish:
        d[fish] += 1
    print(d)
    for day in range(days):
        toReproduce = d[0]
        for i in range(8):
            d[i] = d[i+1]
        d[8] = toReproduce
        d[6] += toReproduce
    print(d)
    return sum([d[i] for i in d.keys()])

def parseinput(file):
    line = ""
    for l in file:
        line = l.split(",")
    file = line
    l = []
    for item in file:
        l.append(int(item))
    return l

f = open("input.txt", "r")
l = parseinput(f)
print(solution(l, 256))