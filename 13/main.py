import sys

infile = "input"
(point_strs, fold_strs) = [l.split('\n') for l in open(infile).read()[0:-1].split("\n\n")]
def make_point(point_str):
    (n1, n2) = point_str.split(",")
    return (int(n1), int(n2))
points = [make_point(s) for s in point_strs]
def make_fold(fold_str):
    fold_str = fold_str.split(" ")[2]
    (axis, n) = fold_str.split("=")
    return (axis, int(n))
folds = [make_fold(s) for s in fold_strs]

# yes, it's copy-pasted. no, i don't care
def fold_x(points, x):
    remaining = set(filter(lambda p: p[0] < x, points))
    for p in filter(lambda p: p[0] > x, points):
        remaining.add((2*x - p[0], p[1]))
    return remaining

def fold_y(points, y):
    remaining = set(filter(lambda p: p[1] < y, points))
    for p in filter(lambda p: p[1] > y, points):
        remaining.add((p[0], 2*y - p[1]))
    return remaining

def fold(points, fold):
    if fold[0] == 'x':
        return fold_x(points, fold[1])
    else:
        return fold_y(points, fold[1])

print(len(fold(points, folds[0])))
for f in folds:
    points = fold(points, f)
max_x = max(points, key=lambda p: p[0])[0]
max_y = max(points, key=lambda p: p[1])[1]

for y in range(max_y + 1):
    for x in range(max_x + 1):
        sys.stdout.write("#" if (x,y) in points else ".")
    sys.stdout.write("\n")
