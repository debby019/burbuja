'''Descripcion del programa:'''
from buscar import *
from burbuja import *
class Productos:
    '''productos'''
    def __init__(self, nombre, precio=1, peso=1, fragil=1):
        '''caracteristicas de los productos'''
        self.nombre = nombre
        self.precio = float(precio)
        self.peso = int(peso)
        self.fragil = int(fragil)

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Peso: {self.peso}, Fragilidad: {self.fragil}"

    def buscar():
        producto_a_buscar = input("Ingrese el nombre del producto: ")
        ubicacion = localizar(lista,producto_a_buscar)
        producto_encontrado = buscar_producto(lista, producto_a_buscar)
        if producto_encontrado:
            print("producto: \n ",producto_encontrado,"\nposicion del producto: ", ubicacion )
        elif commando:
            print("Producto no encontrado.")

    def ordenar_precio():
        '''ordena el los productos de menor a mayor precio'''
        verifica = verificador(lista)
        if verifica:
            for producto in lista:
                print("Numeros ordenados: ",producto)
        else:
            print(" los numeros ya estan ordenados ")

            input("precione enter para continuar...")
    
    def agregar_producto():
        '''agrega un producto al archivo de texto'''
        nombre = input("Ingrese el nombre del producto: ").lower()
        verificar = buscar_producto(lista,nombre)
        if verificar:
            print("el producto ya se encuentra en el almacen: ")
        else:
            precio = input("Ingrese el precio del producto: ")
            peso = input("Ingrese el peso del producto: ")
            fragil = input("Es el producto fragil? (1 para si, 0 para no): ")
            nuevo_producto = Productos(nombre, precio, peso, fragil)
            lista.append(nuevo_producto)

            with open('basedatos.txt', 'a') as text:
                text.write(f"{nombre},{precio},{peso},{fragil}\n")
            for producto in lista:
                print("Producto agregado correctamente:", producto)

    '''def eliminar_producto():
        producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        producto_a_eliminar = producto_a_eliminar.lower()

        with open('basedatos.txt', 'w') as text:
            for producto in lista:
                text.write(f"{producto.nombre},{producto.precio},{producto.peso},{producto.fragil}\n")

            print("El producto se elimino del archivo de texto.")'''

with open('basedatos.txt', 'r') as text:
    lista = []
    for line in text:
        atributos = line.strip().split(',')
        lista.append(Productos(*atributos))

commando = ""
while (commando != "exit"):
    commando = input("Que desea hacer?")
    if commando == "buscar":
        Productos.buscar()
    elif commando == "ordenar":
        Productos.ordenar_precio()
    elif commando == "agregar":
        Productos.agregar_producto()
