import sys
import time

from PyQt5 import uic, QtWidgets, QtCore
qtCreatorfile = "P16_CheckBox_Ejemplo1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorfile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    ##    self.btn_temporizador.clicked.connect(self.temporizador)

   ##     self.segundoPlano = QtCore.QTimer(self)

    def temporizadorv2(self):
        self.value = int(self.txt_temporizador.text())
        self.segundoPlano.start(250)
        if self.value > 0:
            self.value = 1
            self.txt_temporizador.setText(str(self.value))
        else:
            self.segundoPlano.stop()

    def temporizador(self):
        import time as t
        valor = int(self.txt_temporizador.txt())
        for v in range(valor, 0, -1):
            self.txt_temporizador.setText(str(v))
            print(v)
            t.sleep(0.25)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())