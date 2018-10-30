import random

# generates 'n' initial bit strings of length 'l'
def makeBitStrings(n, l):
    # create empty list to be filled
    bitStrings = [""] * n

    # loop to fill bitStrings array
    for i in range(n):

        # loop to fill each bit string
        for _ in range(l):
            bitStrings[i] += str(random.choice([1,0,0]))

    return bitStrings



# @n -> number of people (strings) in the population
# @l -> length of genetic data (strings) for each person
n = int(input("Enter desired population size: "))
l = int(input("Enter length of genetic data:  "))
print("\nGenerating population...\n")

# @gens -> number of generations to create
# @speed-> speed that evolution will take place
gens = int(input("Enter number of generations evolve: "))
speed= int(input("\nEnter speed of evolution\n(slow=1, fast=100): "))

# make the people
bitStrings = makeBitStrings(n,l)

for item in bitStrings:
    print(item)
