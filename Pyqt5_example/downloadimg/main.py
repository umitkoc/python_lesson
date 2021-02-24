from sys import exit,argv
from os import getcwd,system
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton,QMessageBox
from urllib.request import urlretrieve
class Window(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle('Download İmage')
      self.setFixedSize(500,200)
      self.design()
    def design(self):
        ###
        self.lbl_url=QLabel(self)
        self.lbl_url.setText('Url: ')
        self.lbl_url.move(20,5)
        ###
        self.lbl_name=QLabel(self)
        self.lbl_name.setText('file name')
        self.lbl_name.move(20,30)
        ###
        self.txt_url=QLineEdit(self)
        self.txt_url.move(50,10)
        self.txt_url.resize(400,20)
        ### 
        self.txt_name=QLineEdit(self)
        self.txt_name.move(80,35)
        self.txt_name.resize(80,20)
        ### download button
        self.btn_download=QPushButton(self)
        self.btn_download.move(395,150)
        self.btn_download.setText('download')
        #### open files
        self.btn_open=QPushButton(self)
        self.btn_open.move(5,150)
        self.btn_open.setText('Open file')
        self.btn_open.setEnabled(False)
        ###message box
        self.messsage=QMessageBox(self)
        ###
        self.btn_download.clicked.connect(self.download)
        self.btn_open.clicked.connect(self.openfile)
    def download(self):
        if self.txt_name.text()=='' or self.txt_url.text()=='':
            self.messsage.setText('please do not leave blank ☻ ')
            self.messsage.show()
        else:
            self.path=getcwd()+'/'+self.txt_name.text()+'.png'
            try:
                urlretrieve(self.txt_url.text(),self.path)
                self.btn_open.setEnabled(True)
            except :
                self.messsage.setText('error')
                self.messsage.show()
        self.txt_name.setText('')
        self.txt_url.setText('')
    def openfile(self):
        system(f'start {self.path}')
        self.btn_open.setEnabled(False)



if __name__=='__main__':
    app=QApplication(argv)
    win=Window()
    win.show()
    exit(app.exec_())








