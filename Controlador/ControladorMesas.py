import traceback
from PyQt6 import QtWidgets
from Vista.VentanaRestaurante import Ui_Form
from Modelo.ModeloRestaurantes import Restaurante

class controladorVmesas(QtWidgets.QWidget):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uivm = Ui_Form()
        self.uivm.setupUi(self)
        self.restaurante = Restaurante("Restaurante")  # Inicializar con el nombre del restaurante
        self.restaurante.cargar_mesas("mesas.pkl")  # Cargar las mesas desde un archivo

        self.uivm.btnBuscar.clicked.connect(self.buscarMesa)
        self.uivm.btnGuardar.clicked.connect(self.guardarMesa)
        self.uivm.btnModificar.clicked.connect(self.modificarMesa)
        self.uivm.btnEliminar.clicked.connect(self.eliminarMesa)
        self.uivm.btnCancelar.clicked.connect(self.cancelar)
        self.uivm.btnRegresar.clicked.connect(self.regresar)

        self.uivm.btnModificar.setVisible(False)
        self.uivm.btnEliminar.setVisible(False)

        self.actualizarTablaMesas()  # Mostrar las mesas cargadas en la tabla al iniciar

    def buscarMesa(self):
        try:
            numero = self.uivm.txtBuscarmesa.text().strip()
            if not numero:
                self.mostrarMensaje("El campo 'Número de mesa' es obligatorio para buscar.")
                return

            mesa = self.restaurante.obtener_mesa(numero)
            if mesa:
                self.uivm.cbx_capacidad.setCurrentText(str(mesa.capacidad))
                self.uivm.cbx_disponibilidad.setCurrentText("Disponible" if mesa.disponible else "No disponible")
                self.uivm.btnGuardar.setVisible(False)
                self.uivm.btnModificar.setVisible(True)
                self.uivm.btnEliminar.setVisible(True)
            else:
                self.mostrarMensaje(f"No se encontró la mesa con número {numero}.")
        except Exception as e:
            print("Error al buscar la mesa:", str(e))
            traceback.print_exc()

    def guardarMesa(self):
        try:
            numero = self.uivm.txtnumerodemesa.text().strip()
            capacidad = self.uivm.cbx_capacidad.currentText()
            disponibilidad = self.uivm.cbx_disponibilidad.currentText()

            if not numero or not capacidad:
                self.mostrarMensaje("Los campos 'Número de mesa' y 'Capacidad' son obligatorios.")
                return

            capacidad = int(capacidad)
            disponible = disponibilidad == "Disponible"
            self.restaurante.agregar_mesa(numero, capacidad, disponible)
            self.restaurante.guardar_mesas("mesas.pkl")

            self.limpiarCampos()
            self.mostrarMensaje("Mesa guardada con éxito.")
            self.actualizarTablaMesas()  # Actualizar la tabla después de guardar la mesa
        except Exception as e:
            print("Error al guardar la mesa:", str(e))
            traceback.print_exc()

    def modificarMesa(self):
        try:
            numero = self.uivm.txtBuscarmesa.text().strip()
            capacidad = self.uivm.cbx_capacidad.currentText()
            disponibilidad = self.uivm.cbx_disponibilidad.currentText()

            if not numero or not capacidad:
                self.mostrarMensaje("Los campos 'Número de mesa' y 'Capacidad' son obligatorios.")
                return

            capacidad = int(capacidad)
            disponible = disponibilidad == "Disponible"
            self.restaurante.modificar_mesa(numero, capacidad, disponible)
            self.restaurante.guardar_mesas("mesas.pkl")

            self.limpiarCampos()
            self.mostrarMensaje("Mesa modificada con éxito.")
            self.actualizarTablaMesas()  # Actualizar la tabla después de modificar la mesa
        except Exception as e:
            print("Error al modificar la mesa:", str(e))
            traceback.print_exc()

    def eliminarMesa(self):
        try:
            numero = self.uivm.txtBuscarmesa.text().strip()
            if not numero:
                self.mostrarMensaje("El campo 'Número de mesa' es obligatorio para eliminar.")
                return

            self.restaurante.eliminar_mesa(numero)
            self.restaurante.guardar_mesas("mesas.pkl")

            self.limpiarCampos()
            self.mostrarMensaje("Mesa eliminada con éxito.")
            self.actualizarTablaMesas()  # Actualizar la tabla después de eliminar la mesa
        except Exception as e:
            print("Error al eliminar la mesa:", str(e))
            traceback.print_exc()

    def cancelar(self):
        self.limpiarCampos()
        self.uivm.btnGuardar.setVisible(True)
        self.uivm.btnModificar.setVisible(False)
        self.uivm.btnEliminar.setVisible(False)

    def mostrarMensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)

    def limpiarCampos(self):
        self.uivm.txtBuscarmesa.clear()
        self.uivm.cbx_capacidad.setCurrentIndex(0)
        self.uivm.cbx_disponibilidad.setCurrentIndex(0)

    def regresar(self):
        try:
            from Controlador.ControladorPrincipal import controladorVprincipal
            self.controladorprincipal = controladorVprincipal(self.cargo)
            self.controladorprincipal.show()
            self.close()
        except Exception as e:
            print("Error al regresar:", str(e))
            traceback.print_exc()

    def actualizarTablaMesas(self):
        try:
            self.uivm.tableMesas.setRowCount(0)  # Limpiar la tabla antes de actualizar
            for mesa in self.restaurante.mesas:
                row_position = self.uivm.tableMesas.rowCount()
                self.uivm.tableMesas.insertRow(row_position)
                self.uivm.tableMesas.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(mesa.numero)))
                self.uivm.tableMesas.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(mesa.capacidad)))
                self.uivm.tableMesas.setItem(row_position, 2, QtWidgets.QTableWidgetItem("Disponible" if mesa.disponible else "No disponible"))
        except Exception as e:
            print("Error al actualizar la tabla de mesas:", str(e))
            traceback.print_exc()
