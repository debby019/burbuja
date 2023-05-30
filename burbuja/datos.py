'''Descripcion del programa:'''
class productos:
    def __init__(self, nombre, precio=1, peso=1, fragil=1):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.fragil = fragil

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Peso: {self.peso}, Fragilidad: {self.fragil}"

with open('basedatos.txt', 'r') as text:
    lista = []
    for line in text:
        atributos = line.strip().split(',')
        lista.append(productos(*atributos))
for producto in lista:
    print(producto)
