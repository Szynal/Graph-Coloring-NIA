from algorithm import Algorithm
from copy import deepcopy
from individual import Individual
from math import ceil, floor
from matplotlib import pyplot as plt
from pathlib import Path
from datetime import datetime
import random
from gui.console import GuiConsole


class BruteForceAlgorithm(Algorithm):
    def __init__(self, graph):
        self.best_solution = Individual(graph)
        self.best_solution.correct_genotype(graph)
        self.graph = graph
        self.type = "Przegląd zupełny"

    def __repr__(self):
        return f"BruteForceAlgorithm({self.best_solution.genotype}, " \
               f"'{self.graph.name}', '{self.type}')"

    def run_algorithm(self, console):
        solution = Individual(self.graph)
        solution.correct_genotype(self.graph)
        i = 0
        while i < len(solution.genotype):
            if i != 0:
                # if solution[j-1] == len(solution)-1:
                if solution.genotype[i] != len(solution.genotype) - 1:
                    solution.genotype[i] += 1

                    for j in range(0, i):
                        solution.genotype[j] = 0
                    i = 0
                    continue

            for k in range(len(solution.genotype)):
                solution.genotype[0] = k
                solution.correct_genotype(self.graph)
                if solution.penalty < self.best_solution.penalty \
                        or (solution.penalty == self.best_solution.penalty
                            and solution.score < self.best_solution.score):
                    self.best_solution = deepcopy(solution)
            i += 1
        GuiConsole.append_test_to_console(self, console=console, text=self.best_solution.genotype)
        GuiConsole.append_test_to_console(self, console=console, text=f"score: {self.best_solution.score}")
