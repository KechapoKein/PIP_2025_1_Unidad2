import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Para cargar el .ui


class Convertidor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("01_Grados_C_F.ui", self)  # Carga el archivo .ui

        # Conectar botón a la función de conversión
        self.btnConvertir.clicked.connect(self.convertir)

    def convertir(self):
        try:
            celsius = float(self.inputCelsius.text())  # Obtener valor de entrada
            fahrenheit = (celsius * 9 / 5) + 32  # Convertir a Fahrenheit
            self.labelResultado.setText(f"{fahrenheit:.2f} °F")  # Mostrar resultado
        except ValueError:
            self.labelResultado.setText("Ingrese un número válido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Convertidor()
    ventana.show()
    sys.exit(app.exec())
