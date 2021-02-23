import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


    

def Window():
    app=QApplication(sys.argv)
    win=QMainWindow()
    def clicked():
        print(f"buttona tıklandı name: {text_email.text()}")
    win.setWindowTitle('New Project')
    win.setIconSize(QSize(30,30))
    win.setWindowIcon(QIcon('logo.png'))
    win.setToolTip("New Project")
    win.setFixedSize(500,800)
    lbl_email=QLabel(win)
    lbl_email.setText("e-mail: ")
    lbl_email.move(100,500)
    lbl_password=QLabel(win)
    lbl_password.setText("password: ")
    lbl_password.move(100,550)
    text_email=QLineEdit(win)
    text_email.move(175,500)
    text_password=QLineEdit(win)
    text_password.move(175,550)
    submit=QPushButton(win)
    submit.setText("sumbit")
    submit.move(150,600)
    submit.clicked.connect(clicked)


    
    win.show()
    sys.exit(app.exec_())

Window()