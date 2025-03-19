import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTime
from PyQt6 import uic  # Cargar el .ui sin convertirlo


class ConversorHoras(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("02_Conversor_Horas.ui", self)  # Cargar la UI

        # Conectar botón a la función de conversión
        self.btnConvertir.clicked.connect(self.convertir_a_segundos)

    def convertir_a_segundos(self):
        # Obtener la hora ingresada
        hora = self.timeEdit.time()
        horas = hora.hour()
        minutos = hora.minute()
        segundos = hora.second()

        # Convertir a segundos
        total_segundos = (horas * 3600) + (minutos * 60) + segundos

        # Mostrar el resultado
        self.labelResultado.setText(f"Segundos del día: {total_segundos}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ConversorHoras()
    ventana.show()
    sys.exit(app.exec())
