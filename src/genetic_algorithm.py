from algorithm import Algorithm
from individual import Individual
from math import ceil, floor
import random


class GeneticAlgorithm(Algorithm):
    def __init__(self, graph):
        self.type = "Genetyczny"
        self.population = []
        self.graph = graph

    def generate_population(self, size):
        for i in range(size):
            individual = Individual(self.graph)
            individual.generate_genotype(self.graph)
            self.population.append(individual)

    def roulette_breeding(self, iteration):
        total_score = 0
        total_penalty = 0
        copied_size = floor(0.15 * len(self.population))
        bred_size = ceil(0.85 * len(self.population))
        if bred_size % 2 == 1:
            copied_size += 1
            bred_size -= 1
        self.population.sort(key=lambda x: (x.penalty, x.score), reverse=False)
        new_population = []
        for i in range(copied_size):
            new_population.append(self.population[i])
        for individual in self.population:
            total_penalty += self.graph.nodes - individual.penalty
        for i in range(round(bred_size / 2)):
            found = [False, False]
            selected_value = [random.randint(0, total_penalty),
                              random.randint(0, total_penalty)]
            parents = []
            for individual in self.population:
                selected_value[0] -= self.graph.nodes - individual.penalty
                selected_value[1] -= self.graph.nodes - individual.penalty
                if not found[0] and selected_value[0] <= 0:
                    parents.append(individual)
                    found[0] = True
                if not found[1] and selected_value[1] <= 0:
                    parents.append(individual)
                    found[1] = True
                if found[0] and found[1]:
                    break
            ind_a = Individual(self.graph)
            ind_b = Individual(self.graph)
            ind_a.breeding(parents[0], parents[1], self.graph)
            ind_b.breeding(parents[1], parents[0], self.graph)
            ind_a.iteration = iteration
            ind_b.iteration = iteration
            new_population.append(ind_a)
            new_population.append(ind_b)

        new_population.sort(key=lambda x: (x.penalty, x.score), reverse=False)
        self.population = new_population

    def run_algorithm(self, iterations):
        for i in range(iterations):
            self.roulette_breeding(i)
            if i % 10 == 0 or i == iterations - 1:
                print(f"Iteracja {i} - najlepszy osobnik:\nKara:"
                      f"{self.population[0].penalty}\tLiczba kolorów:"
                      f"{self.population[0].score}")

    def export_results(self, filename, parameters):
        try:
            with open("exported_results/" + filename, 'w+') as f:
                if parameters != "":
                    for x, y in parameters.items():
                        f.write("{}: {}\n".format(x, y))
                f.write("\n\n")
                for individual in self.population:
                    f.write(individual.__repr__())
                    f.write('\n')
            return True
        except NotADirectoryError and FileNotFoundError:
            return False
