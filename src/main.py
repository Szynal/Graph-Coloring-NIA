#!/usr/bin/env python
import sys

from PyQt5.QtCore import QDateTime, Qt, QTimer, QUrl, QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QMessageBox, QPushButton, QFileDialog)

from src.gui.description import GUIProjectDescription
from src.gui.error_message import GUIShowErrorMsg

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

    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.progressBar = QProgressBar()
        self.topLeftGroupBox = QGroupBox("Choose algorithm")
        self.topRightGroupBox = QGroupBox("")
        self.bottomLeftTabWidget = QTabWidget()
        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        self.create_radio_buttons_widget()
        self.create_buttons_widget()
        self.create_description_widget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        styleComboBox.activated[str].connect(self.change_style)

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle(self.window_title + self.version)
        self.setWindowIcon(QIcon('gui/img/app_icon.png'))
        self.change_style(self.style)

    def change_style(self, style_name):
        QApplication.setStyle(QStyleFactory.create(style_name))
        self.change_palette()

    def change_palette(self):
        QApplication.setPalette(self.originalPalette)

    def init_progress_bar(self):
        progress_bar_cur_val = self.progressBar.value()
        progress_bar_max_val = self.progressBar.maximum()
        self.progressBar.setValue(progress_bar_cur_val + (progress_bar_max_val - progress_bar_cur_val) // 100)

    def create_radio_buttons_widget(self):
        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def create_buttons_widget(self):
        generate_dataset_button = QPushButton("Generate a dataset")
        generate_dataset_button.setDefault(True)

        load_graph_button = QPushButton("Load the graph")
        load_graph_button.setDefault(True)

        print_graph_button = QPushButton("Print the graph")
        print_graph_button.setDefault(True)

        run_genetic_alg_button = QPushButton("Run Genetic Algorithm")
        run_genetic_alg_button.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(generate_dataset_button)
        layout.addWidget(load_graph_button)
        layout.addWidget(print_graph_button)
        layout.addWidget(run_genetic_alg_button)

        load_graph_button.clicked.connect(self.load_graph_button_clicked)
        print_graph_button.clicked.connect(self.print_graph_buton_clicked)
        run_genetic_alg_button.clicked.connect(self.run_genetic_alg_button_clicked)

        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

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

    def print_graph_buton_clicked(self):

        if self.graph is None:
            GUIShowErrorMsg.show_error_msg('Error', "Graph not found. Load the graph to display it properly.")
        else:
            print(self.graph)

    def run_genetic_alg_button_clicked(self):
        raise NotImplementedError

    def create_description_widget(self):
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                                               QSizePolicy.Ignored)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText(GUIProjectDescription.get_project_description())
        textEdit.setReadOnly(True)
        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab2, "Project Description")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    def createProgressBar(self):
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.init_progress_bar)
        timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
