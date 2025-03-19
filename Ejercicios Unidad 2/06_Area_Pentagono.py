import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class CalculadoraPentagono(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("06_Area_Pentagono.ui", self)  # Cargar la UI

        # Conectar botón a la función de cálculo
        self.btnCalcular.clicked.connect(self.calcular_area)

    def calcular_area(self):
        try:
            # Obtener valores ingresados y convertirlos a float
            lado = float(self.inputLado.text())
            apotema = float(self.inputApotema.text())

            # Calcular el área del pentágono
            area = (5 * lado * apotema) / 2

            # Mostrar el resultado
            self.labelResultado.setText(f"Área: {area:.2f} unidades²")
        except ValueError:
            self.labelResultado.setText("Ingrese valores numéricos válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraPentagono()
    ventana.show()
    sys.exit(app.exec())
