import random
import numpy as np

class Individual:
    def __init__(self, graph):
        self.genotype = np.arange(start=0, stop=graph.nodes, step=1)
        self.penalty = 0
        self.score = 0
        self.iteration = 0
        self.tag = 0
    def __str__(self):
        return "{}\n{}".format(self.genotype, self.score)
    def __repr__(self) -> str:
        representation = ""
        representation += "{}\n".format(self.genotype)
        representation += "Tag: {}\n".format(hex(self.tag))
        representation += "Created in {} iteration\n".format(self.iteration)
        representation += "Penalty: {}\n".format(self.penalty)
        representation += "Score: {}\n".format(self.score)
        return representation

    def generate_genotype(self, graph):
        colors=0
        for i in range(len(self.genotype)):
            self.genotype[i] = random.randint(0, graph.nodes)
            if self.genotype[i] == colors:
                colors+=1
        self.correct_genotype(graph)
        self.score = len(np.unique(self.genotype))
        self.generate_tag()

    def correct_genotype(self, graph):
        self.penalty = 0
        colors = np.max(self.genotype)+1
        for i in range(len(self.genotype)):
            for j in range(len(self.genotype)):
                if (graph.edges[i][j] == 1
                and self.genotype[i] == self.genotype[j]):
                    self.penalty+=1

    def breeding(self, ind_a, ind_b, graph):
        for i in range(len(self.genotype)):
            if i < len(self.genotype)/2:
                self.genotype[i] = ind_a.genotype[i]
            else:
                self.genotype[i] = ind_b.genotype[i]
        self.mutate()
        self.correct_genotype(graph)
        self.generate_tag()
        self.score = len(np.unique(self.genotype))


    def mutate(self):
        for i in range(len(self.genotype)):
            if random.uniform(0, 1) < 0.05:
                self.genotype[i] = random.randint(0, np.max(self.genotype))

    def generate_tag(self):
        self.tag = 0
        for i in range(len(self.genotype)):
            self.tag += int(self.genotype[i])*2**(len(self.genotype)-i-1)
