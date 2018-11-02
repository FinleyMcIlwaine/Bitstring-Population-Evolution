import random

# generates 'n' initial people of with genetic length 'l' and fitness level 'f'
def makePeople(n, l, f):
    # correct inputs
    f = 10 if f>=10 else 0 if f<0 else f
    n = 20 if n<=0  else n
    l = 20 if n<=0  else l

    # generate fitness array for randomization
    percFitness = [0] * 20
    i = 1
    while i<=f:
        percFitness[i] = 1
        i += 1

    # create people array to be filled
    people = [[0 for x in range(l)] for y in range(n)]

    # loop to fill array of people
    for i in range(n):
        for j in range(l):
            people[i][j] = random.choice(percFitness)
    return people