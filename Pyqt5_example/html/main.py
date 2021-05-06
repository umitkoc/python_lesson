from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from os import path
from sys import exit, argv

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle("umitkoc.com")
        self.web=QWebEngineView(self)
        self.web.load(QUrl.fromLocalFile(
            path.abspath("Pyqt5_example\html\index.html")))
        self.web.resize(500,500)


if __name__=="__main__":
    app=QApplication(argv)
    main=Main()
    main.show()
    exit(app.exec())
