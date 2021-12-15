import math

f = open("input.txt", "r")
crabs = []
for l in f:
    l = l.split(",")
    crabs = l

crabs = [int(crab) for crab in crabs]
max = max(crabs)
best = float("inf")
best_pos = 0
for i in range(max):
    s = sum([abs(i-crab)*(abs(i-crab)+1)/2 for crab in crabs])
    if best >= s:
        best_pos = i
        best = s
print(best)
"""
for pos in crabs:
    sum += int(pos)
mean = sum / len(crabs)
num_above = len([crab for crab in crabs if int(crab) >= mean])
num_below = len([crab for crab in crabs if int(crab) < mean])
print(math.ceil(mean)) if num_above >= num_below else print(math.floor(mean))
"""