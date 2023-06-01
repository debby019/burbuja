'''ordena por las piezas del producto'''
def verificador_cantidad(productos):
    '''verifica que el arreglo este ordenado de menor a mayor'''
    n = len(productos)
    for i in range(n-1):
        for j in range(i+1,n):
            if productos[j].cantidad < productos[i].cantidad:
                burbuja_cantidad(productos)
                return True
def burbuja_cantidad(arreglo):
    '''ordena los numeros del arreglo'''
    n = len(arreglo)
    for i in range(n-1):
        for j in range(i+1,n):
            if arreglo[i].cantidad > arreglo[j].cantidad:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
