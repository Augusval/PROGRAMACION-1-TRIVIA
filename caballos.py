import random
import time 

import random
def crear_caballos(z):
    lista=[]
    for i in range(z):
        x = random.randint(1, 100)  #Random.randint Crea un numero aleatorio incluyendo a los numeros de los extremos
        lista.append(x)
    while x in lista: 
        lista.remove(x)
    return lista, lista[0], lista[1], lista[2], lista[3]

def muestra_caballos(x): #Listas 
    for i in range(len(x)):
        print("Caballo:",x[i])


"""
def formato_circuito():
def juego():
def tabla de posiciones(): 
"""

#Programa principal 
pozo = 0
z=5
apuesta= 10 
lista_caballos=[]
Lista_jugadores=[]
lista_caballos,c1,c2,c3,c4= crear_caballos(z)


print("El dia de hoy, en el hipodromo clandestino del profe de progra1, los caballos a apostar son:")
muestra_caballos(lista_caballos)
hay_apuestas=True

#print("A=",c1,"B=",c2,"D=",c3,"D=",c4)

while hay_apuestas: 
    jugador= input("Ingrese su nombre:")
    while jugador in Lista_jugadores:
        print("Usted ya aposto")
        jugador= input("Ingrese otro nombre:")

    Lista_jugadores.append(jugadores)
    apuesta= int("A que caballo quiere apostar:")
    if apuesta==c1:
        pozo+=apuesta