'''Este codigo localiza un elemento dentro de un arreglo y te da su ubicacion'''
def localizar(productos, nombre):
    '''devuelve la posicion del producto'''
    list_localizar = []
    i=0
    for producto in productos:
        if producto.nombre.lower() == nombre:
            list_localizar.append(i)
            return list_localizar
        i = i + 1
def buscar_producto(productos,nombre):
    '''devuelve el producto'''
    for producto in productos:
        if producto.nombre.lower() == nombre:
            return producto
