import sys
import random
from PyQt5 import uic, QtWidgets
import sisas_rc

qtCreatorFile = "ProyectoUnidad2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.imagenes = ["supergucci", "cangrejocai", "goob", "snake"]
        self.empezarbutton.clicked.connect(self.iniciar_juego)
        self.superguccibutton.clicked.connect(lambda: self.verificar_seleccion("supergucci"))
        self.cangrejocaibutton.clicked.connect(lambda: self.verificar_seleccion("cangrejocai"))
        self.goobbutton.clicked.connect(lambda: self.verificar_seleccion("goob"))
        self.snakebutton.clicked.connect(lambda: self.verificar_seleccion("snake"))
        self.cerrarbutton.clicked.connect(self.cerrar_aplicacion)
        self.imagen_actual = None
    def iniciar_juego(self):
        self.imagen_actual = random.choice(self.imagenes)
        self.escogeestelabel.setText(self.imagen_actual)
    def verificar_seleccion(self, imagen_seleccionada):
        if imagen_seleccionada == self.imagen_actual:
            QtWidgets.QMessageBox.information(self, "Correcto", "¡Correcto! Has seleccionado la imagen correcta.")
            self.iniciar_juego()
        else: 
            QtWidgets.QMessageBox.warning(self, "Incorrecto", "¡Incorrecto! Intenta de nuevo.")
    def cerrar_aplicacion(self):
        self.close()
        # Área de los Signals
        
    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())