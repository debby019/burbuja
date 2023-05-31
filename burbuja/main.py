'''Descripcion del programa:'''
from buscar import *
class Productos:
    '''productos'''
    def __init__(self, nombre, precio=1, peso=1, fragil=1):
        '''caracteristicas de los productos'''
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.fragil = fragil

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Peso: {self.peso}, Fragilidad: {self.fragil}"
    def buscar():
        producto_a_buscar = input("Ingrese el nombre del producto: ")
        producto_encontrado = buscar_producto(lista, producto_a_buscar)
        if producto_encontrado:
            print(" el producto se encuentra en la posicion: ",producto_encontrado)
        elif commando != "exit":
            print("Producto no encontrado.")

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
