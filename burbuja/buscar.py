'''este codigo localiza un elemento dentro de un arreglo y te da su ubicacion'''
def localizar(productos, nombre):
    list = []
    i=0
    for producto in productos:
        if producto.nombre == nombre:
            list.append(i)
            return list
        i = i + 1
def buscar_producto(productos,nombre): 
    for producto in productos:
        if producto.nombre.lower() == nombre:
            return producto
