from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout


class GuiConsole(object):
    console_text_color = QColor(1, 1, 1)
    background_color = "background-color: rgb(255, 255, 255);"

    @staticmethod
    def createConsole(parent, console, console_group_box):
        console_widget = QWidget()
        # console_widget.setStyleSheet(GuiConsole.background_color)

        console.setReadOnly(True)
        # console.setStyleSheet(GuiConsole.background_color)
        console.setTextColor(GuiConsole.console_text_color)

        console_box = QHBoxLayout()
        console_box.setContentsMargins(5, 5, 5, 5)
        console_box.addWidget(parent.console)

        console_widget.setLayout(console_box)

        layout = QVBoxLayout()
        layout.addWidget(console_widget)
        layout.addStretch(1)

        console_group_box.setLayout(layout)

    @staticmethod
    def append_test_to_console(self, console, text):
        console.append(str(text))
