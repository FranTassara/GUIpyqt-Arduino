# ---------------------------
# Si quisieras usar PyQt5:
# from PyQt5 import QtWidgets, uic
# ---------------------------

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ---------- PyQt5 ----------
        # uic.loadUi(
        #     r"C:/Users/Tassara/Documents/Facultad/PSIB - Clase Arduino-pyqt5/b. pyqt5/1.MiPrimerGUI/MiPrimerGUI.ui",
        #     self
        # )
        # self.pushButton_clickMe.clicked.connect(self.say_hello)
        # self.pushButton_delete.clicked.connect(self.clear_label)
        # ----------------------------

        # ---------- PySide6 ----------
        loader = QUiLoader()
        ui_file = QFile(
            r"C:/Users/Tassara/Documents/Facultad/PSIB - Clase Arduino-pyqt5/b. pyqt5/1.MiPrimerGUI/MiPrimerGUI.ui"
        )
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)   # la UI completa es self.ui
        ui_file.close()

        # Conectar señales usando self.ui
        self.ui.pushButton_clickMe.clicked.connect(self.say_hello)
        self.ui.pushButton_delete.clicked.connect(self.clear_label)
        # ----------------------------

    def say_hello(self):
        # self.label_terminal.setText("Hola mundo")   # PyQt5
        self.ui.label_terminal.setText("Hola mundo")  # PySide6

    def clear_label(self):
        # self.label_terminal.setText("")             # PyQt5
        self.ui.label_terminal.setText("")            # PySide6


if __name__ == "__main__":
    # ---------- PyQt5 ----------
    # app = QtWidgets.QApplication(sys.argv)
    # window = MyMainWindow()
    # window.show()
    # sys.exit(app.exec_())
    # ---------------------------

    # ---------- PySide6 ----------
    app = QApplication(sys.argv)
    window = MyMainWindow()
    # mostramos la UI cargada dentro de la clase
    window.ui.show()
    sys.exit(app.exec())
    # ---------------------------