'''este codigo localiza un elemento dentro de un arreglo y te da su ubicacion'''
def buscar_producto(productos, nombre):
    list = []
    i=0
    for producto in productos:
        if producto.nombre == nombre:
            list.append(i)
            return list
        i = i + 1
def cambiar_precio(productos,nombre,precio,nuevo): 
      pass

