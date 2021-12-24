import functools
import operator

infile = "input"

(template, rules_str) = open(infile).read()[0:-1].split("\n\n")

def make_rules(rules_str):
    rules = {}
    for s in rules_str.split("\n"):
        (start, deriv) = s.split(" -> ")
        rules[start] = deriv
    return rules

def pair_insert(polymer, inserts_left, rules, expanded):
    if inserts_left == 0:
        return {}
    elif (inserts_left, polymer) in expanded:
        return expanded[(inserts_left, polymer)]
    mat = rules[polymer]
    counts = {mat: 1}
    c1 = pair_insert(polymer[0] + mat, inserts_left - 1, rules, expanded)
    c2 = pair_insert(mat + polymer[1], inserts_left - 1, rules, expanded)
    for c in c1:
        counts[c] = counts.get(c, 0) + c1[c]
    for c in c2:
        counts[c] = counts.get(c, 0) + c2[c]
    expanded[(inserts_left, polymer)] = counts
    return counts

def do_pair_inserts(template, rules, steps):
    expanded = {}
    total_counts = {}
    for i in range(len(template)-1):
        counts = pair_insert(template[i:i+2], steps, rules, expanded)
        for c in counts:
            total_counts[c] = total_counts.get(c, 0) + counts[c]
    for c in template:
        total_counts[c] = total_counts.get(c, 0) + 1

    counts = list(total_counts.items())
    counts.sort(key=lambda p: p[1])
    min_occ = counts[0][1]
    max_occ = counts[len(counts)-1][1]
    print(max_occ - min_occ)

rules = make_rules(rules_str)
do_pair_inserts(template, rules, 10)
do_pair_inserts(template, rules, 40)
