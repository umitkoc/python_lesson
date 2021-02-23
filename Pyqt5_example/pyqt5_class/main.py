from sys import exit,argv
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit,QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
      super(Window,self).__init__()
      self.setWindowTitle('Class Window')
      self.setFixedSize(500,800)
      self.initUi()
    def initUi(self):
        self.lbl_name=QLabel(self)
        self.lbl_name.setText("name:")
        self.lbl_name.move(200,500)
        ####
        self.lbl_surname=QLabel(self)
        self.lbl_surname.setText("surname:")
        self.lbl_surname.move(200,550)
        ####
        self.txt_name=QLineEdit(self)
        self.txt_name.move(275,500)
        ####
        self.txt_surname=QLineEdit(self)
        self.txt_surname.move(275,550)
        ####
        self.submit=QPushButton(self)
        self.submit.setText("submit")
        self.submit.move(250,600)
        self.submit.clicked.connect(self.clicked)
    def clicked(self):
        print(f"name: {self.txt_name.text()}\nsurname:{self.txt_surname.text()}")




if __name__=="__main__":
    app=QApplication(argv)
    win=Window()
    win.show()
    exit(app.exec_())
    

