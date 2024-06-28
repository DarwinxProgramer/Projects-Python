import traceback
from PyQt6 import QtWidgets
from Vista.VentanaLogin import Ui_VentanaLogin
from Modelo.ModeloEmpleados import Empleados

class controladorVlogin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.uivl = Ui_VentanaLogin()
        self.uivl.setupUi(self)
        self.empleados = Empleados()
        self.empleados.cargar_empleados("empleados.pkl")
        self.uivl.btnIngresar.clicked.connect(self.ingresar)

    def ingresar(self):
        try:
            usuario = self.uivl.txtUser.text().strip()
            contrasena = self.uivl.txtContrasena.text().strip()

            cargo = self.validaringreso(usuario, contrasena)
            if cargo:
                from Controlador.ControladorPrincipal import controladorVprincipal
                self.controladorprincipal = controladorVprincipal(cargo)
                self.controladorprincipal.show()
                self.close()
            else:
                self.mostrarMensaje("Usuario o contraseña incorrectos.")
                self.limpiarcampos()
        except Exception as e:
            print("Error al ingresar:", str(e))
            traceback.print_exc()

    def validaringreso(self, usuario, contrasena):
        for empleado in self.empleados.obtener_empleados().values():
            if empleado["correo"] == usuario and empleado["cedula"] == contrasena:
                return empleado["cargo"]
        return None


    def mostrarMensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)


    def limpiarcampos(self):
        self.uivl.txtContrasena.clear()
        self.uivl.txtUser.clear()