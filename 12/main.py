from copy import copy

infile = "input"
path_strs = open(infile).read()[0:-1].split('\n')

def add_edge(n1, n2, paths):
    if n1 in paths:
        paths[n1].append(n2)
    else:
        paths[n1] = [n2]

def build_graph(path_strs):
    paths = {}
    for path_str in path_strs:
        n1,n2 = path_str.split("-")
        add_edge(n1, n2, paths)
        add_edge(n2, n1, paths)
    return paths

def traverse(node, visited, visited_list, visited_lists, edges, moves_left, small_cave_rule):
    if node in visited:
        visited[node] += 1
    else:
        visited[node] = 1

    visited_list.append(node)
    if node == "end":
        visited_lists.append(visited_list)
    elif node == "start" and visited["start"] > 1:
        return
    elif node != "start" and node.islower() and small_cave_rule(node, visited):
        return
    elif moves_left != 0:
        for node in edges[node]:
            traverse(node, copy(visited), copy(visited_list), visited_lists, edges, moves_left - 1, small_cave_rule)

def part1_small_cave_rule(n, visited):
    return n in visited and visited[n] > 1

def part2_small_cave_rule(n, visited):
    other_cave_visits = list(map(lambda x: visited[x], filter(lambda s: s != n and s.islower() and s != "start" and s != "end", visited.keys())))
    return (visited[n] == 2 and 2 in other_cave_visits) or visited[n] > 2

def good_paths(path_strs, small_cave_rule):
    paths = []
    traverse("start", {}, [], paths, build_graph(path_strs), len(path_strs), small_cave_rule)
    return paths

print(len(good_paths(path_strs, part1_small_cave_rule)))
print(len(good_paths(path_strs, part2_small_cave_rule)))
