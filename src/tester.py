from genetic_algorithm import GeneticAlgorithm
from graph import Graph
import numpy as np
from scipy.stats import ttest_rel
from tabulate import tabulate

population_sizes = (50, 100, 150)
numbers_of_generations = (50, 100, 150)
graph = Graph("graphs/games120.graph")
# graph = Graph("graphs/miles750.graph")
combinations = []
for size in population_sizes:
    for gen in numbers_of_generations:
        combinations.append((size, gen))
print(combinations)
iterations = 5
results = np.zeros((len(combinations), iterations))
loop_index = 1
for i, subset in enumerate(combinations):
    for j in range(iterations):
        print(f"Iteracja {loop_index}/{len(combinations)*iterations}")
        alg = GeneticAlgorithm(graph)
        alg.generate_population(subset[0])
        alg.run_algorithm(subset[1], None)
        loop_index += 1
        if alg.lowest_penalties[-1] == 0:
            results[i][j] = alg.best_scores[-1]
        else:
            results[i][j] = graph.nodes
print(results)
avg_result = np.mean(results, axis=1)
for i, subset in enumerate(combinations):
    print(f"Pop: {subset[0]} Gen: {subset[1]} Avg_ score: {avg_result[i]}")

alfa = .05
t_statistic = np.zeros((len(combinations), len(combinations)))
p_value = np.zeros((len(combinations), len(combinations)))

for i in range(len(combinations)):
    for j in range(len(combinations)):
        t_statistic[i, j], p_value[i, j] = ttest_rel(results[i], results[j])
print("t-statistic:\n", t_statistic, "\n\np-value:\n", p_value)

headers = ["50, 50", "50, 100", "50, 150", "100, 50", "100, 100", "100, 150", "150, 50", "150, 100", "150, 150"]
names_column = np.array([["50, 50"], ["50, 100"], ["50, 150"], ["100, 50"], ["100, 100"], ["100, 150"], ["150, 50"], ["150, 100"], ["150, 150"]])
t_statistic_table = np.concatenate((names_column, t_statistic), axis=1)
t_statistic_table = tabulate(t_statistic_table, headers, floatfmt=".2f")
p_value_table = np.concatenate((names_column, p_value), axis=1)
p_value_table = tabulate(p_value_table, headers, floatfmt=".2f")
print("t-statistic:\n", t_statistic_table, "\n\np-value:\n", p_value_table)

advantage = np.zeros((len(combinations), len(combinations)))
advantage[t_statistic < 0] = 1
advantage_table = tabulate(np.concatenate(
    (names_column, advantage), axis=1), headers)
print("Advantage:\n", advantage_table)

significance = np.zeros((len(combinations), len(combinations)))
significance[p_value <= alfa] = 1
significance_table = tabulate(np.concatenate(
    (names_column, significance), axis=1), headers)
print("Statistical significance (alpha = 0.05):\n", significance_table)

stat_better = significance * advantage
stat_better_table = tabulate(np.concatenate(
    (names_column, stat_better), axis=1), headers)
print("Statistically significantly better:\n", stat_better_table)
