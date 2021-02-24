from  pytube import YouTube
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton,QProgressBar,QComboBox,QMessageBox
from sys import argv,exit
from os import getcwd,system


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Youtube Downloader')
        self.setFixedSize(500,200)
        self.design()
    def design(self):
        self.lbl_url=QLabel(self)
        self.lbl_url.setText('URL:')
        self.lbl_url.move(10,20)
        ##
        self.txt_url=QLineEdit(self)
        self.txt_url.move(40,25)
        self.txt_url.resize(450,20)
        ##
        self.lbl_format=QLabel(self)
        self.lbl_format.setText('FORMAT:')
        self.lbl_format.move(10,60)
        ##
        self.layout=QComboBox(self)
        self.layout.move(60,65)
        self.layout.resize(60,20)
        self.layout.addItem('mp4')
        self.layout.addItem('mp3')
        ###
        self.download_button=QPushButton(self)
        self.download_button.setText('Download')
        self.download_button.move(380,150)
        ###
        self.open_file=QPushButton(self)
        self.open_file.move(10,150)
        self.open_file.setText('Open')
        self.open_file.setEnabled(False)
        ###
        self.progress=QProgressBar(self)
        self.progress.move(100,100)
        self.progress.resize(350,20)
        ###
        self.message=QMessageBox(self)
        self.download_button.clicked.connect(self.download)
        self.open_file.clicked.connect(self.openfile)
    def download(self):
        if self.txt_url.text().strip()!='':
            self.setVisible(False)
            self.txt_url.setEnabled(False)
            self.layout.setEnabled(False)
            self.path=getcwd()
            self.youtube=YouTube(self.txt_url.text())
            if self.layout.currentText()=='mp4':
                self.video=self.youtube.streams.get_lowest_resolution()
                self.video.download(self.path)
            else:
                self.music=self.youtube.streams.get_audio_only()
                self.music.download(self.path)
            self.startprogress()
            self.txt_url.setText('')
        else:
            self.message.setText('please do not leave url blank')
            self.message.show()
        
    def openfile(self):
        system(f'start {self.path}')
        self.open_file.setEnabled(False)

    def startprogress(self):
        for i in range(101):
            self.progress.setValue(i)
        self.open_file.setEnabled(True)
        self.setVisible(True)
        self.txt_url.setEnabled(True)
        self.layout.setEnabled(True)

if __name__=='__main__':
    app=QApplication(argv)
    win=Window()
    win.show()
    exit(app.exec_())



