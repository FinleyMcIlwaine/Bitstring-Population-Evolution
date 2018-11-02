import random

# generates 'n' initial bit strings of length 'l'
def makeBitStrings(n, l, f):
    # correct fitness input
    f = 10 if f>=10 else 0 if f<0 else f

    percFitness = [0] * 20
    i = 1
    while i<=f:
        percFitness[i] = 1
        i = i + 1

    # create empty list to be filled
    bitStrings = [""] * n

    # loop to fill bitStrings array
    for i in range(n):

        # loop to fill each bit string
        for _ in range(l):
            bitStrings[i] += str(random.choice(percFitness))

    return bitStrings



# @n -> number of people (strings) in the population
# @l -> length of genetic data (strings) for each person
n = int(input("Enter desired population size:   "))
l = int(input("Enter length of genetic data:    "))
f = int(input("\nEnter fitness level of population\n(0 for lazy slobs, 10 for athletic specimens): "))
print("\nGenerating population...\n")

# make the people
bitStrings = makeBitStrings(n,l,f)

# confirm start of evolution
# start = input("Start evolution? (Y/N): ")

for item in bitStrings:
    print(item)
