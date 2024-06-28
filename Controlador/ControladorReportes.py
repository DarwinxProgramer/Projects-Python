import traceback

from PyQt6 import QtWidgets
from Vista.VentanaListarReportes import Ui_Form
from Modelo.ModeloReservas import Reservas
from Modelo.ModeloCarta import Carta

class controladorreportes(QtWidgets.QWidget):
    def __init__(self, cargo):
        super().__init__()
        self.cargo = cargo
        self.uivlreportes = Ui_Form()
        self.uivlreportes.setupUi(self)
        self.reservas = Reservas()
        self.reservas.cargar_reservas("reservas.pkl")
        self.platos = Carta()
        self.platos.cargar_platos("platos.pkl")

        self.uivlreportes.btnreporte1.clicked.connect(self.reporteMesaMasReservada)
        self.uivlreportes.btnreporte2.clicked.connect(self.reporteDiasMasResercas)
        self.uivlreportes.btnreporte3.clicked.connect(self.platosMasCarosOrdenDecendente)
        self.uivlreportes.btnRegresar.clicked.connect(self.regresar)

    def reporteMesaMasReservada(self):
        try:
            if not self.reservas.reservas:
                self.mostrarMensaje("No hay datos de reservas disponibles.")
                return

            contador_reservas = {}
            for reserva in self.reservas.reservas:
                mesa = reserva.mesa
                if mesa in contador_reservas:
                    contador_reservas[mesa] += 1
                else:
                    contador_reservas[mesa] = 1

            if not contador_reservas:
                self.mostrarMensaje("No hay datos suficientes para generar el reporte.")
                return

            mesa_mas_reservada = max(contador_reservas, key=contador_reservas.get)
            numero_reservas = contador_reservas[mesa_mas_reservada]

            self.mostrarMensaje(f"La mesa más reservada es la mesa {mesa_mas_reservada} con {numero_reservas} reservas")

            self.uivlreportes.tablareporte1.setRowCount(0)
            self.uivlreportes.tablareporte1.setColumnCount(2)
            self.uivlreportes.tablareporte1.setHorizontalHeaderLabels(["Mesa", "Número de reservas de la mesa"])

            self.uivlreportes.tablareporte1.insertRow(0)
            self.uivlreportes.tablareporte1.setItem(0, 0, QtWidgets.QTableWidgetItem(str(mesa_mas_reservada)))
            self.uivlreportes.tablareporte1.setItem(0, 1, QtWidgets.QTableWidgetItem(str(numero_reservas)))

            self.uivlreportes.tablareporte1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        except Exception as e:
            self.mostrarMensaje("Error al generar el reporte de la mesa más reservada.")
            print("Error al generar el reporte de la mesa más reservada:", str(e))
            traceback.print_exc()

    def reporteDiasMasResercas(self):
        try:
            if not self.reservas.reservas:
                self.mostrarMensaje("No hay datos de reservas disponibles.")
                return

            contador_reservas = {}
            for reserva in self.reservas.reservas:
                fecha = reserva.fecha
                if fecha in contador_reservas:
                    contador_reservas[fecha] += 1
                else:
                    contador_reservas[fecha] = 1

            if not contador_reservas:
                self.mostrarMensaje("No hay datos suficientes para generar el reporte.")
                return

            self.mostrarMensaje("Reporte de días con más reservas")

            self.uivlreportes.tablareporte2.setRowCount(0)
            self.uivlreportes.tablareporte2.setColumnCount(2)
            self.uivlreportes.tablareporte2.setHorizontalHeaderLabels(["Fecha", "Número de reservas"])

            row = 0
            for fecha, numero_reservas in sorted(contador_reservas.items(), key=lambda x: x[1], reverse=True):
                self.uivlreportes.tablareporte2.insertRow(row)
                self.uivlreportes.tablareporte2.setItem(row, 0, QtWidgets.QTableWidgetItem(fecha))
                self.uivlreportes.tablareporte2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(numero_reservas)))
                row += 1

            self.uivlreportes.tablareporte2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        except Exception as e:
            self.mostrarMensaje("Error al generar el reporte de días con más reservas.")
            print("Error al generar el reporte de días con más reservas:", str(e))
            traceback.print_exc()

    def platosMasCarosOrdenDecendente(self):
        try:
            platos = self.platos.obtener_platos_mas_caros()
            if not platos:
                self.mostrarMensaje("No hay datos de platos disponibles.")
                return

            self.mostrarMensaje("Reporte de platos más caros en orden descendente")

            self.uivlreportes.tablareporte3.setRowCount(0)
            self.uivlreportes.tablareporte3.setColumnCount(2)
            self.uivlreportes.tablareporte3.setHorizontalHeaderLabels(["Plato", "Precio"])

            row = 0
            for plato in platos:
                self.uivlreportes.tablareporte3.insertRow(row)
                self.uivlreportes.tablareporte3.setItem(row, 0, QtWidgets.QTableWidgetItem(plato.nombre))
                self.uivlreportes.tablareporte3.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{plato.precio:.2f}"))
                row += 1

            self.uivlreportes.tablareporte3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        except Exception as e:
            self.mostrarMensaje("Error al generar el reporte de platos más caros.")
            print("Error al generar el reporte de platos más caros:", str(e))
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