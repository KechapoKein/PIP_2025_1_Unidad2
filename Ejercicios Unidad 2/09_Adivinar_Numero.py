import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class AdivinaNumero(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("09_Adivinar_Numero.ui", self)  # Cargar la UI

        # Generar número aleatorio entre 1 y 100
        self.numero_secreto = random.randint(1, 100)

        # Conectar botones con funciones
        self.btnAdivinar.clicked.connect(self.comprobar_numero)
        self.btnReiniciar.clicked.connect(self.reiniciar_juego)

    def comprobar_numero(self):
        try:
            # Obtener el número ingresado por el usuario
            numero_usuario = int(self.inputNumero.text())

            # Comprobar si el número es correcto
            if numero_usuario < self.numero_secreto:
                self.labelResultado.setText("El número es mayor")
            elif numero_usuario > self.numero_secreto:
                self.labelResultado.setText("El número es menor")
            else:
                self.labelResultado.setText("¡Correcto! 🎉")
        except ValueError:
            self.labelResultado.setText("Ingrese un número válido")

    def reiniciar_juego(self):
        """Genera un nuevo número secreto y limpia la interfaz"""
        self.numero_secreto = random.randint(1, 100)
        self.inputNumero.clear()
        self.labelResultado.setText("Nuevo juego iniciado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AdivinaNumero()
    ventana.show()
    sys.exit(app.exec())
