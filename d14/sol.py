from collections import defaultdict

rule_dict = defaultdict(None)
pair_count = defaultdict(int)
elem_count = defaultdict(int)
polymer = ""
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "->" in line:
            line = line.split(" -> ")
            rule_dict[line[0]] = line[1]
        elif len(line) > 0:
            for i in range(len(line)-1):
                pair_count[line[i]+line[i+1]] += 1
                elem_count[line[i]] += 1
            elem_count[line[-1]] += 1


def solution(steps, pair_count, rule_dict, elem_count):
    for i in range(steps):
        new_pair_count = defaultdict(int)
        for pair in pair_count:
            c = pair_count[pair]
            new_elem = rule_dict[pair]
            a, b = pair[0] + rule_dict[pair], rule_dict[pair] + pair[1]
            new_pair_count[a] += c
            new_pair_count[b] += c
            elem_count[new_elem] += c
        pair_count = new_pair_count
    
    quantities = [elem_count[k] for k in elem_count.keys()]
    print(max(quantities) - min(quantities)) 
solution(10, pair_count.copy(), rule_dict, elem_count.copy())
solution(40, pair_count.copy(), rule_dict, elem_count.copy())
