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
from ui_form import Ui_Widget
# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.speech = QTextToSpeech(self)
        self.generateQuestion()  # Generate the initial question
        # Connect signals
        # Initialize pygame for music playback
        pygame.mixer.init()
              # Connect signals and slots
        self.ui.operation.currentIndexChanged.connect(self.operationChanged)
        self.ui.Difficulty_levels.currentIndexChanged.connect(self.generateQuestion)
        self.ui.user_ans.textChanged.connect(self.validateUserInput)
        self.ui.user_ans.installEventFilter(self)
        self.ui.user_ans.setFocus()
    def play_correct_music(self):
        # Load and play the correct answer music file
        pygame.mixer.music.load("sounds/excellent-1.ogg")
        pygame.mixer.music.play()

    def validateUserInput(self, text):
        # Regular expression pattern to match numeric input
        regex = r"\d+(\.\d+)?"
        match = re.match(regex, text)
        if not match:
            self.ui.user_ans.clear()

    def clearUserAnswer(self):
        self.ui.user_ans.clear()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            keyEvent = QKeyEvent(event)
            if keyEvent.key() == Qt.Key_Enter or keyEvent.key() == Qt.Key_Return:
                self.checkAnswer()
            elif keyEvent.key() == Qt.Key_Semicolon:
                self.speech.setRate(self.speech.rate() - 0.2)
            elif keyEvent.key() == Qt.Key_Apostrophe:
                self.speech.setRate(self.speech.rate() + 0.2)
            elif keyEvent.key() == Qt.Key_Shift:
                self.verbosesay() # Shift key
            elif keyEvent.key() == Qt.Key_Space:
                self.speech.say(self.question)
            elif keyEvent.key() == Qt.Key_A:  # Addition
                self.ui.operation.setCurrentIndex(0)
            elif keyEvent.key() == Qt.Key_S:  # Subtraction
                self.ui.operation.setCurrentIndex(1)
            elif keyEvent.key() == Qt.Key_D:  # Division
                self.ui.operation.setCurrentIndex(2)
            elif keyEvent.key() == Qt.Key_M:  # Multiplication
                self.ui.operation.setCurrentIndex(3)

        return super().eventFilter(obj, event)

    def spellOutNumber(self, number):
        digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        spelledNumber = ""
        # Convert each digit to its spelled-out form
        numStr = str(number)
        for digit in numStr:
            if digit.isdigit():
                spelledNumber += digits[int(digit)] + " "
        return spelledNumber.strip()  # Remove trailing space

    def verbosesay(self):
        n1_v = self.spellOutNumber(self._n1)
        n2_v = self.spellOutNumber(self._n2)
        v_ques = f"What is {n1_v} {self.operation} {n2_v}?"
        self.speech.say(v_ques)

    def generateQuestion(self):
        difficulty_index = self.ui.Difficulty_levels.currentIndex()
        if difficulty_index == 0:
            self._n1 = random.randint(0, 4)
            self._n2 = random.randint(0, 4)
        elif difficulty_index == 1:
            self._n1 = random.randint(0, 49)
            self._n2 = random.randint(0, 49)
        elif difficulty_index == 2:
            self._n1 = random.randint(0, 3999)
            self._n2 = random.randint(0, 3999)
        elif difficulty_index == 3:
            self._n1 = random.randint(0, 49999)
            self._n2 = random.randint(0, 49999)
        else:
            self._n1 = random.randint(0, 499999)
            self._n2 = random.randint(0, 499999)

        if self._n2 > self._n1:
            self._n1, self._n2 = self._n2, self._n1

        if self._n2 == 0:
            self._n2 = 1

        self.ui.n1.display(self._n1)
        self.ui.n2.display(self._n2)

        if self.ui.operation.currentIndex() == 0:
            self.tans = self._n1 + self._n2
        elif self.ui.operation.currentIndex() == 1:
            self.tans = self._n1 - self._n2
        elif self.ui.operation.currentIndex() == 2:
            self.tans = self._n1 / self._n2
        else:
            self.tans = self._n1 * self._n2

        self.operation = self.ui.operation.currentText()
        self.question = f"What is {self._n1} {self.operation} {self._n2}?"
        self.speech.say(self.question)
        self.ui.user_ans.setFocus()
        self.clearUserAnswer()
    def operationChanged(self):
        if self.ui.operation.currentIndex() == 0:
            self.ui.op_label.setText("+")
        elif self.ui.operation.currentIndex() == 1:
            self.ui.op_label.setText("-")
        elif self.ui.operation.currentIndex() == 2:
            self.ui.op_label.setText("/")
        else:
            self.ui.op_label.setText("*")

        self.generateQuestion()

    def checkAnswer(self):
        userans = float(self.ui.user_ans.text())
        userans = round(userans, 1)  # Truncate to 1 decimal place
        self.tans = round(self.tans, 1)  # Truncate to 1 decimal place

        if userans == self.tans:
            self.ui.result.setText("Correct")

            thread =threading.Thread(target=self.play_correct_music)
            thread.start()
            # Wait for the music to finish before generating the next question
            time.sleep(4)
            #self.speech.say("Correct")
            self.generateQuestion()
        else:
            self.ui.result.setText("Wrong")
            self.speech.say("Wrong")
            self.ui.user_ans.clear()
            self.speech.say(self.question)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
