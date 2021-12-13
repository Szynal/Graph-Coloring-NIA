class Algorithm:
    def __init__(self):
        self.results = []
        self.type = ""

    def __str__(self):
        return "Algorytm: {}\nWyniki:\n{}".format(self.type, self.results)

    def __repr__(self):
        return f"Algorithm({self.results}, '{self.type}')"

    def export_results(self, filename):
        with open(filename, 'w') as file:
            file.write(self.results)
