import json
import random
contenido = open("test.json","r")
trivia=contenido.read()
contenido.close
arch=json.loads(trivia)



def SeleccionarPreguntas():  # pregunta cuantas preguntas responder y crea una lista de preguntas que no se repiten
    cantqst = 0
    choice = int(input("1 para 10 preguntas , 2 para 20 preguntas"))
    listarandpreguntas = []
    if  choice == 1:
        cantqst = 2  # 2 es para testea debe ser 10
    elif choice ==2:
        cantqst=20
    for i in range (cantqst):
        rndqst = random.randint(1,2)   # 2 es para test debe ser 25 o variable para poder agregar preguntas
        while rndqst in listarandpreguntas:
            rndqst = random.randint(1,2)   # aca lo mismo
        listarandpreguntas.append(rndqst)
    print(listarandpreguntas)

    return(listarandpreguntas)

#MAIN
randomMode = False
continuar = True
while continuar:
    tema=int(input("ingrese 1 para Geografia, 2 para Historia, 3 PARA RANDOM: "))
    if tema==1:
        select="Geografia"
    elif tema==2:
        select="Historia"
    elif tema ==3:
        randomMode = True

    cantpreguntas = 10
    listapreguntas=SeleccionarPreguntas()

    for i in listapreguntas:
        
        qst = str(i)

        if randomMode == True:
            listtema=["Geografia","Historia"] #abria que agregar todas la categorias
            select=listtema[random.randint(0,1)] #1 es para test cambiar
            qst=str(random.randint(1,2))
        else:
            pass

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
    

