import operator
import functools

infile = "input"
heightmap = [[int(c) for c in line] for line in open(infile).read()[0:-1].split("\n")]

# Part 1
def is_low_point(i,j):
    is_low = True
    height = heightmap[i][j]
    if i != 0:
        is_low &= height < heightmap[i-1][j]
    if j != 0:
        is_low &= height < heightmap[i][j-1]
    if i != len(heightmap) - 1:
        is_low &= height < heightmap[i+1][j]
    if j != len(heightmap[0]) - 1:
        is_low &= height < heightmap[i][j+1]
    return is_low

low_points = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if is_low_point(i,j):
            low_points.append((i,j))
print(sum(map(lambda p: heightmap[p[0]][p[1]] + 1, low_points)))

# Part 2
def basin_size_aux(p, prev_height, seen):
    i,j = p[0],p[1]
    if i == -1 or i == len(heightmap) or j == -1 or j == len(heightmap[0]):
        return 0
    elif (i,j) in seen or heightmap[i][j] == 9:
        return 0
    elif heightmap[i][j] < prev_height:
        return 0
    else:
        seen[(i,j)] = True
        return 1 + sum(map(lambda p: basin_size_aux(p, heightmap[i][j], seen), [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]))

def basin_size(low_point):
    return basin_size_aux(low_point, -1, {})

def product(xs):
    return functools.reduce(operator.mul, xs, 1)

basin_sizes = list(map(basin_size, low_points))
basin_sizes.sort(reverse=True)
top_sizes = basin_sizes[0:3]
print(product(top_sizes))
