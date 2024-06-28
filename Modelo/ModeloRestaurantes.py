from Modelo.ModeloEmpleados import Empleados
from Modelo.ModeloCarta import Carta
import pickle

class Mesa:
    def __init__(self, numero, capacidad=6, disponible=True):
        self.numero = numero
        self.capacidad = capacidad
        self.disponible = disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []
        self.horario = [f"{hora}:00" for hora in range(9, 22)]  # Horario de 9:00 a 21:00
        self.empleados = Empleados()
        self.cartas = Carta()

    def agregar_mesa(self, numero, capacidad, disponibilidad):
        mesa = Mesa(numero, capacidad, disponibilidad)
        self.mesas.append(mesa)

    def validar_horas(self, hora_inicio, hora_fin):
        return 0 <= hora_inicio <= 23 and 0 <= hora_fin <= 23 and hora_inicio < hora_fin

    def modificar_horario(self, hora_inicio, hora_fin):
        if self.validar_horas(hora_inicio, hora_fin):
            self.horario = [f"{hora}:00" for hora in range(hora_inicio, hora_fin + 1)]
            print(f"Horario actualizado: {', '.join(self.horario)}")
        else:
            print("Horas no válidas. Por favor, ingrese horas entre 0 y 23.")

    def modificar_mesa(self, numero, capacidad, disponible):
        for mesa in self.mesas:
            if mesa.numero == numero:
                mesa.capacidad = capacidad
                mesa.disponible = disponible
                return

    def eliminar_mesa(self, numero):
        self.mesas = [mesa for mesa in self.mesas if mesa.numero != numero]

    def obtener_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def guardar_mesas(self, archivo='mesas.pkl'):
        try:
            with open(archivo, 'wb') as file:
                pickle.dump(self.mesas, file)
        except Exception as e:
            print(f"Error al guardar las mesas: {e}")

    def cargar_mesas(self, archivo='mesas.pkl'):
        try:
            with open(archivo, 'rb') as file:
                self.mesas = pickle.load(file)
        except Exception as e:
            print(f"Error al cargar las mesas: {e}")
