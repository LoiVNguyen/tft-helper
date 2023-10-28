from PyQt6 import QtCore, QtWidgets, QtGui  
from PyQt6.QtCore import Qt
from utils.text_image_scraper import get_image, get_augment_round, get_augments, grab_augments_table, convert_augments_data, LOLCHESS


class TFTWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.set_label()
        self.set_widget_dimensions()
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )
        self.augments_data = convert_augments_data(grab_augments_table(LOLCHESS))

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.frame)
        timer.start()
        self.x = 0


    def set_widget_dimensions(self):
        app = QtWidgets.QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setFixedSize(geometry.width(), geometry.height())

    
    def set_label(self):
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.hlayout.setSpacing(260)
        self.hlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setStyleSheet("color: white; font: bold 14px") 
        self.label1.setGeometry(400, 100, 500, 200)
        self.hlayout.addWidget(self.label1) 

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setStyleSheet("color: white; font: bold 14px")
        self.label1.setGeometry(400, 100, 500, 200)
        self.hlayout.addWidget(self.label2)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setStyleSheet("color: white; font: bold 14px")
        self.label1.setGeometry(400, 100, 500, 200)
        self.hlayout.addWidget(self.label3)


    def frame(self):
        stats = get_augments(get_image())
        average_placements = [augment[1][0] for augment in stats]
        if len(average_placements) == 3:
            self.label1.setText(average_placements[0])
            self.label2.setText(average_placements[1])
            self.label3.setText(average_placements[2])
        else:
            self.label1.setText("")
            self.label2.setText("")
            self.label3.setText("")
        print(stats)
        print(self.x)
        self.x += 1
        # print(stats)
