infile = "input"
lines = open(infile).read()[0:-1].split("\n")

closers = {'[': ']', '{': '}', '<': '>', '(': ')'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
closer_values = [closers[key] for key in closers]
autocomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}

def syntax_error_score(line):
    opens = []
    i = 0
    syntax_valid = True
    while i < len(line) and syntax_valid:
        if line[i] in closer_values and closers[opens.pop()] != line[i]:
            syntax_valid = False
        elif line[i] in closer_values:
            i += 1
        else:
            opens.append(line[i])
            i += 1
    if i != len(line):
        return scores[line[i]]
    else:
        return 0

# Part 1
print(sum(map(syntax_error_score, lines)))
# Part 2
def autocomplete_score(line):
    closes_needed = []
    for c in line:
        if c in closer_values:
            closes_needed.pop()
        else:
            closes_needed.append(closers[c])
    closes_needed = closes_needed[::-1]
    score = 0
    while len(closes_needed) > 0:
        score *= 5
        score += autocomplete_scores[closes_needed[0]]
        closes_needed = closes_needed[1:]
    return score

scores = list(map(autocomplete_score, filter(lambda line: syntax_error_score(line) == 0, lines)))
scores.sort()
print(scores[(len(scores) - 1) // 2])
