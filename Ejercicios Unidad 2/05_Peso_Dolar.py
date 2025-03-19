import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic  # Cargar el .ui sin convertirlo
import requests  # Para obtener la tasa de cambio actual


class ConversorMoneda(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("05_Peso_Dolar.ui", self)  # Cargar la UI

        # Conectar botón a la función de conversión
        self.btnConvertir.clicked.connect(self.convertir_a_usd)

        # Obtener la tasa de cambio actual
        self.tasa_cambio = self.obtener_tasa_cambio()

    def obtener_tasa_cambio(self):
        try:
            url = "https://api.exchangerate-api.com/v4/latest/MXN"
            response = requests.get(url)
            data = response.json()
            return data["rates"]["USD"]
        except Exception:
            return 0.058  # Valor aproximado en caso de error

    def convertir_a_usd(self):
        try:
            # Obtener el valor ingresado y convertirlo a float
            pesos = float(self.inputPesos.text())
            dolares = pesos * self.tasa_cambio  # Convertir a dólares

            # Mostrar el resultado
            self.labelResultado.setText(f"{dolares:.2f} USD")
        except ValueError:
            self.labelResultado.setText("Ingrese un número válido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ConversorMoneda()
    ventana.show()
    sys.exit(app.exec())
