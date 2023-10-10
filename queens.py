from typing import List
from random import randint

# Important constants
MUTATION_RATE = 2
POPULATION_SIZE = 300
GENERATIONS = 1000
QUEENS = 8


class Individual:
    """
    an individual is a chromosome.
    chromosome is a list of integers that represents the location of the queen in each column.
    """

    def __init__(self, chromosome: List[int]):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @classmethod
    def random(cls) -> 'Individual':
        """
        create a random individual
        :return: a new individual
        """
        return cls([randint(0, QUEENS - 1) for _ in range(QUEENS)])

    def calculate_fitness(self) -> int:
        """
        calculate the fitness of the individual. Each conflict is a point.
        The lower the fitness, the better the individual.
        :return: the fitness of the individual (the number of conflicts)
        """
        conflicts = 0
        for i in range(len(self.chromosome)):
            for j in range(len(self.chromosome)):
                if i == j:
                    continue
                if self.chromosome[i] == self.chromosome[j]:
                    conflicts += 1
                if abs(self.chromosome[i] - self.chromosome[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def mutate(self):
        """
        mutate the individual by changing a random gene
        """
        self.chromosome[randint(0, len(self.chromosome) - 1)] = randint(0, len(self.chromosome) - 1)

    def crossover(self, other: 'Individual') -> 'Individual':
        """
        crossover between two individuals (aka mate them)
        :param other: the other individual to mate with
        :return: a new individual
        """
        return Individual(self.chromosome[:len(self.chromosome) // 2] + other.chromosome[len(self.chromosome) // 2:])

    def __add__(self, other: 'Individual'):
        """
        Just to make things more readable
        rather than writing: child = parent1.crossover(parent2)
        we can write: child = parent1 + parent2
        :param other: the other individual to mate with
        :return: a new individual
        """
        return self.crossover(other)

    def print_board(self):
        """
        Simple function to print the board
        """
        print(f"Fitness: {self.fitness}")
        for i in range(len(self.chromosome)):
            for j in range(len(self.chromosome)):
                if self.chromosome[i] == j:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()
        print("="*10)


class GeneticAlgo:
    """
    The main class that runs the genetic algorithm
    """

    def __init__(self):
        """
        Initialize the population with random individuals
        """
        self.population = [Individual.random() for _ in range(POPULATION_SIZE)]

    def run(self):
        """
        The core logic of the algorithm
        For the given number of generations:
            1. Sort the population by fitness
            2. If the best individual has a fitness of 0, we are done
            3. Create a new population by taking the best individuals and mate them
            4. Mutate the new population
            5. Replace the old population with the new population
        Print the best individual
        """
        gen = 0
        for gen in range(GENERATIONS):
            self.population.sort(key=lambda x: x.fitness)
            if self.population[0].fitness == 0:
                break
            new_population = self.population[:POPULATION_SIZE // 2]
            for _ in range(POPULATION_SIZE // 2):
                parent1 = new_population[randint(0, len(new_population) - 1)]
                parent2 = new_population[randint(0, len(new_population) - 1)]
                child = parent1 + parent2
                if randint(0, 100) <= MUTATION_RATE:
                    child.mutate()
                new_population.append(child)
            self.population = new_population
        self.population.sort(key=lambda x: x.fitness)
        print(f"Generation: {gen}")
        self.population[0].print_board()


if __name__ == '__main__':
    GeneticAlgo().run()
