import json
import random
contenido = open("newtest.json","r") #sacar todas las tildes del json o da error
trivia=contenido.read()
contenido.close
arch=json.loads(trivia)



def SeleccionarPreguntas():  # pregunta cuantas preguntas responder y crea una lista de preguntas que no se repiten
    cantqst = 0
    choice = int(input("1 para 10 preguntas , 2 para 20 preguntas"))
    listarandpreguntas = []
    if  choice == 1:
        cantqst = 4  # 2 es para test debe ser 10
    elif choice ==2:
        cantqst=20
    for i in range (cantqst):
        rndqst = random.randint(1,4)   # 2 es para test debe ser 25 o variable para poder agregar preguntas
        while rndqst in listarandpreguntas:
            rndqst = random.randint(1,4)   # aca lo mismo
        listarandpreguntas.append(rndqst)
    print(listarandpreguntas)

    return(listarandpreguntas)

#MAIN
randomMode = False
continuar = True
while continuar:
    tema=int(input("ingrese 0 para formula, 2 para cine, 3 para futbol, 8 PARA RANDOM: "))
    listtema=["Formula","Futbol","Literatura"]  #agregar tematicas
    if tema ==8:
        randomMode = True
    else:
        select=listtema[tema]
    

    cantpreguntas = 10
    listapreguntas=SeleccionarPreguntas()

    for i in listapreguntas:
        
        qst = str(i)

        if randomMode == True:
            listtema=["Literatura","Futbol","Formula","Deporte General","Video Juegos","Autos","Ciencias Naturales","Cine"] #abria que agregar todas la categorias
            select=listtema[random.randint(0,1)] #1 es para test cambiar
            qst=str(random.randint(1,4)) #4 es para test cambiar a 25
        

        ans = arch[select][qst]["ans"]


        print(arch[select][qst]["qst"])
        print("A)", arch[select][qst]["a"])
        print("B)", arch[select][qst]["b"])
        print("C)", arch[select][qst]["c"])
        print("D)", arch[select][qst]["d"])
        pans=input("ingrese respuesta: ")
        if pans == ans:
            print("correcto")           
        else:
            print("incorrecto")
    
    play = int(input("1 seguir 2 terminar: "))
    if play==1:
        continuar = True
    elif play==2:
        continuar = False
    

