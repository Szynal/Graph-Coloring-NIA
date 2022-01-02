from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QProgressBar


class ProgressBar(object):
    timer = None
    progress_bar = None

    def __init__(self):
        self.progress_bar = QProgressBar()
        self.createProgressBar()

    def createProgressBar(self):
        self.progress_bar.setRange(0, 10000)
        self.progress_bar.setValue(0)

    def init_progress_bar(self):
        progress_bar_cur_val = self.progress_bar.value()
        progress_bar_max_val = self.progress_bar.maximum()
        self.progress_bar.setValue(progress_bar_cur_val + (progress_bar_max_val - progress_bar_cur_val) // 100)

    def startProgressBar(self, time):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.init_progress_bar)
        self.timer.start(time)

