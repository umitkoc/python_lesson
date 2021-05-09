from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QHBoxLayout, QWidget


class tab(QWidget):
    def __init__(self):
        super().__init__()
        self.web = QWebEngineView(self)
        self.web.load(QUrl("https://duckduckgo.com/"))
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.web)

