import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class ConversorML(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("03_Mililitros_Litros.ui", self)  # Cargar la UI

        # Conectar botón a la función de conversión
        self.btnConvertir.clicked.connect(self.convertir_a_litros)

    def convertir_a_litros(self):
        try:
            # Obtener el valor ingresado y convertirlo a float
            mililitros = float(self.inputMililitros.text())
            litros = mililitros / 1000  # Convertir a litros

            # Mostrar el resultado
            self.labelResultado.setText(f"{litros:.3f} Litros")
        except ValueError:
            self.labelResultado.setText("Ingrese un número válido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ConversorML()
    ventana.show()
    sys.exit(app.exec())
