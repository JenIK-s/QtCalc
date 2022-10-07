from main import *
from math import sqrt

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Number:
    def test(self, args):
        tex = self.ui.lineEdit_4.text()
        text = tex[len(tex) - 1]
        if '+' == text:
            self.ui.lineEdit_5.insert(None)
        elif '-' == text:
            self.ui.lineEdit_5.insert(None)
        elif '/' == text:
            self.ui.lineEdit_5.insert(None)
        elif '*' == text:
            self.ui.lineEdit_5.insert(None)
        elif '**' == text:
            self.ui.lineEdit_5.insert(None)
        elif '=' in self.ui.lineEdit_5.text():
            print('12')
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_5.insert(tex)
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.insert(args)
        else:
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.insert(args)

    def plus(self):
        Number.test(self, '+')

    def mns(self):
        Number.test(self, '-')

    def dl(self):
        Number.test(self, '/')

    def ymn(self):
        Number.test(self, '*')

    def quad(self):
        Number.test(self, '**')

    def C(self):
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        width = self.size().width()
        height = self.size().height()
        print(width)
        print(height)

    def dlt(self):
        tex = self.ui.lineEdit_4.text()
        text = tex[:-1]
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_4.insert(text)
        if '=' in self.ui.lineEdit_5.text():
            self.ui.lineEdit_5.clear()
        else:
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_5.insert(text)

    def enter(self):
        result = eval(self.ui.lineEdit_5.text())
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_4.insert(str(result))
        self.ui.lineEdit_5.insert('=')

    def sq(self):
        text = self.ui.lineEdit_5.text()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_4.insert(str(sqrt(int(text))))

    def numbers(self):
        self.ui.pushButton_30.clicked.connect(lambda: self.ui.lineEdit_4.insert('0'))
        self.ui.pushButton_34.clicked.connect(lambda: self.ui.lineEdit_4.insert('1'))
        self.ui.pushButton_33.clicked.connect(lambda: self.ui.lineEdit_4.insert('2'))
        self.ui.pushButton_28.clicked.connect(lambda: self.ui.lineEdit_4.insert('3'))
        self.ui.pushButton_48.clicked.connect(lambda: self.ui.lineEdit_4.insert('4'))
        self.ui.pushButton_49.clicked.connect(lambda: self.ui.lineEdit_4.insert('5'))
        self.ui.pushButton_50.clicked.connect(lambda: self.ui.lineEdit_4.insert('6'))
        self.ui.pushButton_44.clicked.connect(lambda: self.ui.lineEdit_4.insert('7'))
        self.ui.pushButton_45.clicked.connect(lambda: self.ui.lineEdit_4.insert('8'))
        self.ui.pushButton_46.clicked.connect(lambda: self.ui.lineEdit_4.insert('9'))
        self.ui.pushButton_31.clicked.connect(lambda: self.ui.lineEdit_4.insert('.'))
        self.ui.pushButton_30.clicked.connect(lambda: self.ui.lineEdit_5.insert('0'))
        self.ui.pushButton_34.clicked.connect(lambda: self.ui.lineEdit_5.insert('1'))
        self.ui.pushButton_33.clicked.connect(lambda: self.ui.lineEdit_5.insert('2'))
        self.ui.pushButton_28.clicked.connect(lambda: self.ui.lineEdit_5.insert('3'))
        self.ui.pushButton_48.clicked.connect(lambda: self.ui.lineEdit_5.insert('4'))
        self.ui.pushButton_49.clicked.connect(lambda: self.ui.lineEdit_5.insert('5'))
        self.ui.pushButton_50.clicked.connect(lambda: self.ui.lineEdit_5.insert('6'))
        self.ui.pushButton_44.clicked.connect(lambda: self.ui.lineEdit_5.insert('7'))
        self.ui.pushButton_45.clicked.connect(lambda: self.ui.lineEdit_5.insert('8'))
        self.ui.pushButton_46.clicked.connect(lambda: self.ui.lineEdit_5.insert('9'))
        self.ui.pushButton_31.clicked.connect(lambda: self.ui.lineEdit_5.insert('.'))


class Operatsion:
    def oper(self):
        self.ui.pushButton_29.clicked.connect(lambda: Number.plus(self))
        self.ui.pushButton_38.clicked.connect(lambda: Number.C(self))
        self.ui.pushButton_39.clicked.connect(lambda: Number.dlt(self))
        self.ui.pushButton_27.clicked.connect(lambda: Number.enter(self))
        self.ui.pushButton_35.clicked.connect(lambda: Number.mns(self))
        self.ui.pushButton_40.clicked.connect(lambda: Number.sq(self))
        self.ui.pushButton_47.clicked.connect(lambda: Number.ymn(self))
        self.ui.pushButton_43.clicked.connect(lambda: Number.dl(self))
        self.ui.pushButton_42.clicked.connect(lambda: Number.quad(self))
