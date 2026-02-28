# Sistema de Gestión de Contactos
# Documentación: Menú interactivo para CRUD de contactos.
# Autor: Osvaldo Andrés Muñoz Valenzuela
# Fecha: 28/02/2026

class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Tel: {self.telefono}, Correo: {self.correo}, Dir: {self.direccion}"

class GestorContactos:
    def __init__(self):
        self.contactos = []  # Lista para almacenar instancias de Contacto
    
    def agregar(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")
    
    def buscar(self, criterio):
        resultados = [c for c in self.contactos if criterio.lower() in c.nombre.lower() or criterio in c.telefono]
        if resultados:
            for c in resultados:
                print(c)
        else:
            print("No se encontraron contactos.")
        return resultados
    
    def editar(self, indice, **kwargs):
        if 0 <= indice < len(self.contactos):
            contacto = self.contactos[indice]
            for clave, valor in kwargs.items():
                setattr(contacto, clave, valor)
            print("Contacto editado.")
        else:
            print("Índice inválido.")
    
    def eliminar(self, indice):
        if 0 <= indice < len(self.contactos):
            eliminado = self.contactos.pop(indice)
            print(f"Contacto eliminado: {eliminado.nombre}")
        else:
            print("Índice inválido.")

# Menú principal con sentencias básicas e iterativas
def menu():
    gestor = GestorContactos()
    while True:
        print("\n1. Agregar\n2. Buscar\n3. Editar\n4. Eliminar\n5. Mostrar todos\n6. Salir")
        opcion = input("Opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")
            contacto = Contacto(nombre, telefono, correo, direccion)
            gestor.agregar(contacto)
        
        elif opcion == '2':
            criterio = input("Criterio (nombre/teléfono): ")
            gestor.buscar(criterio)
        
        elif opcion == '3':
            indice = int(input("Índice a editar: "))
            # Ejemplo simple: editar nombre
            nuevo_nombre = input("Nuevo nombre: ")
            gestor.editar(indice, nombre=nuevo_nombre)
        
        elif opcion == '4':
            indice = int(input("Índice a eliminar: "))
            gestor.eliminar(indice)
        
        elif opcion == '5':
            for i, c in enumerate(gestor.contactos):
                print(f"{i}: {c}")
        
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
