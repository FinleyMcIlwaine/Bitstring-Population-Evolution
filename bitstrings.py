import random
from makePeople import makePeople
from mutatePeople import mutatePeople

# @n -> number of people (strings) in the population
# @l -> length of genetic data (strings) for each person
# @f -> fitness level of population,
#       gets translated into a probability when generating population
n = int(input("\nEnter desired population size: "))
l = int(input("Enter length of genetic data:  "))
f = int(input("\nEnter (0-10) fitness level of population\n(0 for lazy slobs, 10 for freak athletes): "))

# make the people based on the user's input
# @people -> the total generated population. (2d array of 1s and 0s)
print("\nGenerating population...\n")
people = makePeople(n,l,f)

# @percMutate -> user's desired mutation speed, 
#                gets translated into a probability when mutating.
percMutate = int(input("Enter (0-10) speed of mutation\n(0 for slow, 10 for fast): "))

# @start  -> confirms start of mutations
# @result -> stays -1 if no perfect human is generated, else is defined as
#            a list that holds # of human that became perfect and # of generations
start = input("\nStart mutations? (Y/N): ")
result = -1

# check start input
if start == "Y" or start == "y" or start == "Yes" or start == "yes":
    # start mutations
    print("\nMutating...\n")
    result = mutatePeople(people, percMutate)

    # display evolution results
    if (result == -1):
        print("Perfect human could not be created in <100,000 generations.")
    else:
        print("\nHuman #" + str(result[1]) + " became perfect in " + str(result[0]) + " mutations.")

else:
    print("Mutation cancelled.")