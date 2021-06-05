from sys import argv, exit
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle,
                             QVBoxLayout, QWidget)


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        self.show()

    def ui(self):
        self.setWindowTitle("Media Player")
        self.setStyleSheet("background-color:black;")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setGeometry(500, 200, 800, 600)
        self.video_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        video_widget = QVideoWidget()
        self.video_player.setVideoOutput(video_widget)
        # open file button
        btn_open_file = QPushButton("Open File")
        btn_open_file.clicked.connect(self.open_folder)
        btn_open_file.setStyleSheet("background-color:white;color:black;")
        # play file button
        self.btn_play_file = QPushButton("Play")
        self.btn_play_file.setIcon(
            self.style().standardIcon(QStyle.SP_MediaPlay))
        self.btn_play_file.setStyleSheet("background-color:white;color:black;")
        self.btn_play_file.setEnabled(False)
        self.btn_play_file.clicked.connect(self.play_video)
        # slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.sliderMoved.connect(self.slider_moved)
        # time label
        self.lbl_time = QLabel()
        self.lbl_time.setStyleSheet("color:white;")
        self.lbl_time.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # horizontal box layout
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(btn_open_file)
        hbox.addWidget(self.btn_play_file)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.lbl_time)
        # vertical box layout
        vbox = QVBoxLayout()
        vbox.addWidget(video_widget)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.video_player.positionChanged.connect(self.position_video)
        self.video_player.stateChanged.connect(self.state_video)
        self.video_player.durationChanged.connect(self.duration_video)

    def duration_video(self, value):
        self.slider.setRange(0, value)

    def state_video(self):
        if self.video_player.state() == QMediaPlayer.PlayingState:
            self.btn_play_file.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.btn_play_file.setIcon(
                self.style().standardIcon(QStyle.SP_MediaStop))

    def position_video(self, value):
        self.slider.setValue(value)
        value //= 1024
        self.lbl_time.setText(f"{value//60}:{value%60}")

    def slider_moved(self, value):
        self.video_player.setPosition(value)

    def open_folder(self):
        self.video_player.setMedia(
                QMediaContent(QUrl("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4")))
        self.btn_play_file.setEnabled(True)

    def play_video(self):
        if self.video_player.state() == QMediaPlayer.PlayingState:
            self.video_player.pause()
        else:
            self.video_player.play()


app = QApplication(argv)
main = Main()
exit(app.exec_())
