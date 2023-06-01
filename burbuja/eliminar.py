'''eliminar productos'''
def eliminar(arreglo, nombre):
    '''elimina el numero del arreglo'''
    espacio = len(arreglo)
    j=0
    for i in range(espacio-1):
        if arreglo[i].nombre.lower() == nombre:
            j = i + 1
            temp = arreglo[i]
            arreglo[i] = arreglo[j]
            arreglo[j] = temp
    nuevoarreglo =  arreglo[:espacio-1]
    return nuevoarreglo