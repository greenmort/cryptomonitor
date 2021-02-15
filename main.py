from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from  PyQt5 import QtCore
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Cryptoconverter"
        self.top = 200
        self.left = 600
        self.width = 300
        self.height = 500
        self.UiComponents()
        self.init_window()

    # def me_clicked(self):
        

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("cryptocurrency.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def UiComponents(self):
        button = QPushButton("calculate", self)
        button.setGeometry(QRect(100,  300, 110, 50))
        button.setIcon(QtGui.QIcon("bitcoin.png"))
        button.setIconSize(QtCore.QSize(30, 30))


# if __name__ == "main":
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
