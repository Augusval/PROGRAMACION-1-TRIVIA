import json
import random
import os
from difflib import SequenceMatcher
import modulo_funciones.core as imprimir

with open("Preguntas.json", "r", encoding="utf-8") as contenido:
    trivia = contenido.read()
arch = json.loads(trivia)


puntajes = open("puntajes.txt","a")



def SeleccionarPreguntas(tema, esRandom):  # pregunta cuantas preguntas responder y crea una lista de preguntas que no se repiten
    cantqst = 0
    choice = int(input("1 para 5 preguntas , 2 para 10 preguntas, 3 para 20 preguntas: "))
    listarandpreguntas = []
    
    if  choice == 1:
        cantqst = 5  
    elif choice ==2:
        cantqst=10
    elif choice ==3:
        cantqst=20
    
    if esRandom == True:
        for i in range(cantqst):
            listarandpreguntas.append(" ")

    else:
        listapreguntasentema = list(arch[tema].keys())
        random.shuffle(listapreguntasentema)
        listarandpreguntas = listapreguntasentema[:cantqst] 
    
    
    
    print(listarandpreguntas)

    return(listarandpreguntas)

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
        while len(namelen) !=4:
            print("nombre invalido")
            name = input("Ingrese su nombre en 4 letras")
            namelen = list(name)
        puntajes.write(name+" "+puntajejuego)
        puntajes.write("\n") 
    else:
        pass

def maingame():

    randomMode = False
    continuar = True
    puntaje = 0

    

    imprimir.selectdificultad()

    dificultad = int(input("ingrese dificultad 1 Normal /  2 Dificil(sin opciones): "))  
    if dificultad == 1:
        multi = 1
        dificil=False
    elif dificultad==2:
        multi = 2
        dificil = True
    


    while continuar:

        imprimir.trivias()

        tema=int(input("seleccione el tema que desea: "))
        listtema=list(arch.keys())
        

        if tema !=10:
            select=listtema[tema]
            rand = False
            listapreguntas=SeleccionarPreguntas(select,rand)
            
            
        elif tema==10:
            randomMode = True
            rand = True
            select = " "
            listapreguntas=SeleccionarPreguntas(select,rand)
            
                 

        for i in listapreguntas:
            qst = str(i)
            
            if randomMode == True: #modorandom cada iteracion elige tema random y pregunta random
                listtema=list(arch.keys()) 
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
            
            
            print(arch[select][qst]["qst"])
            if dificil != True:   #en dificl no imprime
                print("A)", arch[select][qst]["a"])
                print("B)", arch[select][qst]["b"])
                print("C)", arch[select][qst]["c"])
                print("D)", arch[select][qst]["d"])
            pans=input("ingrese respuesta: ")

            if dificil: #esto es para probar
                print(SequenceMatcher(None, ans, pans).ratio())
                
            
            if pans == ans or (dificil and SequenceMatcher(None, ans, pans).ratio() >= 0.60):
                print("correcto")
                puntaje = puntaje + 100*multi
                print("tu puntaje es", puntaje)           
            else:
                print("incorrecto")
                print("tu puntaje es", puntaje)

        agregarpuntaje(puntaje)
            
        play = int(input("1 volver a jugar / 2volver al menu: "))
        if play==1:
            continuar = True
        elif play==2:
            continuar = False
        

imprimir.menu()
try:
        opcion_menu = int(input("Ingrese opción_menu: "))
        if opcion_menu == 1:
            imprimir.modo()
            opcion_menumodo = int(input("Ingrese opción_menu: "))
            if opcion_menumodo == 1:
                maingame()
            elif opcion_menumodo ==2:
                pass
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


    


    

