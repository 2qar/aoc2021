infile = "example"
risks = [[int(c) for c in line] for line in open(infile).read()[0:-1].split("\n")]

# Use A* i guess, each risk is a weight sorta
