import pickle

class Plato:
    def __init__(self, nombre, tipo_comida, categoria, es_vegetariano, precio):
        self.nombre = nombre
        self.tipo_comida = tipo_comida
        self.categoria = categoria
        self.es_vegetariano = es_vegetariano
        self.precio = precio

    def __str__(self):
        vegetariano = "Sí" if self.es_vegetariano else "No"
        return (f"Nombre: {self.nombre}, Tipo de comida: {self.tipo_comida}, "
                f"Categoría: {self.categoria}, Vegetariano: {vegetariano}, Precio: ${self.precio:.2f}")

class Carta:
    TIPOS_COMIDA = [
        "", "oriental", "mexicana", "carnes a la brasa", "pescados", "pasta",
        "pizza", "vegetarianos", "macrobiotica", "veganos", "tapas",
        "rapida", "picante", "detox", "celiac", "otro"
    ]

    CATEGORIAS = ["", "entrada", "postre", "plato fuerte", "guarnicion", "bebidas"]

    def __init__(self):
        self.platos = []

    def agregar_plato(self, nombre, tipo_comida, categoria, es_vegetariano, precio):
        if tipo_comida not in self.TIPOS_COMIDA:
            raise ValueError(f"Tipo de comida '{tipo_comida}' no es válido. Debe ser uno de {self.TIPOS_COMIDA}.")
        if categoria not in self.CATEGORIAS:
            raise ValueError(f"Categoría '{categoria}' no es válida. Debe ser una de {self.CATEGORIAS}.")

        plato = Plato(nombre, tipo_comida, categoria, es_vegetariano, precio)
        self.platos.append(plato)
        print(f"Plato agregado: {plato}")

    def listar_platos(self):
        for plato in self.platos:
            print(plato)

    def obtener_platos_mas_caros(self):
        if not self.platos:
            return []
        platos_ordenados = sorted(self.platos, key=lambda plato: plato.precio, reverse=True)
        return platos_ordenados

    def obtener_platos_por_categoria(self, categoria):
        if categoria not in self.CATEGORIAS:
            raise ValueError(f"Categoría '{categoria}' no es válida. Debe ser una de {self.CATEGORIAS}.")

        platos_por_categoria = [plato for plato in self.platos if plato.categoria == categoria]
        return platos_por_categoria

    def obtener_platos_vegetarianos(self):
        platos_vegetarianos = [plato for plato in self.platos if plato.es_vegetariano]
        return platos_vegetarianos


    def guardar_platos(self, archivo='platos.pkl'):
        try:
            with open(archivo, 'wb') as file:
                pickle.dump(self.platos, file)
            print(f"Platos guardados en el archivo '{archivo}'")
        except Exception as e:
            print(f"Error al guardar los platos: {e}")

    def cargar_platos(self, archivo='platos.pkl'):
        try:
            with open(archivo, 'rb') as file:
                self.platos = pickle.load(file)
            print(f"Platos cargados desde el archivo '{archivo}'")
        except Exception as e:
            print(f"Error al cargar los platos: {e}")


    def mostrar_platos(self):
        if not self.platos:
            print("No hay platos disponibles.")
        else:
            for plato in self.platos:
                print(plato)
