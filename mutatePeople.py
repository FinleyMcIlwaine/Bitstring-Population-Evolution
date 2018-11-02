import random

# This function mutates the given population.
# Mutations occur based on the probability that is decided
# by the user's input.

def mutatePeople(people, percMutate):
    # generations count
    generations = 1

    # perfect person for comparison
    perfectPerson = [1] * len(people[0])

    # mutation randomization array
    mutationChance = [1]
    for i in range(9 - percMutate):
        mutationChance.append(0)

    # check for perfect person in generation 1
    for person in people:
        # check if current person is perfect
        if person == perfectPerson:
            return (generations, people.index(person))

    # evolve while there is not a perfect person
    while generations < 100000:
        # loop over people
        for person in people:
            # mutate person
            for i, gene in enumerate(person):  
                if gene == 0:  
                    person[i] = random.choice(mutationChance)

            # check if current person is perfect
            if person == perfectPerson:
                return (generations, people.index(person))

            # increment to next generation
            generations += 1
    
    return -1