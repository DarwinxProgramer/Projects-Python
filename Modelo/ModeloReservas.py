class Reserva:
    def __init__(self, numero_reserva, hora, fecha, mesa):
        self.numero_reserva = numero_reserva
        self.hora = hora
        self.fecha = fecha
        self.mesa = mesa

    def __str__(self):
        return (f"Reserva #{self.numero_reserva} "
                f"para la mesa {self.mesa} a las {self.hora} del {self.fecha}")

import pickle

class Reservas:
    def __init__(self):
        self.reservas = []

    def realizar_reserva(self, numero_reserva, hora, fecha, mesa):
        reserva = Reserva(numero_reserva, hora, fecha, mesa)
        self.reservas.append(reserva)
        print(f"Reserva realizada: {reserva}")

    def guardar_reservas(self, archivo):
        with open(archivo, 'wb') as file:
            pickle.dump(self.reservas, file)
        print("Reservas guardadas correctamente.")

    def cargar_reservas(self, archivo):
        try:
            with open(archivo, 'rb') as file:
                self.reservas = pickle.load(file)
            print("Reservas cargadas correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. No se pudieron cargar las reservas.")
        except EOFError:
            print("Archivo vacío. No se pudieron cargar las reservas.")

    def obtener_reservas(self, fecha):
        reservas_por_fecha = [reserva for reserva in self.reservas if reserva.fecha == fecha]
        return reservas_por_fecha