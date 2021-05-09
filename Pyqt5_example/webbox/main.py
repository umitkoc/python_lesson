from sys import argv, exit

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu,
                             QMenuBar, QShortcut, QTabWidget)
from Pyqt5_example.webbox.tab import tab


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open("style.qss", "r").read())
        self.tab_menu()
        self.menu_bar()
        self.home_design()
        self.shortcut()
        
    def home_design(self):
        self.setWindowTitle("WEBBOX")
        self.resize(1920,1080)
        self.setWindowFlag(Qt.FramelessWindowHint)
    def tab_menu(self):
        self.tabmenu = QTabWidget(self)
        self.tabmenu.resize(1920, 1080)
        self.newpage()
    def menu_bar(self):
        self.menubar = QMenuBar(self)
        self.menubar.resize(500,30)
        self.addmenu("files")
        self.addmenu("views")
        self.addmenu("settings")
    def shortcut(self):
        short=QShortcut(QKeySequence("CTRL+N"),self)
        short.activated.connect(self.newpage)
    def newpage(self):
        pages=self.tabmenu.addTab(tab(),"google.com")
        self.tabmenu.setCurrentIndex(pages)
    def addmenu(self,value):
        self.menu=QMenu(self)
        self.menu.setTitle(value)
        self.menubar.addMenu(self.menu)
        self.addaction()
    def addaction(self):
        self.action=QAction(self)
        self.menu.addAction(self.action)
        if self.menu.title()=="files":
            self.action.setText("exit")
            self.action.triggered.connect(self.close)
        if self.menu.title()=="views":
            self.action.setText("views1")
    def close(self):
        exit()






        


if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec())
