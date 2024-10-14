from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python HSL Player")
        self.setGeometery(100, 100, 800, 600)

        self.central_widget= QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.video_widget = QVideoWidget()
        self.layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_pause)
        self.layout.addWidget(self.play_button)

        self.open_button = QPushButton("Open File")
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)
        
        self.status_label = QLabel("No media loaded")
        self.layout.addWidget(self.status_label)

    
    def play_pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
            self.play_button.setText("Play")
        else:
            self.media_player.play()
            self.play_button.setText("Pause")