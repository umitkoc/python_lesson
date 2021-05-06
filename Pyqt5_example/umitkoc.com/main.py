from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton
from sys import argv, exit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)
        self.web=QWebEngineView(self)
        self.web.load(QUrl("http://www.umitkoc.com/"))
        self.web.resize(1000,950)
        self.web.move(0,50)
        ###########
        self.back=QPushButton(self)
        self.back.move(10,5)
        self.back.resize(30,30)
        self.back.setText("<")
        self.back.clicked.connect(self.web.back)
        #########
        self.forward=QPushButton(self)
        self.forward.setText(">")
        self.forward.move(60,5)
        self.forward.resize(30, 30)
        self.forward.clicked.connect(self.web.forward)
        ###########
        self.url=QLineEdit(self)
        self.url.setPlaceholderText("http://")
        self.url.resize(600,30)
        self.url.move(100,5)
        ###########
        self.search=QPushButton(self)
        self.search.setText("search")
        self.search.resize(50, 30)
        self.search.move(720,5)
        self.search.clicked.connect(self.ok)
    def ok(self):
        self.web.load(QUrl(self.url.text()))



if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec())
