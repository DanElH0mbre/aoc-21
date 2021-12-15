scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
comp_scores = {")": 1, "]": 2, "}": 3, ">": 4}
open_brackets = ["(", "[", "{", "<"]
close_brackets = [")", "]", "}", ">"]
score = 0
incomplete_scores = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        stack = []
        is_corrupt = False
        c = 0
        while is_corrupt == False and c < len(line):
            char = line[c]
            c += 1
            try:
                is_closed = False
                for option in range(len(close_brackets)):
                    if char == close_brackets[option]:
                        is_closed = True
                        assert stack[-1] == open_brackets[option]
                        stack.pop()
                if is_closed == False:
                    stack.append(char)
            except:
                score += scores[char]
                is_corrupt = True
        if is_corrupt == False:
            completion_score = 0
            for char in reversed(stack):
                for option in range(len(open_brackets)):
                    if char == open_brackets[option]:
                        completion_score = 5 * completion_score + comp_scores[close_brackets[option]]
            incomplete_scores.append(completion_score)
            
print(score)
print(sorted(incomplete_scores)[int(len(incomplete_scores)/2)])
