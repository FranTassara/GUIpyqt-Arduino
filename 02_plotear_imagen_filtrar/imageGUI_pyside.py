# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotImageGUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import ImageView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(569, 469)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_plot = QPushButton(self.centralwidget)
        self.pushButton_plot.setObjectName(u"pushButton_plot")

        self.horizontalLayout.addWidget(self.pushButton_plot)

        self.pushButton_filter = QPushButton(self.centralwidget)
        self.pushButton_filter.setObjectName(u"pushButton_filter")

        self.horizontalLayout.addWidget(self.pushButton_filter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget = ImageView(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 569, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
    # retranslateUi


import sys
import numpy as np
from scipy.ndimage import gaussian_filter
# Clase que hereda de QMainWindow y maneja la lógica
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # conectar botones
        self.pushButton_plot.clicked.connect(self.plot_image)
        self.pushButton_filter.clicked.connect(self.apply_filter)

        # inicializar datos de imagen
        self.image_data = None

    def plot_image(self):
        # generar datos random
        self.image_data = np.random.rand(512, 512)
        self.widget.setImage(self.image_data)  # 'widget' es el ImageView del .ui

    def apply_filter(self):
        if self.image_data is not None:
            filtered = gaussian_filter(self.image_data, sigma=2)
            self.widget.setImage(filtered)
        else:
            print("Primero debes plotear una imagen.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())