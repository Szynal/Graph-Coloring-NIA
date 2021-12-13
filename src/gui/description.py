from PyQt5.QtWidgets import QSizePolicy, QWidget, QTextEdit, QHBoxLayout, QLabel


class GuiProjectDescription(object):
    tab2 = None
    text_edit = None
    tab2box = None
    authors_widget = None
    authors_label = None
    authors_box = None

    project_description = "The aim of the project is to implement an" \
                          "optimization algorithm inspired by nature. \n\n" \
                          "The chosen optimization problem is the coloring of" \
                          "the graph. As part of the project, a simulator" \
                          " should also be prepared for a given optimization" \
                          " problem, in which it is possible to test the " \
                          "implemented genetic algorithm.\n\n"

    authors = "Paweł Szynal\n" \
              "Nr albumu: 226026\n" \
              "\nKamil Zdeb\n" \
              "Nr albumu: 235871\n"

    @staticmethod
    def get_project_description(project_description=project_description):
        return project_description

    @staticmethod
    def get_project_authors(authors=authors):
        return authors

    def __init__(self, tab_widget_group_box):
        self.create_description_widget(tab_widget_group_box)

    def create_description_widget(self, tab_widget_group_box):
        tab_widget_group_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        self.tab2 = QWidget()
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(GuiProjectDescription.get_project_description())
        self.text_edit.setReadOnly(True)
        self.tab2box = QHBoxLayout()
        self.tab2box.setContentsMargins(5, 5, 5, 5)
        self.tab2box.addWidget(self.text_edit)
        self.tab2.setLayout(self.tab2box)
        tab_widget_group_box.addTab(self.tab2, "Project Description")

        self.authors_widget = QWidget()
        self.authors_label = QLabel()
        self.authors_label.setText(GuiProjectDescription.get_project_authors())
        self.authors_box = QHBoxLayout()
        self.authors_box.setContentsMargins(5, 5, 5, 5)
        self.authors_box.addWidget(self.authors_label)
        self.authors_widget.setLayout(self.authors_box)
        tab_widget_group_box.addTab(self.authors_widget, "Authors")
