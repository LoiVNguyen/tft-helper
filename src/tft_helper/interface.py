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


    def set_widget_dimensions(self):
        app = QtWidgets.QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setFixedSize(geometry.width(), geometry.height())

    
    def set_label(self):
        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.vlayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet("color: white")
        self.vlayout.addWidget(self.label)


    def frame(self):
        stats = get_augments(get_image())
        self.label.setText(str(stats))

