import traceback
from PyQt6 import QtWidgets, QtCore
from Vista.VentanaReservar import Ui_VentanaReservar
from Modelo.ModeloCarta import Carta
from Modelo.ModeloReservas import Reservas
from Modelo.ModeloRestaurantes import Restaurante

class controladorVreservas(QtWidgets.QWidget):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uic = Ui_VentanaReservar()
        self.uic.setupUi(self)
        self.reservas = Reservas()
        self.carta = Carta()

        self.restaurante = Restaurante("Restaurante")
        self.reservas.cargar_reservas("reservas.pkl")
        self.carta.cargar_platos("platos.pkl")
        self.restaurante.cargar_mesas("mesas.pkl")

        self.uic.btnRegresar.clicked.connect(self.regresar)
        self.uic.btnGuardar.clicked.connect(self.reservar)
        self.uic.btnCancelar.clicked.connect(self.cancelar)

        self.cargarMesas()
        self.uic.calendarioWFecha.selectionChanged.connect(self.actualizarHorasDisponibles)
        self.actualizarHorasDisponibles()

    def cargarMesas(self):
        try:
            self.uic.cbxMesas.clear()
            for mesa in self.restaurante.mesas:
                self.uic.cbxMesas.addItem(f"Mesa {mesa.numero}")
        except Exception as e:
            print("Error al cargar las mesas:", str(e))
            traceback.print_exc()

    def cargarHorasDisponibles(self, fecha):
        try:
            horas_disponibles = self.restaurante.horario
            self.uic.tableHora.setRowCount(0)
            for hora in horas_disponibles:
                estado = self.obtenerEstadoHora(hora, fecha)
                rowPosition = self.uic.tableHora.rowCount()
                self.uic.tableHora.insertRow(rowPosition)
                self.uic.tableHora.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(hora))
                self.uic.tableHora.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(estado))
        except Exception as e:
            print("Error al cargar las horas disponibles:", str(e))
            traceback.print_exc()

    def obtenerEstadoHora(self, hora, fecha):
        for reserva in self.reservas.obtener_reservas(fecha):
            if reserva.hora == hora:
                return "Reservada"
        return "Disponible"

    def reservar(self):
        try:
            numero_reserva = self.uic.txtNumeroReserva.text().strip()
            fecha = self.uic.calendarioWFecha.selectedDate().toString("yyyy-MM-dd")
            mesa = self.uic.cbxMesas.currentText()
            hora = self.getSelectedHora()

            if not numero_reserva:
                self.mostrarMensaje("El campo 'Número de reserva' es obligatorio.")
                return
            if not hora:
                self.mostrarMensaje("Debe seleccionar una hora para la reserva.")
                return

            estado = self.obtenerEstadoHora(hora, fecha)
            if estado == "Reservada":
                self.mostrarMensaje("La hora seleccionada no está disponible.")
                return

            self.reservas.realizar_reserva(numero_reserva, hora, fecha, mesa)
            self.reservas.guardar_reservas("reservas.pkl")
            self.limpiarCampos()
            self.actualizarHorasDisponibles()
            self.mostrarMensaje("Reserva realizada con éxito.")
        except Exception as e:
            print("Error al realizar la reserva:", str(e))
            traceback.print_exc()

    def getSelectedHora(self):
        selected_items = self.uic.tableHora.selectedItems()
        if selected_items:
            return selected_items[0].text()
        return None

    def cancelar(self):
        self.limpiarCampos()

    def limpiarCampos(self):
        self.uic.txtNumeroReserva.clear()
        self.uic.calendarioWFecha.setSelectedDate(QtCore.QDate.currentDate())
        self.uic.cbxMesas.setCurrentIndex(0)
        self.uic.tableHora.clearSelection()

    def mostrarMensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)

    def regresar(self):
        try:
            from Controlador.ControladorPrincipal import controladorVprincipal
            self.controladorprincipal = controladorVprincipal(self.cargo)
            self.controladorprincipal.show()
            self.close()
        except Exception as e:
            print("Error al regresar:", str(e))
            traceback.print_exc()

    def actualizarHorasDisponibles(self):
        fecha = self.uic.calendarioWFecha.selectedDate().toString("yyyy-MM-dd")
        self.cargarHorasDisponibles(fecha)
