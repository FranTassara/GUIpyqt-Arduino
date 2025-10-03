import sys
import numpy as np
from scipy.ndimage import gaussian_filter

# ---------------------------
# Si quisieras usar PyQt5:
#rom PyQt5 import QtWidgets, uic
#from pyqtgraph import ImageView

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import pyqtgraph as pg

# class MyMainWindow(QtWidgets.QMainWindow): #pyqt
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ---------- PyQt5 ----------
        ## Cargar archivo .ui
        #uic.loadUi("C:/Users/ulabceriani/Desktop/plotImageGUI.ui", self)
        ## Conectar botones (usar los nombres del .ui)
        #self.pushButton_plot.clicked.connect(self.plot_image)
        #self.pushButton_filter.clicked.connect(self.apply_filter)
        # ----------------------------

        # ---------- PySide6 ----------
        loader = CustomUiLoader()
        ui_file = QFile(
            r"C:/Users/Tassara/Documents/Facultad/PSIB - Clase Arduino-pyqt5/b. pyqt5_pyside6/2.plotImageGUI/plotImageGUI.ui"
        )
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)   # la UI completa es self.ui
        ui_file.close()
        # Conectar señales usando self.ui
        self.ui.pushButton_plot.clicked.connect(self.plot_image)
        self.ui.pushButton_filter.clicked.connect(self.apply_filter)
        # ----------------------------

        # Inicializar imagen vacía
        self.image_data = None

    def plot_image(self):
        # Crear imagen aleatoria
        self.image_data = np.random.rand(512, 512)
        self.ui.widget.setImage(self.image_data)

    def apply_filter(self):
        if self.image_data is not None:
            filtered = gaussian_filter(self.image_data, sigma=2)
            self.ui.widget.setImage(filtered)
        else:
            print("Primero debes plotear una imagen.")

# ---------- Comentar la siguiente clase si se usa PyQt ---------
class CustomUiLoader(QUiLoader):
    def createWidget(self, class_name, parent=None, name=""):
        if class_name == "ImageView":
            widget = pg.ImageView(parent)
            widget.setObjectName(name)
            return widget
        return super().createWidget(class_name, parent, name)

if __name__ == "__main__":
    # ---------- PyQt5 ----------
    #app = QtWidgets.QApplication(sys.argv)
    #window = MyMainWindow()
    #window.show()
    #sys.exit(app.exec_())
    # ---------------------------

    # ---------- PySide6 ----------
    app = QApplication(sys.argv)
    window = MyMainWindow()
    # mostramos la UI cargada dentro de la clase
    window.ui.show()
    sys.exit(app.exec())
    # ---------------------------