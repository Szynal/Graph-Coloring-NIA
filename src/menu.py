from graph import Graph
from genetic_algorithm import GeneticAlgorithm


def main():
    menu()


def menu():
    alg = ""
    graph = ""
    choice = 0
    prompt = "MENU\tWybierz opcję:\n1.Wczytaj graf\n2.Wyświetl graf\n" \
             "3.Algorytm referencyjny(TODO)\n4.Algorytm genetyczny\n" \
             "5.Wyeksportuj wyniki\n6.Wyjście\n"
    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("To nie jest właściwa opcja!")
            continue
        match choice:
            case 1:
                filename = input("Podaj nazwę pliku z grafem"
                                 "(domyślnie=graphs/projekt0_n50_m854.graph)")
                if filename == "":
                    filename = "graphs/projekt0_n50_m854.graph"
                try:
                    graph = Graph(filename)
                except FileNotFoundError:
                    print('Nie znaleziono pliku o podanej nazwie!')
            case 2:
                print(graph)
            case 4:
                alg = GeneticAlgorithm(graph)
                try:
                    population_size = int(input(
                        "Podaj rozmiar populacji (domyślnie=100): "))
                except ValueError:
                    population_size = 100
                try:
                    number_of_generations = int(input(
                        "Podaj liczbę pokoleń (domyślnie=50): "))
                except ValueError:
                    number_of_generations = 50
                alg.generate_population(population_size)
                alg.run_algorithm(number_of_generations)
            case 5:
                if (alg != ""):
                    alg.export_results(input("Podaj nazwę pliku,"
                                             "do którego chcesz zapisać wyniki"
                                             "(w katalogu exported_results):"),
                                       "")
                else:
                    print("Najpierw należy uruchomić algorytm")
            case 6:
                break
        print("\n")


if __name__ == "__main__":
    main()
