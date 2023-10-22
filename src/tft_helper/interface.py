from PyQt6 import QtCore, QtWidgets, QtGui  
from PyQt6.QtCore import Qt

class TFTWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.set_widget_dimensions()
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )
        
        label = QtWidgets.QLabel("TESTING WIP", self)
        #label.move(15, 10)


    def set_widget_dimensions(self):
        app = QtWidgets.QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setFixedSize(geometry.width(), geometry.height())
