import sys
from interface import TFTWidget, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = TFTWidget()
    widget.show()

    sys.exit(app.exec())
