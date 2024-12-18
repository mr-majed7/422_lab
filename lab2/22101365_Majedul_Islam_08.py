import random


def fitness(n, t, chromsome):
    fitness_val = 0
    i = 0

    keys = range(0, t)
    count = {key: 0 for key in keys}

    while i < n * t:
        segment = chromsome[i : i + n]
        fitness_val += 0 if segment.count("1") - 1 < 0 else segment.count("1") - 1

        for j in range(len(segment)):
            if segment[j] == "1":
                count[j] += 1
        i += n
    for k in count.keys():
        fitness_val += abs(count[k] - 1)

    return fitness_val * -1


def random_selection(parents):
    """Consecutive pairs will be selected for crossover"""
    random.shuffle(parents)
    return parents


def crossover(parents):
    parents = random_selection(parents)
    offsprings = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]

        crossover_point = random.randint(1, len(parent1) - 1)

        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        offsprings.extend([child1, child2])
    return offsprings


def mutation(chromosomes, n):
    mutated_chromosomes = []

    for chromosome in chromosomes:
        chromosome_list = list(chromosome)

        i = random.randint(0, n - 1)
        chromosome_list[i] = "1" if chromosome_list[i] == "0" else "0"

        mutated_chromosomes.append("".join(chromosome_list))

    return mutated_chromosomes


def genetic_algo(maxiter, parents, n, t):
    current_chromosomes = parents

    best_fitness = float("-inf")
    best_chromosome = ""
    i = 0

    while i <= maxiter:
        for c in current_chromosomes:
            current_fitness = fitness(n, t, c)
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_chromosome = c
        if best_fitness == 0:
            return [best_chromosome, best_fitness]
        current_chromosomes = mutation(crossover(current_chromosomes), n)
        i += 1
    return (best_chromosome, best_fitness)


def generate_parents(n, t):
    length = n * t
    parents = []
    for _ in range(4):
        parent = "".join(random.choice("01") for _ in range(length))
        parents.append(parent)
    random.shuffle(parents)
    return parents


N = int(input("Enter the Value of N:"))
T = int(input("Enter the Value of T:"))
parents = generate_parents(N, T)
print(genetic_algo(10000, parents, N, T))


def two_point_crossover(parents):
    parent1, parent2 = parents

    point1 = random.randint(0, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)

    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return [child1, child2]


print(two_point_crossover(["000111000", "111000111"]))
