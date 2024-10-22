import json
import random
with open("Preguntas.json", "r", encoding="utf-8") as contenido: #para que no de error
    trivia = contenido.read()
arch = json.loads(trivia)

puntajes = open("puntajes.txt","a")



def SeleccionarPreguntas():  # pregunta cuantas preguntas responder y crea una lista de preguntas que no se repiten
    cantqst = 0
    choice = int(input("1 para 5 preguntas , 2 para 10 preguntas, 3 para 20 preguntas"))
    listarandpreguntas = []
    if  choice == 1:
        cantqst = 5  
    elif choice ==2:
        cantqst=10
    elif choice ==3:
        cantqst=20
    for i in range (cantqst):
        rndqst = random.randint(1,24)   # 24 por variable para poder agregar preguntas
        while rndqst in listarandpreguntas:
            rndqst = random.randint(1,24)   
        listarandpreguntas.append(rndqst)
    print(listarandpreguntas)

    return(listarandpreguntas)

def crearpreguntas():  #incompleto
    seleccion = int(input("ingrese tema: "))
    listtema=["Literatura","Futbol","Formula","Deporte General","Video Juegos","Autos","Ciencias Naturales","Cine"]
    tema =listtema[seleccion]
    cantpreguntastema = int(arch[tema]["cant"])
    cantpreguntas =+1 # falta que los escriba en el archivo (lo de abajo tambien)
    #arch[tema]["cant"] = string(cantpreguntas)
    input("Ingrese Pregunta: ")
    input("Ingrese Opcion A: ")
    input("Ingrese Opcion B: ")
    input("Ingrese Opcion C: ")
    input("Ingrese Opcion D: ")
    input("Ingrese Opcion Correcta: ")

def agregarpuntaje(puntajejuego): #incompleto
    save = int(input("desea guardar su puntaje 1 si // 2 no: "))
    if save == 1:
        puntajejuego = str(puntajejuego)
        name = input("Ingrese su nombre en 4 letras")
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
    while continuar:
        tema=int(input("0Lite , 1Futbol, 2Fromula, 3DeporteGral, 4Videojuegos 8 PARA RANDOM: "))
        listtema=["Literatura","Futbol","Formula","Deporte General","videoJuegos","Autos","Ciencias Naturales","Cine"]  #se puede hacer lisstema variable global para no llamarla dos veces

        if tema ==8:
            randomMode = True
        else:
            select=listtema[tema]
                
                
            

        listapreguntas=SeleccionarPreguntas()

        for i in listapreguntas:
            qst = str(i)
            #modorandom
            if randomMode == True:
                listtema=["Literatura","Futbol","Formula","Deporte General","Video Juegos","Autos","Ciencias Naturales","Cine"] 
                select=listtema[random.randint(0,8)] 
                qst=str(random.randint(1,24)) 

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
                puntaje=puntaje+100           
            else:
                print("incorrecto")
        agregarpuntaje(puntaje)
            
        play = int(input("1 seguir 2 terminar: "))
        if play==1:
            continuar = True
        elif play==2:
            continuar = False

#puntos = int(input("ingrese puntaje: ")) #probar ingreso de puntos
#agregarpuntaje(puntos)
maingame()


    


    

