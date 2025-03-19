import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class ConversorMetros(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("04_Metros_Kilometros.ui", self)  # Cargar la UI

        # Conectar botón a la función de conversión
        self.btnConvertir.clicked.connect(self.convertir_a_km)

    def convertir_a_km(self):
        try:
            # Obtener el valor ingresado y convertirlo a float
            metros = float(self.inputMetros.text())
            kilometros = metros / 1000  # Convertir a kilómetros

            # Mostrar el resultado
            self.labelResultado.setText(f"{kilometros:.3f} Kilómetros")
        except ValueError:
            self.labelResultado.setText("Ingrese un número válido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ConversorMetros()
    ventana.show()
    sys.exit(app.exec())
