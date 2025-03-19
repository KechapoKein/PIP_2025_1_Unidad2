import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class TeoremaPitagoras(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("07_Teorema_Pitagoras.ui", self)  # Cargar la UI

        # Conectar botón a la función de cálculo
        self.btnCalcular.clicked.connect(self.calcular_hipotenusa)

    def calcular_hipotenusa(self):
        try:
            # Obtener valores ingresados y convertirlos a float
            a = float(self.inputCatetoA.text())
            b = float(self.inputCatetoB.text())

            # Calcular la hipotenusa
            c = math.sqrt(a ** 2 + b ** 2)

            # Mostrar el resultado
            self.labelResultado.setText(f"Hipotenusa: {c:.2f}")
        except ValueError:
            self.labelResultado.setText("Ingrese valores numéricos válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TeoremaPitagoras()
    ventana.show()
    sys.exit(app.exec())
