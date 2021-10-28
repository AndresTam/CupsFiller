#Importación de las librerias utilizadas
import random as rnd  #Importa la libreria usada para generar numeros aleatorios
import time #Importa la libreria necesaria para trabajar el retardo del tiempo
import os #Importa la libreria necesaria para borrar la impresion en consola

#--------Generación de las funciones--------#
    #---Función para imprimir el llenado de vasos
def printCups(colorsArray):
    """
    Esta función sirve para poder imprimir los vasos dentro de la consola,
    poniendo cada color dentro de los mismos, guiandose por el arreglo donde
    se almacenaron previamente.
    """
    print(f"""
        |        |  |        |  |        |
        |________|  |________|  |________|
        |  {colorsArray[0][0]}  |  |  {colorsArray[0][1]}  |  |  {colorsArray[0][2]}  |
        |________|  |________|  |________|
        |  {colorsArray[1][0]}  |  |  {colorsArray[1][1]}  |  |  {colorsArray[1][2]}  |
        |________|  |________|  |________|
    """)

    #Función para generar la posoción aleatoriamente
def randomPositions():
    """
    Esta función sirve para generar las posiciones aleatoriamente de cada
    uno de los colores, al macenandola dentro de un arreglo propio, el cual
    tiene 2 filas y 3 columnas, esto para simular la posicion que tendrá
    dentro del vaso y poder almacenar los resultados dentro del arreglo de colores.
    """
    positions = [
        [0,0,0],
        [0,0,0]
    ]
    count1 = 0
    firstColor = 0;
    while count1 < 2:
        number2 = rnd.randrange(0,3)
        color = rnd.randrange(1,3)
        if positions[0][number2] == 0 and color != 0:
            if count1 < 2:
                if count1 == 0:
                    positions[0][number2] = color
                    firstColor = color
                    count1 = count1 + 1
                elif count1 > 0:
                    if color != firstColor:
                        positions[0][number2] = color
                        count1 = count1 + 1
    for i in range(3):
        if positions[0][i] == 1:
            positions[1][i] = 2
        elif positions[0][i] == 2:
            positions[1][i] = 1
    print(f"Primera {positions}")
    return positions

    #Función para llenar los vasos con retardo
def timeFiller(colors, positions):
    """
    Esta fucnión sirve para poder imprimir los colores de los vasos
    con un retardo de un segundo, aunque el tiempo puede ser cambiado
    a preferencia.
    """
    
    for i in[0,1]:
        for x in[0,1,2]:
            if positions[i][x] != 0:
                if positions[i][x] == 1:
                    colors[i][x] = "Azul"
                else:
                    colors[i][x] = "Rojo"
            clearConsole()
            printCups(colors)
            time.sleep(1)

    #Funcion para limpiar la consola
def clearConsole():
    """
    Esta fucnión sirve para limpiar la consola durante la ejecución
    del programa, manteniendo así una salida en consola más limpia
    y facil de entender.
    """
    command = "clear"
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

    #Función para iniciar el llenado de los vasos
def fillCups():
    """
    Esta funcion inicia el proceso de llenado de los vasos,
    llamando a funciones superiores para poder imprimir y
    realizar la logica para la generacion de numeros aleatorios.
    """
    print("El llenado de los vasos comenzará ahora.")
    colors = [
        ["    ","    ","    "],
        ["    ","    ","    "]
    ]
    printCups(colors)
    time.sleep(2)
    timeFiller(colors, randomPositions())

    #---Función de inicio del juego
def startGame():
    """
    Esta función sirve para dar inicio al programa de llenado,
    dentro de esta estan las opciones de inicio y finalización
    del sistema.
    """
    selection = ""
    print("Bienvenido al juego de llenado de vasos. \nPara iniciar introduce el número 1. \nPara salir introduce el numero 2.")
    while selection != "1":
        selection = input()
        if selection != "1" and selection != "2":
            print("Esa no es una opción en el sistema")
        elif selection == "2":
            print("Esa opción aun no está permitida")
        elif selection == "1":
            fillCups()
            while selection != "2":
                print("Para salir introduce el número 2.")
                selection = input()
                if selection == "2":
                    exit()
                else:
                    print("Esa no es una opción en el sistema")

    return 0;

startGame()