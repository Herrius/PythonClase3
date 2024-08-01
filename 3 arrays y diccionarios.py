class IntroduccionColecciones:
    def __init__(self):
        # Este constructor inicializa ejemplos de listas y diccionarios que se usarán en las demostraciones
        self.ejemplo_lista = [10, 20, 30, 40, 50]
        self.ejemplo_diccionario = {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York'}

    def demo_listas(self):
        # Mostrar cómo se accede a los elementos de una lista
        print("Acceso a elementos de la lista:")
        print(self.ejemplo_lista[0])  # Acceso al primer elemento
        print(self.ejemplo_lista[-1])  # Acceso al último elemento

        # Modificar elementos de la lista
        print("\nModificación de elementos:")
        self.ejemplo_lista[2] = 35
        print(self.ejemplo_lista)

        # Añadir y eliminar elementos
        print("\nAñadir y eliminar elementos:")
        self.ejemplo_lista.append(60)  # Añadir al final
        print(self.ejemplo_lista)
        self.ejemplo_lista.insert(2, 25)  # Insertar en la posición 2
        print(self.ejemplo_lista)
        self.ejemplo_lista.pop()  # Eliminar el último elemento
        print(self.ejemplo_lista)
        self.ejemplo_lista.remove(25)  # Eliminar el primer 25 encontrado
        print(self.ejemplo_lista)

    def demo_diccionarios(self):
        # Mostrar cómo se accede a los valores en un diccionario
        print("Acceso a elementos del diccionario:")
        print(self.ejemplo_diccionario['nombre'])  # Acceso por clave
        print(self.ejemplo_diccionario.get('edad', 'No encontrado'))  # Uso de get para evitar KeyError

        # Modificar y añadir elementos
        print("\nModificación y adición de elementos:")
        self.ejemplo_diccionario['edad'] = 31  # Modificar
        print(self.ejemplo_diccionario)
        self.ejemplo_diccionario['profesion'] = 'Ingeniera'  # Añadir
        print(self.ejemplo_diccionario)

        # Eliminar elementos
        print("\nEliminar elementos:")
        del self.ejemplo_diccionario['ciudad']  # Eliminar clave específica
        print(self.ejemplo_diccionario)
        self.ejemplo_diccionario.pop('profesion', None)  # Uso de pop con manejo de no existencia
        print(self.ejemplo_diccionario)

def main():
    colecciones = IntroduccionColecciones()
    print("Demostración de listas:")
    colecciones.demo_listas()
    print("\nDemostración de diccionarios:")
    colecciones.demo_diccionarios()

if __name__ == "__main__":
    main()
