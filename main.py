import sys
import platform

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from all_modules import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        self.show()

        # ----------------------------NUMBERS----------------------------
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


        # ---------------------------------------------------------------

        # ----------------------------OPERATSION----------------------------


        self.ui.pushButton_29.clicked.connect(lambda : number.plus(self))
        self.ui.pushButton_38.clicked.connect(lambda : number.C(self))
        self.ui.pushButton_39.clicked.connect(lambda : number.dlt(self))
        self.ui.pushButton_27.clicked.connect(lambda: number.enter(self))
        self.ui.pushButton_35.clicked.connect(lambda: number.mns(self))
        self.ui.pushButton_47.clicked.connect(lambda: number.ymn(self))
        self.ui.pushButton_43.clicked.connect(lambda: number.dl(self))


        # ------------------------------------------------------------------

        # ----------------------------FONTS----------------------------



        # -------------------------------------------------------------

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        if 839 >= width >= 490 or 839 >= height >= 570:
            self.ui.pushButton_30.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_34.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_33.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_28.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_48.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_49.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_50.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_44.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_45.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_46.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_36.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_37.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_38.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_39.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_40.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_41.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_42.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_43.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_47.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_35.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_29.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_27.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_31.setFont(QFont('Segoe UI', 19))
            self.ui.pushButton_32.setFont(QFont('Segoe UI', 19))
            self.ui.lineEdit_4.setFont(QFont('Segoe UI', 24))
            self.ui.lineEdit_5.setFont(QFont('Segoe UI', 24))

        elif width >= 840 and height >= 840:
            self.ui.pushButton_30.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_34.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_33.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_28.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_48.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_49.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_50.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_44.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_45.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_46.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_36.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_37.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_38.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_39.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_40.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_41.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_42.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_43.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_47.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_35.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_29.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_27.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_31.setFont(QFont('Segoe UI', 24))
            self.ui.pushButton_32.setFont(QFont('Segoe UI', 24))
            self.ui.lineEdit_4.setFont(QFont('Segoe UI', 30))
            self.ui.lineEdit_5.setFont(QFont('Segoe UI', 30))
        else:
            self.ui.pushButton_30.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_34.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_33.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_28.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_48.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_49.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_50.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_44.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_45.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_46.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_36.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_37.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_38.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_39.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_40.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_41.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_42.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_43.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_47.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_35.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_29.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_27.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_31.setFont(QFont('Segoe UI', 16))
            self.ui.pushButton_32.setFont(QFont('Segoe UI', 16))
            self.ui.lineEdit_4.setFont(QFont(QFont('Segoe UI', 33 , QtGui.QFont.Bold)))
            self.ui.lineEdit_5.setFont(QFont(QFont('Segoe UI', 20 , QtGui.QFont.Bold)))

    def mousePressEvent(self, event):
        # Если нажата левая кнопка мыши
        if event.button() == QtCore.Qt.LeftButton:
            # получаем координаты окна относительно экрана
            x_main = self.geometry().x()
            y_main = self.geometry().y()
            # получаем координаты курсора относительно окна нашей программы
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            # проверяем условием позицию курсора на нужной области программы(у нас это верхний бар)
            # если всё ок - перемещаем
            # иначе игнорируем
            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.ui.lineEdit_4.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
