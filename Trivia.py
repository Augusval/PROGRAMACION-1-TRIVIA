import json
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
    
    print(listarandpreguntas) #borrar despues

    return(listarandpreguntas)

def seleccionarDificultad():
    dificultad = int(input("ingrese dificultad 1 Normal /  2 Dificil(sin opciones): "))
    while dificultad  <1 or dificultad >2:
        print("ingrese una opcion valida")
        dificultad = int(input("ingrese dificultad 1 Normal /  2 Dificil(sin opciones): "))  
        
    if dificultad == 1:
        multi = 1
        dificil=False
    elif dificultad==2:
        multi = 2
        dificil = True
    return dificil, multi


def seleccionarCantidadPreguntas():
    
    choice= int(input("seleccione numero de preguntas 1para6 , 2para10 , 3para20"))
    while choice<1 or choice>3:
        print("seleccione una opcion valida")
        choice= int(input("seleccione numero de preguntas 1 para6 , 2 para10 , 3 para20"))

    if  choice == 1:
        cantqst = 6  
    elif choice ==2:
        cantqst=10
    elif choice ==3:
        cantqst=20
    
    return cantqst


def crearpreguntas():  
    seleccion = int(input("De que tema quiere agregar una pregunta: 0Csnat , 1Literatura, 2Fromula, 3DeporteGral, 4Autos, 5cine, 6futbol, 7culturagral, 8videojuegos, 9animales, 10 PARA RANDOM: "))
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
    
    opcion = int(input("desea continuar si: 1 / no: 2"))
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
    print("su puntaje es: ",puntajejuego)

    save = int(input("desea guardar su puntaje 1 si // 2 no: "))
    if save == 1:
        puntajejuego = str(puntajejuego)
        name = input("Ingrese su nombre en 4 letras: ")
        namelen = list(name)
        while len(namelen) >4:
            print("nombre invalido")
            name = input("Ingrese su nombre en 4 letras")
            namelen = list(name)
        puntajes.write(name+" "+puntajejuego)
        puntajes.write("\n") 
    else:
        pass

def maingame(versus):
    continuar = True
    while continuar:

        puntaje = 0
        puntajeJugador1=0
        puntajeJugador2=0
        randomMode = False

        imprimir.selectdificultad()
        dificil , multi = seleccionarDificultad()
    
        imprimir.trivias()

        tema=int(input("seleccione el tema que desea o -1 para volver: "))
        if tema == -1:
            imprimir.menu()
        while tema < 0 or tema >10:
            tema = int(input("Ingrese un valor valido: "))
        
        listtema=list(arch.keys())

        cantidadseleccionada = seleccionarCantidadPreguntas()
  
        if tema==10:
            randomMode = True
            listapreguntas=[]
            for i in range(cantidadseleccionada):
                listapreguntas.append(" ")    
        else:
            select=listtema[tema]
            listapreguntas=shufflePreguntas(select,cantidadseleccionada)
            
                 

        for i in listapreguntas:
            qst = str(i)
            
            if randomMode == True: #modorandom cada iteracion elige tema random y pregunta random
                select=listtema[random.randint(0,9)]
                tema=select
                listapreguntasentema = list(arch[tema].keys())
                qst=str(random.choice(listapreguntasentema)) 
                print(select)
            

            #en dificil busca la respuesta y la guarda como texto
            if dificil ==True: 
                answer = arch[select][qst]["ans"] 
                ans = arch[select][qst][answer]

            else: #guarda la respuesta
                ans = arch[select][qst]["ans"]
            
            if versus==True and (i+1)%2==0:
                print("Pregunta del jugador 2")
                turno = 2
            elif versus==True and (i+1)%2!=0:
                print("Pregunta del jugador 1")
                turno = 1

            print(arch[select][qst]["qst"])
            if dificil != True:   #en dificl no imprime
                print("A)", arch[select][qst]["a"])
                print("B)", arch[select][qst]["b"])
                print("C)", arch[select][qst]["c"])
                print("D)", arch[select][qst]["d"])
            pans=input("ingrese respuesta: ")

            if dificil: #esto es para probar
                print(SequenceMatcher(None, ans, pans).ratio())
                
            #esto es para modo normal
            if pans == ans or (dificil and SequenceMatcher(None, ans, pans).ratio() >= 0.60) and versus ==False:
                print("correcto")
                puntaje = puntaje + 100*multi
                print("tu puntaje es", puntaje)           
            else:
                print("incorrecto")
                print("tu puntaje es", puntaje)
            
            #esto es para modo versus
            if pans == ans or (dificil and SequenceMatcher(None, ans, pans).ratio() >= 0.60) and versus ==True:
                if turno == 1:
                    print("correcto jugador 1")
                    puntajeJugador1 = puntajeJugador1 + 100*multi
                    print("tu puntaje es", puntajeJugador1)
                elif turno ==2:
                    print("correcto")
                    puntajeJugador2 = puntajeJugador2 + 100*multi
                    print("tu puntaje es", puntajeJugador2)
            else:
                print("incorrecto")
                print("tu puntaje es: ",puntajeJugador1 if turno == 1 else puntajeJugador2) #no probado

        if versus == False:    
            agregarpuntaje(puntaje)
            
        play = int(input("1 volver a jugar / 2volver al menu: "))
        if play==1:
            continuar = True
        elif play==2:
            continuar = False
    imprimir.menu()
        
'''
MAIN
'''
imprimir.menu()
try:
        opcion_menu = int(input("Ingrese opción_menu: "))
        if opcion_menu == 1:
            imprimir.modo()
            opcion_menumodo = int(input("Ingrese opción_menu: "))
            if opcion_menumodo == 1:
                versus=False
                maingame(versus)
            elif opcion_menumodo ==2:
                versus=True
                maingame(versus)
        elif opcion_menu == 2:
            crearpreguntas()
        elif opcion_menu == 4:
            imprimir.juegoinfo()
        elif opcion_menu == 3:
            print("Funcion de puntajes.")
            input('Presione enter para continuar...')
            os.system("cls")
        elif opcion_menu == 5:
            imprimir.equipos()
        elif opcion_menu == 6:
            print("Cerrando...")
            #time.sleep(2)
except:
    print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
    #return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")


#maingame()
#crearpreguntas()


    


    

