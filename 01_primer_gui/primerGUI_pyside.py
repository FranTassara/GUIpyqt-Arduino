# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MiPrimerGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(489, 446)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_clickMe = QPushButton(self.centralwidget)
        self.pushButton_clickMe.setObjectName(u"pushButton_clickMe")
        font = QFont()
        font.setPointSize(12)
        self.pushButton_clickMe.setFont(font)
        self.pushButton_clickMe.setStyleSheet(u"background-color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.pushButton_clickMe)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout.addWidget(self.pushButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_terminal = QLabel(self.centralwidget)
        self.label_terminal.setObjectName(u"label_terminal")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_terminal.setFont(font1)
        self.label_terminal.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.label_terminal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_clickMe.setText(QCoreApplication.translate("MainWindow", u"Click Me", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.label_terminal.setText("")
    # retranslateUi

# Clase que hereda de QMainWindow y maneja la lógica
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar señales a slots
        self.ui.pushButton_clickMe.clicked.connect(self.say_hello)
        self.ui.pushButton_delete.clicked.connect(self.clear_label)

    def say_hello(self):
        self.ui.label_terminal.setText("Hola mundo")
        print("Hola mundo")

    def clear_label(self):
        self.ui.label_terminal.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())