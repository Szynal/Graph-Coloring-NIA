import numpy as np
def load_graph(filename):
    edges = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    nodes = int(lines[0])
    graph = np.zeros((nodes, nodes))
    for i, line in enumerate(lines):
        if i > nodes:
            break
        for word in line.split():
            if word != '0':
                graph[i-1][int(word)-1]=1
    return graph

def save_data(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def main():
    graph = load_graph('graphs/110_n5_m8.graph')
    print(graph)

if __name__=="__main__":
    main()
