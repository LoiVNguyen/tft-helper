import sys
import random
from PyQt6 import QtCore, QtWidgets, QtGui


class TFTWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.set_widget_dimensions()
        self.setWindowFlags(
            QtCore.Qt.WindowType.WindowStaysOnTopHint | 
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground
        )



    def set_widget_dimensions(self):
        app = QtWidgets.QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setFixedSize(geometry.width(), geometry.height())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = TFTWidget()
    widget.show()

    sys.exit(app.exec())

