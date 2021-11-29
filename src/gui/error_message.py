from PyQt5.QtWidgets import QMessageBox


class GuiShowErrorMsg(object):

    @staticmethod
    def show_error_msg(text="Error", info_text="inf"):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(info_text)
        msg.setWindowTitle("Error")
        msg.exec_()
