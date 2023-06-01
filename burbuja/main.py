'''El siguiente programa guarda los objetos, de un archivo de texto, en un arreglo'''
from buscar import *
from burbuja import *
from burbujapeso import verificador_peso
from bubuja_piezas import verificador_cantidad
from eliminar import*
class Productos:
    '''productos'''
    def __init__(self, nombre, precio=1, peso=1, cantidad=0):
        '''caracteristicas de los productos'''
        self.nombre = nombre
        self.precio = float(precio)
        self.peso = int(peso)
        self.cantidad = int(cantidad)

    def __str__(self):
        '''hace que el arreglo de productos sea legible'''
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Peso: {self.peso}, Piezas: {self.cantidad}"

    def buscar():
        '''busca el producto por su nombre'''
        producto_a_buscar = input("Ingrese el nombre del producto: ").lower()
        ubicacion = localizar(lista,producto_a_buscar)
        producto_encontrado = buscar_producto(lista, producto_a_buscar)
        if producto_encontrado:
            print("producto: \n ",producto_encontrado,"\nposicion del producto: ", ubicacion )
        elif commando:
            print("Producto no encontrado.")

    def ordenar():
        '''ordena el los productos de menor a mayor precio'''
        opc_ordenar = input("desea ordenar por peso, precio o piezas ?: ").lower()
        if opc_ordenar == "precio":
            verifica = verificador_precio(lista)
            if verifica:
                for producto in lista:
                    print("Numeros ordenados: ",producto)
            else:
                print(" los numeros ya estan ordenados ")

                input("precione enter para continuar...")

        elif opc_ordenar == "peso":
            verifica = verificador_peso(lista)
            if verifica:
                for producto in lista:
                    print("Numeros ordenados: ",producto)
            else:
                print(" los numeros ya estan ordenados ")

                input("precione enter para continuar...")
        elif opc_ordenar == "piezas":
            verifica = verificador_cantidad(lista)
            if verifica:
                for producto in lista:
                    print("Numeros ordenados: ",producto)
            else:
                print(" los numeros ya estan ordenados ")

                input("precione enter para continuar...")

        else:
            print("ingrese opcion correcta")

    def agregar_producto():
        '''agrega un producto al archivo de texto'''
        nombre = input("Ingrese el nombre del producto: ").lower()
        verificar = buscar_producto(lista,nombre)
        if verificar:
            print("el producto ya se encuentra en el almacen: ")
        else:
            precio = input("Ingrese el precio del producto: ")
            peso = input("Ingrese el peso del producto: ")
            cantidad = input("piezas: ")
            nuevo_producto = Productos(nombre, precio, peso, cantidad)
            lista.append(nuevo_producto)

            with open('basedatos.txt', 'a') as text:
                text.write(f"{nombre},{precio},{peso},{cantidad}\n")

            print("Producto agregado correctamente:", nuevo_producto)

    def eliminar_producto():
        '''elimina el producto ingresando su nombre'''
        producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").lower()
        producto_a_eliminar = producto_a_eliminar.lower()
        verifica = buscar_producto(lista,producto_a_eliminar)
        if verifica:
            list = eliminar(lista,producto_a_eliminar)
            with open('basedatos.txt', 'w') as text:
                for producto in list:
                    text.write(f"{producto.nombre},{producto.precio},{producto.peso},{producto.cantidad}\n")
            print("el producto ha sido eliminado: \n")
            for producto in list:
                print(producto)
        else:
            print("el producto no se encuentra en la lista")

    def imprimir_productos():
        for producto in lista:
            print("Los productos son:\n",producto)

with open('basedatos.txt', 'r') as text:
    lista = []
    for line in text:
        atributos = line.strip().split(',')
        lista.append(Productos(*atributos))

commando = ""
while (commando != "exit"):
    commando = input('-->').lower()
    opciones = {
        "buscar": Productos.buscar,
        "ordenar": Productos.ordenar,
        "agregar": Productos.agregar_producto,
        "eliminar": Productos.eliminar_producto,
        "productos": Productos.imprimir_productos
    }
    if commando in opciones:
        opciones[commando]()
    elif commando == "exit":
        break
    else:
        print("Comando inválido")
