import copy

infile = "input"
octopi = [[int(c) for c in line] for line in open(infile).read()[0:-1].split('\n')]

def bind(lower, x, upper):
    return max(lower, min(x, upper))

def add_if_ok(p, flashers, octopi):
    if p == (bind(0, p[0], len(octopi)-1), bind(0, p[1], len(octopi[0]) - 1)) and octopi[p[0]][p[1]] != -1:
        old_energy = octopi[p[0]][p[1]]
        octopi[p[0]][p[1]] += 1
        if octopi[p[0]][p[1]] > 9 and old_energy <= 9:
            flashers.append(p)


def flash(p, flashers, octopi):
    octopi[p[0]][p[1]] = -1
    for i in range(p[0]-1,p[0]+2):
        for j in range(p[1]-1,p[1]+2):
            if (i,j) != p:
                add_if_ok((i,j), flashers, octopi)

def step(octopi):
    flashers = []
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            octopi[i][j] += 1
            if octopi[i][j] > 9:
                flashers.append((i,j))
    flashes = 0
    while len(flashers) != 0:
        flash(flashers[0], flashers, octopi)
        flashes += 1
        flashers = flashers[1:]

    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            if octopi[i][j] == -1:
                octopi[i][j] = 0

    return flashes

def do_steps(n):
    mypi = copy.deepcopy(octopi)
    flashes = 0
    i = 0
    while i < n:
        flashes += step(mypi)
        i += 1
    return flashes

def all_zero(octopi):
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            if octopi[i][j] != 0:
                return False
    return True

def first_simulflash():
    mypi = copy.deepcopy(octopi)
    nstep = 0
    while not all_zero(mypi):
        step(mypi)
        nstep += 1
    return nstep

print(do_steps(100))
print(first_simulflash())
