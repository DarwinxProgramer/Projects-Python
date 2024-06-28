from PyQt6 import QtWidgets
import sys
from Controlador.ControladorLogin import controladorVlogin


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controladorlogin = controladorVlogin()
    controladorlogin.setWindowTitle("::Bienvenido")
    controladorlogin.show()
    sys.exit(app.exec())