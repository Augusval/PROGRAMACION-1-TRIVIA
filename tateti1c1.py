import random
tablero = [" " for i in range(9)]
def imprimirtablero():
    fila1= "|{}|{}|{}|".format(tablero[0],tablero[1],tablero[2])
    fila2= "|{}|{}|{}|".format(tablero[3],tablero[4],tablero[5])
    fila3= "|{}|{}|{}|".format(tablero[6],tablero[7],tablero[8])

    print(fila1)
    print(fila2)
    print(fila3)

def movimientos_jugador(forma,j1, j2):
    if forma == "X":
        numero=j1
    elif forma == "O":
        numero=j2

    print("Turno del jugador {}" .format(numero))
    try:
        eleccion = int(input("Ingrese su movimiento (1-9): ").strip())
        if tablero[eleccion - 1] == " ":
            tablero[eleccion - 1] = forma
        else:
            print("\nEste espacio se encuentra ocupado\n")
    except:
        print("Usted no ingresó un número válido. Por favor, intente de nuevo.")

   
def es_victoria(forma):
    if  (tablero[0] == forma and tablero[1] == forma and tablero[2] == forma) or \
        (tablero[3] == forma and tablero[4] == forma and tablero[5] == forma) or \
        (tablero[6] == forma and tablero[7] == forma and tablero[8] == forma) or \
        (tablero[0] == forma and tablero[3] == forma and tablero[6] == forma) or \
        (tablero[1] == forma and tablero[4] == forma and tablero[7] == forma) or \
        (tablero[2] == forma and tablero[5] == forma and tablero[8] == forma) or \
        (tablero[0] == forma and tablero[4] == forma and tablero[8] == forma) or \
        (tablero[2] == forma and tablero[4] == forma and tablero[6] == forma):
        return True
    else:
        return False

#programa principal 
j1=str(input("Ingrese el primer jugador:"))
j2=str(input("Ingrese el segundo jugador:"))
juego_terminado = False
while not juego_terminado: 
    imprimirtablero()
    movimientos_jugador("X",j1,j2)
    imprimirtablero()
    if es_victoria("X"):
        print("El jugador %s gano!" %j1)
        imprimirtablero()
        juego_terminado = True
    elif  " " not in tablero:
        print ("Empate")
        juego_terminado = True
    else:
        movimientos_jugador("O", j1 , j2)
        if es_victoria("O"):
            print("El jugador %s gano!" %j2)
            imprimirtablero()
            juego_terminado = True