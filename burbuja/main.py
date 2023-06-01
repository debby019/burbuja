'''Este programa lee los productos de un archivo de texto y realiza diferentes funciones'''
from buscar import localizar, buscar_producto
from burbuja import verificador_precio
from burbujapeso import verificador_peso
from burbuja_piezas import verificador_cantidad
from eliminar import eliminar


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
        return (
            f"Nombre: {self.nombre},"
            f"Precio: {self.precio},"
            f"Peso: {self.peso},"
            f"Piezas: {self.cantidad}"
        )

    def buscar(self):
        '''busca el producto por su nombre'''
        producto_a_buscar = input("Ingrese el nombre del producto: ").lower()
        ubicacion = localizar(lista, producto_a_buscar)
        producto_encontrado = buscar_producto(lista, producto_a_buscar)
        if producto_encontrado:
            print("producto: \n ", producto_encontrado, "\nposicion del producto: ", ubicacion)
        else:
            print("Producto no encontrado.")

    def ordenar(self):
        '''ordena el los productos de menor a mayor precio'''
        dato = input("¿Desea ordenar por precio, peso o piezas?: ").lower()
        opciones_ordenar = {
            "precio": verificador_precio,
            "peso": verificador_peso,
            "piezas": verificador_cantidad
        }
        if dato in opciones_ordenar:
            verificador = opciones_ordenar[dato]
            if verificador(lista):
                for objetos in lista:
                    print("Productos ordenados: ", objetos)
            else:
                print("Los productos ya están ordenados.")
            input("Presione Enter para continuar...")
        else:
            print("Ingrese una opción válida.")

    def agregar_producto(self):
        '''agrega un producto al archivo de texto'''
        nombre = input("Ingrese el nombre del producto: ").lower()
        verificar = buscar_producto(lista, nombre)
        if verificar:
            print("El producto ya se encuentra en el almacén: ")
        else:
            precio = input("Ingrese el precio del producto: ")
            peso = input("Ingrese el peso del producto: ")
            cantidad = input("Ingrese la cantidad(gramos): ")
            nuevo_producto = Productos(nombre, precio, peso, cantidad)
            lista.append(nuevo_producto)

            with open('basedatos.txt', 'a', encoding='utf-8') as texto:
                texto.write(f"{nombre},{precio},{peso},{cantidad}\n")

            print("Producto agregado correctamente:", nuevo_producto)

    def eliminar_producto(self):
        '''elimina el producto ingresando su nombre'''
        producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").lower()
        verifica = buscar_producto(lista, producto_a_eliminar)
        if verifica:
            lista_productos = eliminar(lista, producto_a_eliminar)
            with open('basedatos.txt', 'w', encoding='utf-8') as texto_e:
                for prod in lista_productos:
                    linea = f"{prod.nombre},{prod.precio},{prod.peso},{prod.cantidad}\n"
                    texto_e.write(linea)
            print("El producto ha sido eliminado: \n")
            for prod in lista_productos:
                print(prod)
        else:
            print("El producto no se encuentra en la lista")

    def imprimir_productos(self):
        '''imprime todos los productos'''
        print("Los productos son:\n")
        for prod in lista:
            print(prod)

lista = []
with open('basedatos.txt', 'r', encoding='utf-8') as texto_producto:
    for lineas in texto_producto:
        atributos = lineas.strip().split(',')
        lista.append(Productos(*atributos))

comando = ""
while comando != "exit":
    print("lista de comandos: [buscar, ordenar, agregar, eliminar, productos]")
    comando = input('-->').lower()
    opciones = {
        "buscar": Productos.buscar,
        "ordenar": Productos.ordenar,
        "agregar": Productos.agregar_producto,
        "eliminar": Productos.eliminar_producto,
        "productos": Productos.imprimir_productos
    }
    if comando in opciones:
        opciones[comando](lista)
    else:
        print("Comando inválido")
