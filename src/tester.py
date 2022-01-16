from genetic_algorithm import GeneticAlgorithm
from graph import Graph
import numpy as np

population_sizes = (50, 100, 150)
numbers_of_generations = (50, 100, 150)
graph = Graph("graphs/jean.graph")
# graph = Graph("graphs/projekt0_n10_m4.graph")
combinations = []
for size in population_sizes:
    for gen in numbers_of_generations:
        combinations.append((size, gen))
results = np.zeros((len(combinations), 10))
for i, subset in enumerate(combinations):
    for j in range(10):
        alg = GeneticAlgorithm(graph)
        alg.generate_population(subset[0])
        alg.run_algorithm(subset[1], None)
        print(f"Iteracja {(10 ** i -1) + j+1}/{len(combinations)*10}")
        if alg.lowest_penalties[-1] == 0:
            results[i][j] = alg.best_scores[-1]
        else:
            results[i][j] = graph.nodes
print(results)
avg_result = np.mean(results, axis=1)
for i, subset in enumerate(combinations):
    print(f"Pop: {subset[0]} Gen: {subset[1]} Avg_ score: {avg_result[i]}")
