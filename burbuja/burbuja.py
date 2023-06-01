"""Ordena los productos por precios"""
def verificador_precio(productos):
    '''verifica que el arreglo este ordenado de menor a mayor'''
    tamano = len(productos)
    for i in range(tamano-1):
        for j in range(i+1,tamano):
            if productos[j].precio < productos[i].precio:
                burbuja_precio(productos)
                return True
def burbuja_precio(arreglo):
    '''ordena los numeros del arreglo'''
    tamano = len(arreglo)
    for i in range(tamano-1):
        for j in range(i+1,tamano):
            if arreglo[i].precio > arreglo[j].precio:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
