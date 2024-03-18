# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLCDNumber, QLabel,
    QLineEdit, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.centralwidget = QWidget(Widget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.n1 = QLCDNumber(self.centralwidget)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(160, 150, 131, 41))
        self.n2 = QLCDNumber(self.centralwidget)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(400, 150, 141, 41))
        self.user_ans = QLineEdit(self.centralwidget)
        self.user_ans.setObjectName(u"user_ans")
        self.user_ans.setGeometry(QRect(570, 150, 141, 41))
        font = QFont()
        font.setPointSize(20)
        self.user_ans.setFont(font)
        self.operation = QComboBox(self.centralwidget)
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.setObjectName(u"operation")
        self.operation.setGeometry(QRect(340, 40, 281, 51))
        self.operation.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 50, 81, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(360, 240, 121, 51))
        self.result.setFont(font)
        self.Languages = QComboBox(self.centralwidget)
        self.Languages.addItem("")
        self.Languages.setObjectName(u"Languages")
        self.Languages.setGeometry(QRect(650, 430, 121, 41))
        self.Lang_label = QLabel(self.centralwidget)
        self.Lang_label.setObjectName(u"Lang_label")
        self.Lang_label.setGeometry(QRect(570, 430, 71, 41))
        self.op_label = QLabel(self.centralwidget)
        self.op_label.setObjectName(u"op_label")
        self.op_label.setGeometry(QRect(330, 140, 111, 51))
        font2 = QFont()
        font2.setPointSize(28)
        self.op_label.setFont(font2)
        self.result_2 = QLabel(self.centralwidget)
        self.result_2.setObjectName(u"result_2")
        self.result_2.setGeometry(QRect(0, 450, 531, 101))
        font3 = QFont()
        font3.setPointSize(8)
        self.result_2.setFont(font3)
        self.Difficulty_levels = QComboBox(self.centralwidget)
        self.Difficulty_levels.addItem("")
        self.Difficulty_levels.addItem("")
        self.Difficulty_levels.addItem("")
        self.Difficulty_levels.addItem("")
        self.Difficulty_levels.addItem("")
        self.Difficulty_levels.setObjectName(u"Difficulty_levels")
        self.Difficulty_levels.setGeometry(QRect(650, 480, 121, 41))
        self.difficulty_label = QLabel(self.centralwidget)
        self.difficulty_label.setObjectName(u"difficulty_label")
        self.difficulty_label.setGeometry(QRect(570, 480, 61, 41))
        self.menubar = QMenuBar(Widget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.statusbar = QStatusBar(Widget)
        self.statusbar.setObjectName(u"statusbar")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"MainWindow", None))
        self.operation.setItemText(0, QCoreApplication.translate("Widget", u"Addition", None))
        self.operation.setItemText(1, QCoreApplication.translate("Widget", u"Subraction", None))
        self.operation.setItemText(2, QCoreApplication.translate("Widget", u"Division", None))
        self.operation.setItemText(3, QCoreApplication.translate("Widget", u"Multiplication", None))

        self.label.setText(QCoreApplication.translate("Widget", u"Operation", None))
        self.result.setText(QCoreApplication.translate("Widget", u"Result", None))
        self.Languages.setItemText(0, QCoreApplication.translate("Widget", u"English", None))

        self.Lang_label.setText(QCoreApplication.translate("Widget", u"Language", None))
        self.op_label.setText(QCoreApplication.translate("Widget", u"+", None))
        self.result_2.setText(QCoreApplication.translate("Widget", u"Note: Adjust the speech rate by pressing the apostrophe or semicolon key,which\n"
" are located to the left of the Enter key. Use the Space key to replay the question,\n"
" and employ the Shift key to hear the question in verbose mode\n"
" use A,S,M,D keys to chnage the operation mode ", None))
        self.Difficulty_levels.setItemText(0, QCoreApplication.translate("Widget", u"Simple", None))
        self.Difficulty_levels.setItemText(1, QCoreApplication.translate("Widget", u"Easy", None))
        self.Difficulty_levels.setItemText(2, QCoreApplication.translate("Widget", u"Medium", None))
        self.Difficulty_levels.setItemText(3, QCoreApplication.translate("Widget", u"Hard", None))
        self.Difficulty_levels.setItemText(4, QCoreApplication.translate("Widget", u"Challenging", None))

        self.difficulty_label.setText(QCoreApplication.translate("Widget", u"Difficulty", None))
    # retranslateUi

