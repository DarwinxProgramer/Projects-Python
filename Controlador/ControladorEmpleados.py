from Vista.VentanaEmpleados import Ui_VentanaEmpleados
from Modelo.ModeloEmpleados import Empleados
from PyQt6 import QtWidgets
import traceback

class controladorVempleados(QtWidgets.QWidget):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uie = Ui_VentanaEmpleados()
        self.uie.setupUi(self)

        self.uie.btnRegresar.clicked.connect(self.regresar)
        self.uie.btnGuardar.clicked.connect(self.guardarEmpleado)
        self.uie.btnModificar.clicked.connect(self.ModificarEmpleado)
        self.uie.btnCancelar.clicked.connect(self.Cancelar)
        self.uie.btnEliminar.clicked.connect(self.EliminarEmpleado)
        self.uie.btnBuscar.clicked.connect(self.BuscarEmpleado)

        self.uie.btnModificar.setVisible(False)
        self.uie.btnEliminar.setVisible(False)

        self.modelo_empleados = Empleados()
        self.modelo_empleados.cargar_empleados()

    def guardarEmpleado(self):
        try:
            cedula = self.uie.txtCedula.text().strip()
            nombre = self.uie.txtNombre.text().strip()
            apellido = self.uie.txtApellido.text().strip()
            correo = self.uie.txtCorreo.text().strip()
            cargo = self.uie.cbx_cargo.currentText().strip()

            if not all([cedula, nombre, apellido, correo, cargo]):
                self.mostrarMensaje("Todos los campos son obligatorios.")
                return

            self.modelo_empleados.registrar_empleado(cedula, nombre, apellido, correo, cargo)
            self.modelo_empleados.guardar_empleados()
            self.limpiarCampos()
            self.MostrarEmpleados()
            self.mostrarMensaje("Empleado guardado con éxito.")
        except Exception as e:
            print("Error al guardar el empleado:", str(e))
            traceback.print_exc()

    def ModificarEmpleado(self):
        try:
            cedula = self.uie.txtCedula.text().strip()
            nombre = self.uie.txtNombre.text().strip()
            apellido = self.uie.txtApellido.text().strip()
            correo = self.uie.txtCorreo.text().strip()
            cargo = self.uie.cbx_cargo.currentText().strip()

            if not all([cedula, nombre, apellido, correo, cargo]):
                self.mostrarMensaje("Todos los campos son obligatorios.")
                return

            self.modelo_empleados.modificar_empleado(cedula, nombre, apellido, correo, cargo)
            self.modelo_empleados.guardar_empleados()
            self.limpiarCampos()
            self.MostrarEmpleados()
            self.mostrarMensaje("Empleado modificado con éxito.")
        except Exception as e:
            print("Error al modificar el empleado:", str(e))
            traceback.print_exc()

    def EliminarEmpleado(self):
        try:
            cedula = self.uie.txtBuscarempleado.text().strip()

            if not cedula:
                self.mostrarMensaje("El campo de cédula es obligatorio.")
                return

            self.modelo_empleados.eliminar_empleado(cedula)
            self.modelo_empleados.guardar_empleados()
            self.limpiarCampos()
            self.MostrarEmpleados()
            self.mostrarMensaje("Empleado eliminado con éxito.")
        except Exception as e:
            print("Error al eliminar el empleado:", str(e))
            traceback.print_exc()

    def Cancelar(self):
        self.limpiarCampos()
        self.uie.btnGuardar.setVisible(True)
        self.uie.btnModificar.setVisible(False)
        self.uie.btnEliminar.setVisible(False)

    def BuscarEmpleado(self):
        try:
            cedula = self.uie.txtBuscarempleado.text()
            if not cedula:
                self.mostrarMensaje("Por favor, ingrese la cédula del empleado a buscar.")
                return

            empleado = self.modelo_empleados.empleados.get(cedula)
            if empleado:
                self.uie.txtCedula.setText(empleado['cedula'])
                self.uie.txtNombre.setText(empleado['nombre'])
                self.uie.txtApellido.setText(empleado['apellido'])
                self.uie.txtCorreo.setText(empleado['correo'])
                index = self.uie.cbx_cargo.findText(empleado['cargo'])
                if index >= 0:
                    self.uie.cbx_cargo.setCurrentIndex(index)
                self.mostrarMensaje("Empleado encontrado.")

                self.uie.btnModificar.setVisible(True)
                self.uie.btnEliminar.setVisible(True)
                self.uie.btnGuardar.setVisible(False)
            else:
                self.mostrarMensaje("Empleado no encontrado.")
                self.uie.btnGuardar.setVisible(True)
                self.uie.btnModificar.setVisible(False)
                self.uie.btnEliminar.setVisible(False)
        except Exception as e:
            print("Error al buscar el empleado:", str(e))
            traceback.print_exc()

    def MostrarEmpleados(self):
        try:
            self.uie.tableEmpleados.setRowCount(0)  # Limpiar la tabla
            for cedula, empleado in self.modelo_empleados.empleados.items():
                rowPosition = self.uie.tableEmpleados.rowCount()
                self.uie.tableEmpleados.insertRow(rowPosition)
                self.uie.tableEmpleados.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(empleado['nombre']))
                self.uie.tableEmpleados.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(empleado['apellido']))
                self.uie.tableEmpleados.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(empleado['correo']))
                self.uie.tableEmpleados.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(empleado['cargo']))
        except Exception as e:
            print("Error al mostrar los empleados:", str(e))
            traceback.print_exc()

    def regresar(self):
        try:
            from Controlador.ControladorPrincipal import controladorVprincipal
            self.controladorprincipal = controladorVprincipal(self.cargo)
            self.controladorprincipal.show()
            self.close()
        except Exception as e:
            print("Error al regresar:", str(e))
            traceback.print_exc()

    def limpiarCampos(self):
        self.uie.txtCedula.clear()
        self.uie.txtNombre.clear()
        self.uie.txtApellido.clear()
        self.uie.txtCorreo.clear()
        self.uie.cbx_cargo.setCurrentIndex(0)
        self.uie.txtBuscarempleado.clear()

    def mostrarMensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)
