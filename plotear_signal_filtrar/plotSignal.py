# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotSignalGUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(483, 429)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_load = QPushButton(self.centralwidget)
        self.pushButton_load.setObjectName(u"pushButton_load")

        self.horizontalLayout_2.addWidget(self.pushButton_load)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_freq = QComboBox(self.groupBox)
        self.comboBox_freq.addItem("")
        self.comboBox_freq.addItem("")
        self.comboBox_freq.setObjectName(u"comboBox_freq")

        self.horizontalLayout.addWidget(self.comboBox_freq)

        self.pushButton_filter = QPushButton(self.groupBox)
        self.pushButton_filter.setObjectName(u"pushButton_filter")

        self.horizontalLayout.addWidget(self.pushButton_filter)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_2.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget_plotter = PlotWidget(self.centralwidget)
        self.widget_plotter.setObjectName(u"widget_plotter")
        self.widget_plotter.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.widget_plotter)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.comboBox_freq.setItemText(0, QCoreApplication.translate("MainWindow", u"50 Hz", None))
        self.comboBox_freq.setItemText(1, QCoreApplication.translate("MainWindow", u"60 Hz", None))

        self.pushButton_filter.setText(QCoreApplication.translate("MainWindow", u"Notch", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi


# ======================================================================
from PySide6.QtWidgets import (QFileDialog, QMessageBox)
import numpy as np
from scipy.signal import iirnotch, filtfilt
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configuración inicial del plot
        self.widget_plotter.showGrid(x=True, y=True, alpha=0.3)
        self.widget_plotter.setLabel('bottom', 'Time', 's')
        self.widget_plotter.setLabel('left', 'Amplitude', 'mV')
        self.curve = self.widget_plotter.plot(pen='g')

        # Variables para la señal
        self.signal = None
        self.fs = 1000  # frecuencia de muestreo por defecto

        # Conectar botones
        self.pushButton_load.clicked.connect(self.load_signal)
        self.pushButton_clear.clicked.connect(self.clear_plot)
        self.pushButton_filter.clicked.connect(self.apply_notch_filter)

    # ---------------------------------------------------------------
    def load_signal(self):
        """Cargar señal desde un archivo .txt o .csv"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Load ECG signal", "", "Data Files (*.txt *.csv)")
        if not file_path:
            return

        try:
            # Cargar el archivo (una sola columna o dos: tiempo, señal)
            #data = np.loadtxt(file_path, delimiter=',')
            data = np.loadtxt(file_path, delimiter=',', skiprows=1)
            if data.ndim == 1:
                self.signal = data
                t = np.arange(len(self.signal)) / self.fs
            else:
                t, self.signal = data[:, 0], data[:, 1]

            self.widget_plotter.clear()
            self.curve = self.widget_plotter.plot(t, self.signal, pen='g')
            self.statusbar.showMessage(f"Loaded: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file:\n{e}")

    # ---------------------------------------------------------------
    def clear_plot(self):
        """Limpiar el plot"""
        self.widget_plotter.clear()
        self.signal = None
        self.statusbar.showMessage("Plot cleared")

    # ---------------------------------------------------------------
    def apply_notch_filter(self):
        """Aplicar filtro notch 50 o 60 Hz"""
        if self.signal is None:
            QMessageBox.warning(self, "Warning", "Please load a signal first.")
            return

        freq_text = self.comboBox_freq.currentText()
        f0 = 50 if "50" in freq_text else 60
        Q = 30.0  # factor de calidad

        b, a = iirnotch(f0, Q, self.fs)
        filtered = filtfilt(b, a, self.signal)

        t = np.arange(len(filtered)) / self.fs
        self.widget_plotter.clear()
        self.curve = self.widget_plotter.plot(t, filtered, pen='y')
        self.statusbar.showMessage(f"Applied {f0} Hz notch filter")


# ======================================================================
#                            ---- Main ----
# ======================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())