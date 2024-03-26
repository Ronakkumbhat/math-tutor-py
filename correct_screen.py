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
from ui_correct import Ui_Form

class correct_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        print("correct_screen")
        # Connect signals


