def tablero(nombre_fichero, n):
    ''' Función que muestra por pantalla el tablero n de una partida de ajedrez. 

    Parámetros:
        - nombre_fichero: Es una cadena con el nombre del fichero que contiene la sucesión de tableros de la partida de ajedrez.
        - n: Es un entero con el número del tablero que se tiene que mostrar.
    '''

    f = open(nombre_fichero, 'r')
    tableros = f.read().split('\n')
    for i in tableros[n*9:n*9+8]:
        print(i)
    return

tablero('partida1.txt', 2)