import json
import random
with open("PROGRAMACION-1-PROYECTO/Preguntas.json", "r", encoding="utf-8") as contenido: #utf-8 permite caracteres especiales palabras con tilde (en el json se puede ver raro)
    trivia = contenido.read()
arch = json.loads(trivia)


puntajes = open("PROGRAMACION-1-PROYECTO/puntajes.txt","a")



def SeleccionarPreguntas(max):  # pregunta cuantas preguntas responder y crea una lista de preguntas que no se repiten
    cantqst = 0
    choice = int(input("1 para 5 preguntas , 2 para 10 preguntas, 3 para 20 preguntas: "))
    listarandpreguntas = []
    if  choice == 1:
        cantqst = 5  
    elif choice ==2:
        cantqst=10
    elif choice ==3:
        cantqst=20
    for i in range (cantqst):
        rndqst = random.randint(1,max)   #numero random entre 1 y el numero maximo de preguntas en el tema(para cuando se agreguen preguntas)
        while rndqst in listarandpreguntas:
            rndqst = random.randint(1,max)   
        listarandpreguntas.append(rndqst)
    print(listarandpreguntas)

    return(listarandpreguntas)

def crearpreguntas():  #esto anda por las dudas no usar todavia
    seleccion = int(input("ingrese tema 0Geografia, 1Historia "))
    listtema=["Literatura","Futbol","Formula","DeporteGeneral","videojuegos","Autos","CienciasNaturales","Cine","CulturaGral","Animales"]
    tema = listtema[seleccion]
    cantpreguntas = int(arch[tema]["cant"]) 
    cantpreguntas = cantpreguntas + 1 
    cantpreguntas= str(cantpreguntas)
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
        newpregunta ={cantpreguntas:{"qst":pregunta,
                                     "a":opA,
                                     "b":opB,
                                     "c":opC,
                                     "d":opD,
                                     "ans":respuesta}} 
        arch[tema]["cant"]=cantpreguntas
        arch[tema].update(newpregunta)
        with open("PROGRAMACION-1-PROYECTO/Preguntas.json", "w", encoding="utf-8") as agregar:
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


    dificultad = int(input("ingrese dificultad 1 Facil / 2 Medio / 3 Dificil: "))  #falta agregar media y dificil
    if dificultad == 1:
        multi = 1
    elif dificultad==2:  
        multi = 2
    elif dificultad==3:
        multi = 4


    while continuar:
        tema=int(input("0Literatura , 1Futbol, 2Fromula, 3DeporteGral, 4Videojuegos, 5autos, 6cienciasnaturales, 7cine, 8culturagral, 9animales, 10 PARA RANDOM: "))
        listtema=["Literatura","Futbol","Formula","DeporteGeneral","videojuegos","Autos","CienciasNaturales","Cine","CulturaGral","Animales"] #se puede hacer lisstema variable global para no llamarla dos veces

        if tema ==10:
            randomMode = True
            cantidadpreguntas = 25
        else:
            select=listtema[tema]
            cantidadpreguntas = int(arch[select]["cant"]) #cantidad maxima de preguntas en el tema
            
        listapreguntas=SeleccionarPreguntas(cantidadpreguntas)
                 

        for i in listapreguntas:
            qst = str(i)
            
            if randomMode == True: #modorandom
                listtema=["Literatura","Futbol","Formula","DeporteGeneral","videojuegos","Autos","CienciasNaturales","Cine","CulturaGral","Animales"] 
                select=listtema[random.randint(0,8)] 
                qst=str(random.randint(1,24)) 
                print(select)

            #guarda la respuesta
            ans = arch[select][qst]["ans"]

            
            print(arch[select][qst]["qst"])
            print("A)", arch[select][qst]["a"])
            print("B)", arch[select][qst]["b"])
            print("C)", arch[select][qst]["c"])
            print("D)", arch[select][qst]["d"])
            pans=input("ingrese respuesta: ")
            if pans == ans:
                print("correcto")
                puntaje = puntaje + 100*multi
                print("tu puntaje es", puntaje)           
            else:
                print("incorrecto")
                print("tu puntaje es", puntaje)

        agregarpuntaje(puntaje)
            
        play = int(input("1 seguir 2 terminar: "))
        if play==1:
            continuar = True
        elif play==2:
            continuar = False


maingame()


    


    

