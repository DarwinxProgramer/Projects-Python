from Vista.VentanaAcercade import Ui_VentanaAcercade
from PyQt6 import QtWidgets
import traceback


class controladorVacercade(QtWidgets.QMainWindow):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uiac = Ui_VentanaAcercade()
        self.uiac.setupUi(self)
        self.uiac.btnRegresar.clicked.connect(self.regresar)

    def regresar(self):
        try:
            from Controlador.ControladorPrincipal import controladorVprincipal
            self.controladorprincipal = controladorVprincipal(self.cargo)
            self.controladorprincipal.show()
            self.close()
        except Exception as e:
            print("Error al regresar:", str(e))
            traceback.print_exc()
