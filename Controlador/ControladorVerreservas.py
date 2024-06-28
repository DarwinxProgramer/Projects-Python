import traceback
from PyQt6 import QtWidgets
from Vista.VentanaListarReservas import Ui_Form
from Modelo.ModeloReservas import Reservas

class controladorverreservas(QtWidgets.QWidget):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uivlr = Ui_Form()
        self.uivlr.setupUi(self)
        self.reservas = Reservas()
        self.reservas.cargar_reservas("reservas.pkl")
        self.uivlr.btnver.clicked.connect(self.mostrarReservas)
        self.uivlr.btnRegresar.clicked.connect(self.regresar)

    def mostrarReservas(self):
        try:
            self.uivlr.tablareservas.setRowCount(0)
            todas_reservas = self.reservas.reservas
            reservas_ordenadas = sorted(todas_reservas, key=lambda r: (r.fecha, r.hora))
            for reserva in reservas_ordenadas:
                rowPosition = self.uivlr.tablareservas.rowCount()
                self.uivlr.tablareservas.insertRow(rowPosition)
                self.uivlr.tablareservas.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(reserva.numero_reserva))
                self.uivlr.tablareservas.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(reserva.hora))
                self.uivlr.tablareservas.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(reserva.fecha))
                self.uivlr.tablareservas.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(reserva.mesa))
        except Exception as e:
            print("Error al mostrar las reservas:", str(e))
            traceback.print_exc()





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
