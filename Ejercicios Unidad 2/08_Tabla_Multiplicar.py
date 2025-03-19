import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class TablaMultiplicar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("08_Tabla_Multiplicar.ui", self)  # Cargar la UI

        # Conectar botón a la función de generación
        self.btnGenerar.clicked.connect(self.generar_tabla)

    def generar_tabla(self):
        try:
            # Obtener el número ingresado
            numero = int(self.inputNumero.text())

            # Generar la tabla de multiplicar
            tabla = "\n".join([f"{numero} x {i} = {numero * i}" for i in range(1, 11)])

            # Mostrar la tabla en el QTextEdit
            self.textResultado.setPlainText(tabla)
        except ValueError:
            self.textResultado.setPlainText("Ingrese un número válido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TablaMultiplicar()
    ventana.show()
    sys.exit(app.exec())
