from Vista.VentanaCarta import Ui_Form
from PyQt6 import QtWidgets
from Modelo.ModeloCarta import Carta
import traceback

class controladorVcarta(QtWidgets.QWidget):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uic = Ui_Form()
        self.uic.setupUi(self)
        self.carta = Carta()
        self.uic.btnRegresar.clicked.connect(self.regresar)
        self.uic.btnGuardar.clicked.connect(self.guardar)
        self.uic.btnCancelar.clicked.connect(self.Cancelar)
        self.uic.cbx_tipo.addItems(Carta.TIPOS_COMIDA)
        self.uic.cbx_cat.addItems(Carta.CATEGORIAS)

    def guardar(self):
        try:
            nombre = self.uic.txtNombre.text().strip()
            tipo_comida = self.uic.cbx_tipo.currentText()
            categoria = self.uic.cbx_cat.currentText()
            es_vegetariano = self.uic.radioButtonsi.isChecked()
            precio_text = self.uic.txtPrecio.text().strip()
            if not nombre:
                self.mostrarMensaje("El campo 'Nombre' es obligatorio.")
                return

            if tipo_comida not in Carta.TIPOS_COMIDA:
                self.mostrarMensaje("Seleccione un tipo de comida válido.")
                return

            if categoria not in Carta.CATEGORIAS:
                self.mostrarMensaje("Seleccione una categoría válida.")
                return

            if not precio_text:
                self.mostrarMensaje("El campo 'Precio' es obligatorio.")
                return

            try:
                precio = float(precio_text)
            except ValueError:
                self.mostrarMensaje("El precio debe ser un número válido.")
                return

            self.carta.agregar_plato(nombre, tipo_comida, categoria, es_vegetariano, precio)
            self.carta.guardar_platos("platos.pkl")
            self.actualizarTabla()
            self.limpiarCampos()
            self.mostrarMensaje("Plato guardado con éxito.")
        except Exception as e:
            print("Error al guardar el plato:", str(e))
            traceback.print_exc()

    def Cancelar(self):
        self.limpiarCampos()

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
        self.uic.txtNombre.clear()
        self.uic.txtPrecio.clear()
        self.uic.cbx_tipo.setCurrentIndex(0)
        self.uic.cbx_cat.setCurrentIndex(0)
        self.uic.radioButtonsi.setChecked(False)
        self.uic.radioButtonno.setChecked(False)

    def mostrarMensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)

    def actualizarTabla(self):
        try:
            self.uic.tableCarta.setRowCount(0)  # Limpiar la tabla
            for plato in self.carta.platos:
                rowPosition = self.uic.tableCarta.rowCount()
                self.uic.tableCarta.insertRow(rowPosition)
                self.uic.tableCarta.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(plato.nombre))
                self.uic.tableCarta.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(plato.tipo_comida))
                self.uic.tableCarta.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(plato.categoria))
                es_vegetariano = "Sí" if plato.es_vegetariano else "No"
                self.uic.tableCarta.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(es_vegetariano))
                self.uic.tableCarta.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(f"${plato.precio:.2f}"))
        except Exception as e:
            print("Error al actualizar la tabla:", str(e))
            traceback.print_exc()
