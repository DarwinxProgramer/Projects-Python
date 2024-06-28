import pickle

class Empleados:
    def __init__(self):
        self.empleados = {}

    def registrar_empleado(self, cedula, nombre, apellido, correo, cargo):
        nuevo_empleado = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "cargo": cargo
        }
        self.empleados[cedula] = nuevo_empleado

    def modificar_empleado(self, cedula, nombre, apellido, correo, cargo):
        if cedula in self.empleados:
            self.empleados[cedula] = {
                "cedula": cedula,
                "nombre": nombre,
                "apellido": apellido,
                "correo": correo,
                "cargo": cargo
            }

    def eliminar_empleado(self, cedula):
        if cedula in self.empleados:
            del self.empleados[cedula]

    def guardar_empleados(self, archivo='empleados.pkl'):
        with open(archivo, 'wb') as file:
            pickle.dump(self.empleados, file)

    def cargar_empleados(self, archivo='empleados.pkl'):
        try:
            with open(archivo, 'rb') as file:
                self.empleados = pickle.load(file)
        except FileNotFoundError:
            print("Archivo no encontrado. No se pudieron cargar los empleados.")
        except EOFError:
            print("Archivo vacío. No se pudieron cargar los empleados.")

    def obtener_empleados(self):
        return self.empleados
