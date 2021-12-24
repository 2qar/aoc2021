ages_list = [int(x) for x in open("input").read()[0:-1].split(",")]

def step0(ages_list):
    ages = [0] * 9
    for age in ages_list:
        ages[age] += 1
    return ages

def step(ages):
    new_6 = ages[0]
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7] + new_6
    ages[7] = ages[8]
    ages[8] = new_6

def population(days):
    ages = step0(ages_list)
    i = 0
    while i < days:
        step(ages)
        i += 1
    return sum(ages)

print(population(80))
print(population(256))
