import random

def genera_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    """
    Genera una lista con n números enteros aleatorios en un rango dado,
    asegurando que no haya dos elementos consecutivos iguales.

    Parámetros:
    n (int): Número de elementos en la lista.
    minimo (int): Valor mínimo del rango (inclusive).
    maximo (int): Valor máximo del rango (inclusive).

    Devuelve:
    list[int]: Lista con n números enteros aleatorios.
    """
    res = []
    for i in range(n):
        numero = random.randint(minimo, maximo)
        if i > 0:   #es lo mismo q len(res) > 0
            while numero == res[-1]:   #para acceder al ultimo numero de la lista res
                numero = random.randint(minimo, maximo)
        res.append(numero)
    return res

def intercala_listas(lista1: list, lista2: list) -> list:
    """
    Intercala dos listas. Si una lista es mayor que la otra, los elementos sobrantes se añaden al final.

    Parámetros:
    lista1 (list): Primera lista.
    lista2 (list): Segunda lista.

    Devuelve:
    list: Lista resultante de intercalar las dos listas.
    """
    res = []
    for elem1, elem2 in zip(lista1, lista2):
        res.append(elem1)
        res.append(elem2)
    tam1 = len(lista1)
    tam2 = len(lista2)
    if tam1 > tam2:
        #lista1[tam2:]  # trozo q sobra de lista1
        res.extend(lista1[tam2:])
    elif tam1 < tam2:
        res.extend(lista2[tam1:])
    return res


def mezcla_ordenadas(lista1: list, lista2: list) -> list:
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    lista1 (list): Primera lista ordenada.
    lista2 (list): Segunda lista ordenada.

    Devuelve:
    list: Lista resultante de mezclar las dos listas ordenadas.
    """
    res = []
    i = 0  # posicion por la que vamos de lista 1
    j = 0  # posicion por la que vamos en lista 2
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            res.append(lista1[i])
            i += 1
        else:
            res.append(lista2[j])
            j += 1
    if i < len(lista1):   # aun quedaban elementos de lista1
        res.extend(lista1[i:])
    else:
        res.extend(lista2[j:])
    return res 


def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """ 
    hay_intercambio = True
    while hay_intercambio:
        hay_intercambio = False
        for i in range(len(lista) - 1):  # recorro los elemetnos consecutivos
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                hay_intercambio = True
    
        

def inserta_ordenado(lista_nombres: list[str], nombre: str) -> None:
    """
    Inserta un nombre en una lista de nombres manteniendo el orden (de menor a mayor longitud).
    Si la lista recibida no estuviera ordenada por longitud, la función no hace nada.

    Parámetros:
    lista_nombres (list[str]): Lista de nombres ordenada por longitud.
    nombre (str): Nombre a insertar.
    """
    # TODO: Implementa esta función
    pass

def busca_duplicados(lista: list) -> list:
    """
    Busca y devuelve una lista con los elementos duplicados en la lista recibida.

    Parámetros:
    lista (list): Lista en la que buscar duplicados.

    Devuelve:
    list: Lista con los elementos duplicados.
    """
    # TODO: Implementa esta función:
    # - usando count
    # - usando slicing y sin usar count
    pass