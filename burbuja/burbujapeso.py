"""ordena los productos por peso"""
def verificador_peso(productos):
    '''verifica que el arreglo este ordenado de menor a mayor'''
    tamano = len(productos)
    for i in range(tamano-1):
        for j in range(i+1,tamano):
            if productos[j].peso < productos[i].peso:
                burbuja_peso(productos)
                return True
def burbuja_peso(arreglo):
    '''ordena los numeros del arreglo'''
    tamano = len(arreglo)
    for i in range(tamano-1):
        for j in range(i+1,tamano):
            if arreglo[i].peso > arreglo[j].peso:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
