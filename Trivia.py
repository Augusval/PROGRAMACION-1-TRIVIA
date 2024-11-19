import json
import time
import random
import os
from difflib import SequenceMatcher
import modulo_funciones.core as imprimir

with open("Preguntas.json", "r", encoding="utf-8") as contenido:
    trivia = contenido.read()
arch = json.loads(trivia)
puntajes = open("puntajes.txt","a")

def shufflePreguntas(tema,cantidadpreguntas):  #crea una lista de preguntas que no se repiten
    listarandpreguntas = []
    listapreguntasentema = list(arch[tema].keys())
    random.shuffle(listapreguntasentema)
    listarandpreguntas = listapreguntasentema[:cantidadpreguntas]
    return(listarandpreguntas)

def seleccionarDificultad():
    dificultad = int(input("Ingrese la dificultad->"))
    while dificultad  <1 or dificultad >2:
        print(f"\033[91;1;22m{"Opcion invalida"}\033[0m")
        dificultad = int(input("Ingrese nuevamente la dificultad: "))  
    if dificultad == 1:
        multi = 1
        dificil=False
    elif dificultad==2:
        multi = 2
        dificil = True
    return dificil, multi


def seleccionarCantidadPreguntas():
    imprimir.cant_menu()
    choice= int(input("Ingrese su opcion->"))
    while choice<1 or choice>3:
        print(f"\033[91;1;22m{"Seleccione una opcion valida"}\033[0m")
        choice= int(input("Ingrese su opcion->"))
    if  choice == 1:
        cantpreguntas = 6
        os.system("cls")
    elif choice ==2:
        cantpreguntas=10
        os.system("cls")
    elif choice ==3:
        cantpreguntas=20
        os.system("cls")
    return cantpreguntas


def crearpreguntas():
    imprimir.trivias()
    seleccion = int(input("Ingrese que tema quiere agregar una pregunta->"))
    listtema=list(arch.keys())
    tema = listtema[seleccion]
    cantpreguntas =  len(list(arch["Literatura"].keys()))
    nuevonumero = cantpreguntas + 1 
    nuevonumero= str(nuevonumero)
    pregunta = input("Ingrese Pregunta: ")
    opA = input("Ingrese Opcion A: ")
    opB = input("Ingrese Opcion B: ")
    opC = input("Ingrese Opcion C: ")
    opD = input("Ingrese Opcion D: ")
    respuesta = input("Ingrese Opcion Correcta: ")

    print("tu pregunta seria: ","\n" 
            "pregunt: ",pregunta,"\n"
            "A)",opA,"\n"
            "B)",opB,"\n"
            "C)",opC,"\n"
            "D)",opD,"\n"
            "Respuesta", respuesta)
    
    opcion = int(input("Desea continuar si: 1 / no: 2"))
    if opcion == 1:
        newpregunta ={nuevonumero:{"qst":pregunta,
                                     "a":opA,
                                     "b":opB,
                                     "c":opC,
                                     "d":opD,
                                     "ans":respuesta}} 
        arch[tema].update(newpregunta)
        with open("Preguntas.json", "w", encoding="utf-8") as agregar:
            json.dump(arch,agregar,indent=4)
        print("pregunta guardada")
    else:
        pass
    

def agregarpuntaje(puntajejuego): 
    print("Su puntaje es:", puntajejuego)
    save = int(input("¿Desea guardar su puntaje? 1 - Sí / 2 - No: "))
    if save == 1:
        puntajejuego = str(puntajejuego)
        name = input("Ingrese su nombre en 4 letras: ")
        namelen = list(name)
        while len(namelen) > 4:
            print(f"\033[91;1;22m{"Nombre inválido..."}\033[0m")
            name = input("Ingrese su nombre en 4 letras")
            namelen = list(name)
        
        # Agrega el nuevo puntaje al archivo
        with open("puntajes.txt", "a") as puntajes:
            puntajes.write(name + " " + puntajejuego + "\n")
        
        # Ordenar los puntajes después de agregar el nuevo puntaje
        ordenar_puntajes()
    else:
        pass

def ordenar_puntajes():
    # Leer todos los puntajes del archivo
    with open("puntajes.txt", "r") as archivo:
        puntajes = []
        for linea in archivo:
            nombre, puntaje = linea.split()
            puntajes.append((nombre, int(puntaje)))

    # Ordenar la lista de puntajes de mayor a menor
    puntajes_ordenados = sorted(puntajes, key=lambda x: x[1], reverse=True)

    # Sobrescribir el archivo con los puntajes ordenados
    with open("puntajes.txt", "w") as archivo:
        for nombre, puntaje in puntajes_ordenados:
            archivo.write(f"{nombre} {puntaje}\n")

    print("Puntajes ordenados y guardados en 'puntajes.txt'.")

def listapuntajes():
    imprimir.puntajes()
    with open("puntajes.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())

def maingame(versus):
    continuar = True
    while continuar:
        puntaje = 0
        puntajeJugador1=0
        puntajeJugador2=0
        randomMode = False
        if versus == False:
            turno=0
        imprimir.selectdificultad()
        dificil , multi = seleccionarDificultad()
        imprimir.trivias()

        temaelegido=int(input(f"\033[96;1;22m{"Seleccione el tema que desea o -1 para volver: -> "}\033[0m"))
        if temaelegido == -1:
            mainmenu()
        while temaelegido < 0 or temaelegido >10:
            temaelegido = int(input(f"\033[91;1;22m{"Ingrese un valor valido: "}\033[0m"))
        
        listtema=list(arch.keys())

        cantidadseleccionada = seleccionarCantidadPreguntas()
        if temaelegido==10:
            randomMode = True
            listapreguntas=[]
            for i in range(cantidadseleccionada):
                listapreguntas.append(" ")    
        else:
            tema=listtema[temaelegido]
            listapreguntas=shufflePreguntas(tema,cantidadseleccionada)
               
        turno=1
        imprimir.temasascii(temaelegido)
        imprimir.borde2()
        for i in listapreguntas:
            qst = str(i)
            
            if randomMode == True: 
                tema=listtema[random.randint(0,9)]
                listapreguntasentema = list(arch[tema].keys())
                qst=str(random.choice(listapreguntasentema)) 
                print(f"\033[91;1;22m{tema}\033[0m")
            
            #en dificil busca la respuesta y la guarda como texto
            if dificil ==True: 
                answer = arch[tema][qst]["ans"] 
                ans = arch[tema][qst][answer]

            else: #guarda la respuesta
                ans = arch[tema][qst]["ans"]
            
            
            if versus==True and turno%2==0:
                print(f"\033[94;1;22m{"Pregunta del jugador 2"}\033[0m")
                
            elif versus==True and turno%2!=0:
                print(f"\033[94;1;22m{"Pregunta del jugador 1"}\033[0m")
                
        
            print(arch[tema][qst]["qst"])
            if dificil == False:  
                print("A)", arch[tema][qst]["a"])
                print("B)", arch[tema][qst]["b"])
                print("C)", arch[tema][qst]["c"])
                print("D)", arch[tema][qst]["d"])
            pans=input("ingrese respuesta: ")

            if dificil: 
                print(SequenceMatcher(None, ans, pans).ratio())
                
            #esto es para modo normal
            if (pans == ans or (dificil and SequenceMatcher(None, ans, pans).ratio() >= 0.60)) and versus ==False:
                print(f"\033[92;1;22m{"Correcto"}\033[0m")
                puntaje = puntaje + 100*multi
                print("tu puntaje es", puntaje)           
            elif versus==False:
                print(f"\033[91;1;22m{"Incorrecto"}\033[0m")
                print("tu puntaje es", puntaje)
            
            #esto es para modo versus
            if (pans == ans or (dificil and SequenceMatcher(None, ans, pans).ratio() >= 0.60)) and versus ==True:
                if turno%2!=0:
                    print(f"\033[92;1;22m{"correcto jugador 1"}\033[0m")
                    puntajeJugador1 = puntajeJugador1 + 100*multi
                    print("tu puntaje es", puntajeJugador1)
                elif turno%2==0:
                    print((f"\033[92;1;22m{"correcto jugador 2"}\033[0m"))
                    puntajeJugador2 = puntajeJugador2 + 100*multi
                    print("tu puntaje es", puntajeJugador2)
            elif versus==True:
                print(f"\033[91;1;22m{"Incorrecto"}\033[0m")
                print("tu puntaje es: ",puntajeJugador1 if turno%2!=0 else puntajeJugador2) #no probado
            turno = turno+1
            print("\n")

        #en normal pregunta si quiere guardar, en versus dice quien gana
        if versus == False:    
            agregarpuntaje(puntaje)
        elif versus == True:
            if puntajeJugador1>puntajeJugador2:
                g=("Ganador jugador 1")
            elif puntajeJugador1<puntajeJugador2:
                g=("Ganador jugador 2")
            elif puntajeJugador1==puntajeJugador2:
                g=("Empate")

            imprimir.versus(g)
            
        play = int(input("Ingrese su opción->"))
        if play==1:
            continuar = True
        elif play==2:
            mainmenu()

def mainmenu():
    entra = True
    while entra:
        imprimir.menu()
        try:
            opcion_menu = int(input(f"\033[96;1;22m{"Ingrese su opción-> "}\033[0m"))
            if opcion_menu == 1:
                imprimir.modo()
                opcion_menumodo = int(input(f"\033[96;1;22m{"Ingrese su opción-> "}\033[0m"))
                if opcion_menumodo == 1:
                    versus=False
                    maingame(versus)
                elif opcion_menumodo ==2:
                    versus=True
                    maingame(versus)
                elif opcion_menumodo ==3:
                    entra = False
                    print("Enter para volver al menu")
            elif opcion_menu == 2:
                crearpreguntas()
            elif opcion_menu == 4:
                imprimir.juegoinfo()
            elif opcion_menu == 3:
                ordenar_puntajes()
                listapuntajes()
                input('Presione enter para continuar...')
                os.system("cls")
            elif opcion_menu == 5:
                imprimir.equipos()
                input("Enter para continuar...")
            elif opcion_menu == 6:
                os.system("cls")
                print(f"\033[91;1;22m{"Cerrando..."}\033[0m")
                time.sleep(2)
                entra= False
                imprimir.cierre()
        except:
            print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
            input("Enter para continuar...")

    


    

