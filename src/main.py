#!/usr/bin/env python
import sys

from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QRadioButton, QScrollBar,
                             QSlider, QSpinBox, QStyleFactory, QTabWidget, QTextEdit,
                             QVBoxLayout, QMessageBox, QPushButton, QFileDialog, QDoubleSpinBox)

from gui.description import GuiProjectDescription
from gui.error_message import GuiShowErrorMsg
from gui.console import GuiConsole
from gui.progress_bar import ProgressBar

from graph import Graph
from genetic_algorithm import GeneticAlgorithm
from brute_force_algorithm import BruteForceAlgorithm


class WidgetGallery(QDialog):
    version = "v1.0"
    window_title = "Graph-Coloring-NIA "
    style = "Fusion"

    filename = ""
    default_graph = "graphs/projekt0_n50_m854.graph"
    alg = ""
    graph = None

    console = None
    population_size_box = None
    number_of_generations_box = None
    radio_button_bruteforce = None
    radio_button_genetic = None
    gui_description = None
    progressBar = None

    mutation_rate_spin_box = None
    crossing_rate_spin_box = None

    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.mutation_group_box = QGroupBox("Crossing settings")
        self.dataset_group_box = QGroupBox("Dataset")
        self.radio_buttons_group_box = QGroupBox("Choose algorithm")
        self.genetic_alg_group_box = QGroupBox("Genetic Algorithm")
        self.tab_widget_group_box = QTabWidget()
        self.console_group_box = QTabWidget()
        self.original_palette = QApplication.palette()
        self.console_group_box = QGroupBox("Output Console")

        self.create_radio_buttons_widget()
        self.create_dataset_group_box()
        self.create_genetic_alg_widget()

        GuiProjectDescription(self.tab_widget_group_box)

        self.create_mutation_group_box()
        self.progressBar = ProgressBar()

        self.console = QTextEdit()
        GuiConsole.createConsole(self, self.console, self.console_group_box)

        style_combo_box = QComboBox()
        style_combo_box.addItems(QStyleFactory.keys())
        style_combo_box.activated[str].connect(self.change_style)

        top_layout = QHBoxLayout()
        top_layout.addStretch(1)

        main_layout = QGridLayout()
        main_layout.addWidget(self.tab_widget_group_box, 0, 0, 1, 2)
        main_layout.addLayout(top_layout, 1, 0, 1, 2)

        main_layout.addWidget(self.dataset_group_box, 2, 0)
        main_layout.addWidget(self.mutation_group_box, 2, 1)
        main_layout.addWidget(self.radio_buttons_group_box, 3, 0)
        main_layout.addWidget(self.genetic_alg_group_box, 3, 1)
        main_layout.addWidget(self.progressBar.progress_bar, 4, 0, 1, 2)
        main_layout.addWidget(self.console_group_box, 5, 0, 1, 2)
        main_layout.addWidget(self.console_group_box, 0, 0, 1, 2)

        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)

        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)

        self.setLayout(main_layout)
        self.setWindowTitle(self.window_title + self.version)
        self.setWindowIcon(QIcon('gui/img/app_icon.png'))
        self.change_style(self.style)

    def change_style(self, style_name):
        QApplication.setStyle(QStyleFactory.create(style_name))
        self.change_palette()

    def change_palette(self):
        QApplication.setPalette(self.original_palette)

    def create_dataset_group_box(self):
        # generate_dataset_button = QPushButton("Generate a dataset")
        # generate_dataset_button.setDefault(True)

        load_graph_button = QPushButton("Load the graph")
        load_graph_button.setDefault(True)

        print_graph_button = QPushButton("Print the graph")
        print_graph_button.setDefault(True)

        layout = QVBoxLayout()
        # layout.addWidget(generate_dataset_button)
        layout.addWidget(load_graph_button)
        layout.addWidget(print_graph_button)

        load_graph_button.clicked.connect(self.load_graph_button_clicked)
        print_graph_button.clicked.connect(self.print_graph_button_clicked)

        layout.addStretch(1)
        self.dataset_group_box.setLayout(layout)

    def create_radio_buttons_widget(self):
        self.radio_button_bruteforce = QRadioButton("Brute force")
        self.radio_button_bruteforce.clicked.connect(self.radio_button_bruteforce_clicked)

        self.radio_button_genetic = QRadioButton("Genetic")
        self.radio_button_genetic.clicked.connect(self.radio_button_genetic_clicked)
        self.radio_button_bruteforce.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(self.radio_button_bruteforce)
        layout.addWidget(self.radio_button_genetic)
        layout.addStretch(1)
        self.radio_buttons_group_box.setLayout(layout)

    def radio_button_bruteforce_clicked(self):
        self.radio_button_bruteforce.setChecked(True)
        self.radio_button_genetic.setChecked(False)
        self.population_size_box.setEnabled(False)
        self.number_of_generations_box.setEnabled(False)

    def radio_button_genetic_clicked(self):
        self.radio_button_bruteforce.setChecked(False)
        self.radio_button_genetic.setChecked(True)
        self.population_size_box.setEnabled(True)
        self.number_of_generations_box.setEnabled(True)

    def create_genetic_alg_widget(self):

        run_alg_button = QPushButton("Run Algorithm")
        run_alg_button.setMinimumSize(200, 30)
        run_alg_button.setDefault(True)

        population_size_label = QLabel(self.genetic_alg_group_box)
        population_size_label.setText("Population size:")

        self.population_size_box = QSpinBox(self.genetic_alg_group_box)
        self.population_size_box.setMinimum(10)
        self.population_size_box.setMaximum(100000)
        self.population_size_box.setValue(100)
        self.population_size_box.setEnabled(False)

        number_of_generations_label = QLabel(self.genetic_alg_group_box)
        number_of_generations_label.setText("Number of generations:")

        self.number_of_generations_box = QSpinBox(self.genetic_alg_group_box)
        self.number_of_generations_box.setMinimum(10)
        self.number_of_generations_box.setMaximum(100000)
        self.number_of_generations_box.setValue(50)
        self.number_of_generations_box.setEnabled(False)

        layout = QGridLayout()
        layout.addWidget(population_size_label, 0, 0, 1, 2)
        layout.addWidget(self.population_size_box, 0, 1, 1, 2)

        layout.addWidget(number_of_generations_label, 1, 0, 1, 2)
        layout.addWidget(self.number_of_generations_box, 1, 1, 1, 2)

        layout.addWidget(run_alg_button, 2, 0)
        layout.setRowStretch(3, 1)

        run_alg_button.clicked.connect(self.run_alg_button_clicked)
        self.genetic_alg_group_box.setLayout(layout)

    def load_graph_button_clicked(self):

        try:
            self.filename, _ = QFileDialog.getOpenFileName(self, "Load graph", "./graphs", "Graph Files (*.graph)")
            print(self.filename)

            self.graph = Graph(self.filename)

            if self.filename == "":
                self.filename = self.default_graph

            QMessageBox.information(self, 'Message', "The graph has been loaded correctly")

        except FileNotFoundError:
            QMessageBox.exec(self)

    def print_graph_button_clicked(self):

        if self.graph is None:
            GuiShowErrorMsg.show_error_msg('Error', "Graph not found. Load the graph to display it properly.")
        else:
            self.console.clear()
            GuiConsole.append_test_to_console(self, self.console, self.graph)

    def run_alg_button_clicked(self):

        if self.graph is None:
            GuiShowErrorMsg.show_error_msg('Error', "Graph not found. Load the graph to display it properly.")
        else:
            if self.radio_button_genetic.isChecked():
                print("radio_button_genetic isChecked")
                self.run_genetic_algorithm()
            else:
                self.run_brute_force_algorithm()

    def run_genetic_algorithm(self):
        genetic_algorithm = GeneticAlgorithm(self.graph)
        try:
            population_size = int(self.population_size_box.value())
        except ValueError:
            population_size = 100
        try:
            number_of_generations = int(self.number_of_generations_box.value())
        except ValueError:
            number_of_generations = 50
        self.console.clear()
        self.console.append("run genetic algorithm ")
        genetic_algorithm.generate_population(population_size)
        genetic_algorithm.run_algorithm(number_of_generations, self.console)

    def run_brute_force_algorithm(self):
        self.console.clear()
        self.console.append("run brute force algorithm ")
        brute_force_algorithm = BruteForceAlgorithm(self.graph)
        brute_force_algorithm.run_algorithm(self.console)

    def create_mutation_group_box(self):

        mutation_rate_label = QLabel(self.mutation_group_box)
        mutation_rate_label.setText("Mutation rate:")

        self.mutation_rate_spin_box = QDoubleSpinBox(self.mutation_group_box)
        self.mutation_rate_spin_box.setMinimum(0)
        self.mutation_rate_spin_box.setMaximum(1)
        self.mutation_rate_spin_box.setValue(0.05)
        self.mutation_rate_spin_box.setEnabled(True)

        crossing_rate_label = QLabel(self.mutation_group_box)
        crossing_rate_label.setText("Crossing rate:")

        self.crossing_rate_spin_box = QDoubleSpinBox(self.mutation_group_box)
        self.crossing_rate_spin_box.setMinimum(0)
        self.crossing_rate_spin_box.setMaximum(1)
        self.crossing_rate_spin_box.setValue(0.85)
        self.crossing_rate_spin_box.setEnabled(True)

        layout = QGridLayout()
        layout.addWidget(self.mutation_rate_spin_box, 0, 0, 1, 2)
        layout.setRowStretch(4, 1)

        layout = QGridLayout()
        layout.addWidget(mutation_rate_label, 0, 0, 1, 2)
        layout.addWidget(self.mutation_rate_spin_box, 0, 1, 1, 2)

        layout.addWidget(crossing_rate_label, 1, 0, 1, 2)
        layout.addWidget(self.crossing_rate_spin_box, 1, 1, 1, 2)

        self.mutation_group_box.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
