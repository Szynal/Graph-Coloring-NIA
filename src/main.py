#!/usr/bin/env python
import sys

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QMessageBox, QPushButton, QFileDialog)

from src.gui.description import GuiProjectDescription
from src.gui.error_message import GuiShowErrorMsg
from src.gui.console import GuiConsole

from graph import Graph
from genetic_algorithm import GeneticAlgorithm


class WidgetGallery(QDialog):
    version = "v1.0"
    window_title = "Graph-Coloring-NIA "
    style = "Fusion"

    filename = ""
    default_graph = "graphs/projekt0_n50_m854.graph"
    alg = ""
    graph = ""

    console = None

    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.dataset_group_box = QGroupBox("Dataset")
        self.radio_buttons_group_box = QGroupBox("Choose algorithm")
        self.buttons_group_box = QGroupBox("")
        self.tab_widget_group_box = QTabWidget()
        self.console_group_box = QTabWidget()
        self.original_palette = QApplication.palette()
        self.progress_bar = QProgressBar()
        self.console_group_box = QGroupBox("Output Console")

        self.create_radio_buttons_widget()
        self.create_dataset_group_box()
        self.create_genetic_alg_widget()
        self.create_description_widget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

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
        main_layout.addWidget(self.bottomRightGroupBox, 2, 1)
        main_layout.addWidget(self.radio_buttons_group_box, 3, 0)
        main_layout.addWidget(self.buttons_group_box, 3, 1)
        main_layout.addWidget(self.progress_bar, 4, 0, 1, 2)
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

    def init_progress_bar(self):
        progress_bar_cur_val = self.progress_bar.value()
        progress_bar_max_val = self.progress_bar.maximum()
        self.progress_bar.setValue(progress_bar_cur_val + (progress_bar_max_val - progress_bar_cur_val) // 100)

    def create_dataset_group_box(self):
        generate_dataset_button = QPushButton("Generate a dataset")
        generate_dataset_button.setDefault(True)

        load_graph_button = QPushButton("Load the graph")
        load_graph_button.setDefault(True)

        print_graph_button = QPushButton("Print the graph")
        print_graph_button.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(generate_dataset_button)
        layout.addWidget(load_graph_button)
        layout.addWidget(print_graph_button)

        load_graph_button.clicked.connect(self.load_graph_button_clicked)
        print_graph_button.clicked.connect(self.print_graph_button_clicked)

        layout.addStretch(1)
        self.dataset_group_box.setLayout(layout)

    def create_radio_buttons_widget(self):
        radio_button1 = QRadioButton("Radio button 1")
        radio_button2 = QRadioButton("Radio button 2")
        radio_button3 = QRadioButton("Radio button 3")
        radio_button1.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)
        layout.addWidget(radio_button3)
        layout.addStretch(1)
        self.radio_buttons_group_box.setLayout(layout)

    def create_genetic_alg_widget(self):

        run_genetic_alg_button = QPushButton("Run Genetic Algorithm")
        run_genetic_alg_button.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(run_genetic_alg_button)

        run_genetic_alg_button.clicked.connect(self.run_genetic_alg_button_clicked)

        layout.addStretch(1)
        self.buttons_group_box.setLayout(layout)

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
            GuiConsole.append_test_to_console(self, self.console, self.graph)

    def run_genetic_alg_button_clicked(self):

        if self.graph is None:
            GuiShowErrorMsg.show_error_msg('Error', "Graph not found. Load the graph to display it properly.")
        else:
            alg = GeneticAlgorithm(self.graph)
            try:
                population_size = int(input("Podaj rozmiar populacji (domyślnie=100): "))
            except ValueError:
                population_size = 100
            try:
                number_of_generations = int(input("Podaj liczbę pokoleń (domyślnie=50): "))
            except ValueError:
                number_of_generations = 50
            alg.generate_population(population_size)
            alg.run_algorithm(number_of_generations)

    def create_description_widget(self):
        self.tab_widget_group_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        tab2 = QWidget()
        text_edit = QTextEdit()
        text_edit.setPlainText(GuiProjectDescription.get_project_description())
        text_edit.setReadOnly(True)
        tab2box = QHBoxLayout()
        tab2box.setContentsMargins(5, 5, 5, 5)
        tab2box.addWidget(text_edit)
        tab2.setLayout(tab2box)
        self.tab_widget_group_box.addTab(tab2, "Project Description")

        authors_widget = QWidget()
        authors_label = QLabel()
        authors_label.setText(GuiProjectDescription.get_project_authors())
        authors_box = QHBoxLayout()
        authors_box.setContentsMargins(5, 5, 5, 5)
        authors_box.addWidget(authors_label)
        authors_widget.setLayout(authors_box)
        self.tab_widget_group_box.addTab(authors_widget, "Authors")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spin_box = QSpinBox(self.bottomRightGroupBox)
        spin_box.setValue(50)

        date_time_edit = QDateTimeEdit(self.bottomRightGroupBox)
        date_time_edit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scroll_bar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scroll_bar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spin_box, 1, 0, 1, 2)
        layout.addWidget(date_time_edit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scroll_bar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    def createProgressBar(self):
        self.progress_bar.setRange(0, 10000)
        self.progress_bar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.init_progress_bar)
        timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
