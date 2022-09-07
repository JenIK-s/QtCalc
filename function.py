from main import *

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class number():
    def plus(self):
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.insert('+')
    def mns(self):
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.insert('-')
    def dl(self):
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.insert('/')
    def ymn(self):
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.insert('*')
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