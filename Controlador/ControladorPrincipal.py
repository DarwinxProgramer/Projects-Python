import traceback
from PyQt6 import QtWidgets
from Vista.VentanaPrincipal import Ui_ventanaPrincipal

class controladorVprincipal(QtWidgets.QMainWindow):
    def __init__(self, cargo):
        super().__init__()
        self.uivp = Ui_ventanaPrincipal()
        self.uivp.setupUi(self)
        self.cargo = cargo
        self.setupMenu()
        self.uivp.actionMesa.triggered.connect(self.reservar)
        self.uivp.actionVerReservaciones.triggered.connect(self.reservas)
        self.uivp.actionReportes.triggered.connect(self.reportes)
        self.uivp.actionEmpleados.triggered.connect(self.empleados)
        self.uivp.actionCarta.triggered.connect(self.carta)
        self.uivp.actionMesas.triggered.connect(self.mesas)
        self.uivp.actionInformacion.triggered.connect(self.acercade)
        self.uivp.btnRegresar.clicked.connect(self.regresar)

    def setupMenu(self):
        if self.cargo == "Administrador":
            self.uivp.menuReservar.menuAction().setVisible(True)
            self.uivp.menuVer.menuAction().setVisible(True)
            self.uivp.menuAdministrar.menuAction().setVisible(True)
            self.uivp.menuAcerca_de.menuAction().setVisible(True)
        elif self.cargo == "Mesero":
            self.uivp.menuAdministrar.menuAction().setVisible(False)
            self.uivp.actionReportes.setVisible(False)


    def reservar(self):
        try:
            from Controlador.ControladorReservas import controladorVreservas
            self.controladorreservas = controladorVreservas(self.cargo)
            self.controladorreservas.setWindowTitle("Reservar")
            self.controladorreservas.show()
            self.close()
        except Exception as e:
            print("Error al abrir la ventana de reservas:", str(e))
            traceback.print_exc()

    def reservas(self):
        try:
            from Controlador.ControladorVerreservas import controladorverreservas
            self.controladorreservas = controladorverreservas(self.cargo)
            self.controladorreservas.setWindowTitle("Lista de reservas")
            self.controladorreservas.show()
            self.close()
        except Exception as e:
            print("Error al abrir la ventana para ver las reservas:", str(e))
            traceback.print_exc()

    def reportes(self):
        try:
            from Controlador.ControladorReportes import controladorreportes
            self.controladorreporte = controladorreportes(self.cargo)
            self.controladorreporte.setWindowTitle("Reportes")
            self.controladorreporte.show()
            self.close()
        except Exception as e:
            print("Error al abrir la ventana de reportes:", str(e))
            traceback.print_exc()

    def empleados(self):
        try:
            from Controlador.ControladorEmpleados import controladorVempleados
            self.controladorempleados = controladorVempleados(self.cargo)
            self.controladorempleados.setWindowTitle("Empleados")
            self.controladorempleados.show()
            self.close()
        except Exception as e:
            print("Error al abrir la ventana de empleados:", str(e))
            traceback.print_exc()

    def carta(self):
        try:
            from Controlador.ControladorCarta import controladorVcarta
            self.controladorcarta = controladorVcarta(self.cargo)
            self.controladorcarta.setWindowTitle("Carta")
            self.controladorcarta.show()
            self.close()
        except Exception as e:
            print("Error al abrir la ventana de la carta:", str(e))
            traceback.print_exc()

    def mesas(self):
        try:
            from Controlador.ControladorMesas import controladorVmesas
            self.controladormesas = controladorVmesas(self.cargo)
            self.controladormesas.setWindowTitle("Gestion de mesas")
            self.controladormesas.show()
            self.close()
        except Exception as e:
            print("Error al abrir la ventana de mesas:", str(e))
            traceback.print_exc()

    def acercade(self):
        try:
            from Controlador.ControladorAcercade import controladorVacercade
            self.controladoracercade = controladorVacercade(self.cargo)
            self.controladoracercade.setWindowTitle("Acerca De")
            self.controladoracercade.show()
            self.close()
        except Exception as e:
            print("Error al abrir Acerca de:", str(e))
            traceback.print_exc()

    def regresar(self):
        try:
            from Controlador.ControladorLogin import controladorVlogin
            self.controladorlogin = controladorVlogin()
            self.controladorlogin.show()
            self.close()
        except Exception as e:
            print("Error al regresar:", str(e))
            traceback.print_exc()
