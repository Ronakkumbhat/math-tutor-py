# This Python file uses the following encoding: utf-8
import sys
import random
import threading
import time
import pygame
import re
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtTextToSpeech import QTextToSpeech
from math_screen import math_screen
from ui_welcome_screen import Ui_Form
# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
class BackgroundMusicThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True  # Set the thread as a daemon to automatically terminate when the main thread exits
        self.music_file = "sounds/backgroundmusic.ogg"  # Replace "background_music.mp3" with your actual music file

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.set_volume(0.5)  # Adjust the volume (0.0 to 1.0)
        pygame.mixer.music.play(loops=-1)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Connect signals
        self.ui.enter_box.installEventFilter(self)
        self.speech = QTextToSpeech()
        self.speech.say("press enter to continue")
        self.music_thread = BackgroundMusicThread()
        self.music_thread.start()
    def startMathScreen(self):
        self.math_screen_obj = math_screen()
        self.math_screen_obj.show()
        self.hide()
    def quitApplication(self):
        pygame.mixer.quit()  # Clean up pygame mixer
        app.quit()
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            keyEvent = QKeyEvent(event)
            if keyEvent.key() == Qt.Key_Enter or keyEvent.key() == Qt.Key_Return:
                self.startMathScreen()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
