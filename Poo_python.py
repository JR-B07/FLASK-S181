class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def agregar_bebida(self):
        id = int(input("Ingrese el ID de la bebida: "))
        nombre = input("Ingrese el nombre de la bebida: ")
        clasificacion = input("Ingrese la clasificación de la bebida: ")
        marca = input("Ingrese la marca de la bebida: ")
        precio = float(input("Ingrese el precio de la bebida: "))

        bebida = Bebida(id, nombre, clasificacion, marca, precio)
        self.bebidas.append(bebida)
        print("Bebida agregada correctamente.")

    def eliminar_bebida(self):
        id = int(input("Ingrese el ID de la bebida a eliminar: "))
        bebida = self.buscar_bebida(id)
        if bebida:
            self.bebidas.remove(bebida)
            print("Bebida eliminada correctamente.")
        else:
            print("No se encontró la bebida con el ID especificado.")

    def actualizar_bebida(self):
        id = int(input("Ingrese el ID de la bebida a actualizar: "))
        bebida = self.buscar_bebida(id)
        if bebida:
            nombre = input("Ingrese el nuevo nombre de la bebida: ")
            clasificacion = input("Ingrese la nueva clasificación de la bebida: ")
            marca = input("Ingrese la nueva marca de la bebida: ")
            precio = float(input("Ingrese el nuevo precio de la bebida: "))

            bebida.nombre = nombre
            bebida.clasificacion = clasificacion
            bebida.marca = marca
            bebida.precio = precio
            print("Bebida actualizada correctamente.")
        else:
            print("No se encontró la bebida con el ID especificado.")

    def mostrar_todas_bebidas(self):
        if len(self.bebidas) == 0:
            print("No hay bebidas en el almacén.")
        else:
            for bebida in self.bebidas:
                print(f"ID: {bebida.id}, Nombre: {bebida.nombre}, Clasificación: {bebida.clasificacion}, Marca: {bebida.marca}, Precio: {bebida.precio}")

    def buscar_bebida(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                return bebida
        return None


def mostrar_menu():
    print("\n--- ALMACÉN DE BEBIDAS ---")
    print("1. Alta de bebida")
    print("2. Baja de bebida")
    print("3. Actualizar datos de bebida")
    print("4. Mostrar todas las bebidas")
    print("5. Salir")

almacen = AlmacenBebidas()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        almacen.agregar_bebida()
    elif opcion == "2":
        almacen.eliminar_bebida()
    elif opcion == "3":
        almacen.actualizar_bebida()
    elif opcion == "4":
        almacen.mostrar_todas_bebidas()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("¡Hasta luego!")
