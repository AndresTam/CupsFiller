#Importación de las librerias utilizadas
import random as rnd
import time

#--------Generación de las funciones--------#
    #---Función para imprimir el llenado de vasos
def printCups(colorsArray):
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
    for i in[0,1]:
        for x in[0,1,2]:
            if positions[i][x] != 0:
                if positions[i][x] == 1:
                    colors[i][x] = "Azul"
                else:
                    colors[i][x] = "Rojo"
            printCups(colors)
            time.sleep(1)

    #Función para iniciar el llenado de los vasos
def fillCups():
    print("El llenado de los vasos comenzará ahora.")
    colors = [
        ["    ","    ","    "],
        ["    ","    ","    "]
    ]
    printCups(colors)
    timeFiller(colors, randomPositions())
    exit()

    #---Función de inicio del juego
def startGame():
    selection = "1"
    print("Bienvenido al juego de llenado de vasos. \nPara iniciar introduce el número 1.")
    while selection != 1:
        selection = input()
        if selection != "1":
            print("Esa no es una opción en el sistema")
        else:
            fillCups()
    return 0;

startGame()