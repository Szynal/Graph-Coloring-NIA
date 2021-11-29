import numpy as np


class Graph:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        self.nodes = int(lines[0])
        self.edges = np.zeros((self.nodes, self.nodes))
        for i, line in enumerate(lines):
            if i == 0:
                continue
            if i > self.nodes:
                break
            for word in line.split():
                if word != '0':
                    self.edges[i - 1][int(word) - 1] = 1
        self.number_of_edges = np.count_nonzero(self.edges)

    def __str__(self):
        return "Krawędzie:\n{}\nLiczba wierzchołków: {}\nLiczba krawędzi: {}\n".format(self.edges, self.nodes,
                                                                                       self.number_of_edges)
