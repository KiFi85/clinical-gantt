from createGantt import create_gantt
from PyQt5.QtCore import QSize, QDate, Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QVBoxLayout, QPushButton, \
    QSizePolicy, QDateEdit, QFileDialog
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class PageGantt(QWidget):

    def __init__(self, *args, **kwargs):
        super(PageGantt, self).__init__(*args, **kwargs)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(141, 185, 202))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.layout = QGridLayout(self)
        layout_start = QVBoxLayout(self)
        layout_end = QVBoxLayout(self)

        # Date edits
        now = QDate.currentDate()
        start_date = now.addMonths(-1)
        end_date = now.addMonths(12)
        self.date_start = QDateEdit(date=start_date)
        self.date_start.setCalendarPopup(True)
        self.date_end = QDateEdit(date=end_date)
        self.date_end.setCalendarPopup(True)
        self.date_start.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        self.date_end.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)

        # Date pickers and labels
        label_start = QLabel(text="Select Start Date")
        label_end = QLabel(text="Select End Date")
        label_start.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        label_end.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        layout_start.addWidget(label_start)
        layout_start.addWidget(self.date_start)
        layout_end.addWidget(label_end)
        layout_end.addWidget(self.date_end)
        self.layout.addLayout(layout_start,1,0)
        self.layout.addLayout(layout_end,4,0)

        # Buttons Run and Save Figure
        self.btn_run = QPushButton(text="Plot")
        self.btn_run.clicked.connect(self.plot_gantt)
        self.btn_save = QPushButton(text="Save")
        self.btn_run.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        self.btn_save.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        self.btn_save.clicked.connect(self.save_plot)
        self.layout.addWidget(self.btn_run,21,3)
        self.layout.addWidget(self.btn_save,21,4)

        widget = QWidget()
        widget.setStyleSheet("QWidget{background-color: white}")
        self.layout.addWidget(widget,0,1,20,4)

    def plot_gantt(self):

        start_date = self.date_start.date().toString(Qt.ISODate)
        end_date = self.date_end.date().toString(Qt.ISODate)
        self.fig = create_gantt(start_date,end_date)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas,0,1,20,4)
        self.canvas.draw()

    def save_plot(self):

        file_choices = "PNG (*.png)|*.png"

        path, ext = QFileDialog.getSaveFileName(self,
                                                'Save file', '',
                                                file_choices)

        self.fig.savefig(path)
