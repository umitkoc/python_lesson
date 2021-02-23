from sys import exit,argv
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton

class Window(QMainWindow):
    def __init__(self):
      super(Window,self).__init__()
      self.setWindowTitle("Calculator")
      self.setFixedSize(500,800)
      self.design()
    def design(self):
        self.txt_one=QLineEdit(self)
        self.txt_one.move(200,200)
        #####
        self.txt_two=QLineEdit(self)
        self.txt_two.move(200,260)
        #####
        self.txt_result=QLineEdit(self)
        self.txt_result.move(200,140)
        self.txt_result.setEnabled(False)
        #####
        self.btn_plus=QPushButton(self)
        self.btn_plus.move(200,320)
        self.btn_plus.setText("+")
        #####
        self.btn_extraction=QPushButton(self)
        self.btn_extraction.move(200,360)
        self.btn_extraction.setText("-")
        #####
        self.btn_multiplication=QPushButton(self)
        self.btn_multiplication.move(200,400)
        self.btn_multiplication.setText("x")
        #####
        self.btn_division=QPushButton(self)
        self.btn_division.move(200,440)
        self.btn_division.setText("/")
        #####
        self.btn_plus.clicked.connect(self.plus)
        self.btn_extraction.clicked.connect(self.extraction)
        self.btn_multiplication.clicked.connect(self.multiplication)
        self.btn_division.clicked.connect(self.division)
    def plus(self):
        self.sum=(int(self.txt_one.text())+int(self.txt_two.text()))
        self.txt_result.setText(str(self.sum))
        self.txt_one.setText("")
        self.txt_two.setText("")
    def extraction(self):
        self.sum=(int(self.txt_one.text())-int(self.txt_two.text()))
        self.txt_result.setText(str(self.sum))
        self.txt_one.setText("")
        self.txt_two.setText("")
    def multiplication(self):
        self.sum=(int(self.txt_one.text())*int(self.txt_two.text()))
        self.txt_result.setText(str(self.sum))
        self.txt_one.setText("")
        self.txt_two.setText("")
    def division(self):
        self.sum=(int(self.txt_one.text())/int(self.txt_two.text()))
        self.txt_result.setText(str(self.sum))
        self.txt_one.setText("")
        self.txt_two.setText("")






if "__main__"==__name__:
    app=QApplication(argv)
    win=Window()
    win.show()
    exit(app.exec_())