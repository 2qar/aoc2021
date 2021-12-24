moves = [s.split(" ") for s in open("input", "r").read().split("\n")[0:-1]]

# Part 1
x = 0
y = 0
for move in moves:
    if move[0] == "forward":
        x += int(move[1])
    elif move[0] == "down":
        y += int(move[1])
    elif move[0] == "up":
        y -= int(move[1])
print(x*y)

# Part 2
x = 0
y = 0
aim = 0
for move in moves:
    if move[0] == "forward":
        x += int(move[1])
        y += aim * int(move[1])
    elif move[0] == "down":
        aim += int(move[1])
    elif move[0] == "up":
        aim -= int(move[1])
print(x*y)
