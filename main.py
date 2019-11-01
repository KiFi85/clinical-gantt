import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from gantt_page import PageGantt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Gantt Creator")
        self.setGeometry(900,650,1400,1200) #x,y,w,h
        self.setMinimumHeight(1200)
        self.setMinimumWidth(1600)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setAutoFillBackground(True)
        palette = self.palette()
        self.back_colour = QColor(141*0.5, 185*0.5, 202*0.5)
        palette.setColor(QPalette.Window, self.back_colour)
        self.setPalette(palette)

        # Add page to central widget
        self.setCentralWidget(PageGantt())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
