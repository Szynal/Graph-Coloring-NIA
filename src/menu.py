from graph import Graph
from individual import Individual
from genetic_algorithm import GeneticAlgorithm
import numpy as np

def main():
    temp()

def temp():
    graph = Graph("graphs/projekt0_n50_m854.graph")
    alg = GeneticAlgorithm(graph)
    alg.generate_population(100)
    alg.run_algorithm(50)
    alg.export_results("res.txt", "")

def menu():
    graph = ""
    choice = 0
    prompt = 'MENU\tWybierz opcję:\n1.Wczytaj graf\n2.Wyświetl graf\n3.Algorytm referencyjny\n4.Algorytm genetyczny\n5.Wyświetl wyniki\n6.Wyeksportuj wyniki\n7.Wyjście\n'
    while True:
        try:
            choice = int(input(prompt))
        except:
            continue
        match choice:
            case 1:
                filename = input("Podaj nazwę pliku z grafem (domyślnie=graphs/projekt0_n10_m28.graph)")
                if filename == "":
                    filename="graphs/projekt0_n10_m28.graph"
                try:
                    graph = Graph(filename)
                except FileNotFoundError:
                    print('Nie znaleziono pliku o podanej nazwie!')
            case 2:
                print(graph)
            case 5:
                print()
            case 7:
                break
        print("\n")

if __name__=="__main__":
    main()
