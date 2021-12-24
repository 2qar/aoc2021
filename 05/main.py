from collections import namedtuple
import sys

Point = namedtuple("Point", ["x", "y"])

def point(p_str):
    (x,y) = [int(n) for n in p_str.split(",")]
    return Point(x,y)

def add_point(p, points_dict):
    if p in points_dict:
        points_dict[p] += 1
    else:
        points_dict[p] = 1

def point_add(p1, p2):
    return Point(p1.x + p2.x, p1.y + p2.y)

def direction(p1, p2):
    p = Point(p2.x - p1.x, p2.y - p1.y)
    if p.x != 0:
        p = Point(1, p.y) if p.x > 0 else Point(-1, p.y)
    if p.y != 0:
        p = Point(p.x, 1) if p.y > 0 else Point(p.x, -1)
    return p

def all_nonzero(p):
    return p.x != 0 and p.y != 0

def add_line(line_str, points_dict, add_diagonal=False):
    p1, p2 = [point(p) for p in line.split(" -> ")]
    if not add_diagonal and all_nonzero(direction(p1, p2)):
        return
    while p1.x != p2.x or p1.y != p2.y:
        add_point(p1, points_dict)
        p1 = point_add(p1, direction(p1, p2))
    add_point(p1, points_dict)

lines = open("input").read()[0:-1].split('\n')
# Part 1
points_dict = {}
for line in lines:
    add_line(line, points_dict)
print(len(list(filter(lambda p: points_dict[p] > 1, points_dict.keys()))))

# Part 2
points_dict= {}
for line in lines:
    add_line(line, points_dict, add_diagonal=True)
print(len(list(filter(lambda p: points_dict[p] > 1, points_dict.keys()))))
