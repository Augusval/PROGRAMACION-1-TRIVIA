import json
import random
contenido = open("test.json","r")
trivia=contenido.read()
contenido.close
arch=json.loads(trivia)
select=""
continuar = True
while continuar:
    tema=int(input("ingrese 1 para geografia o 2 para historia: "))
    if tema==1:
        select="Geografia"
    elif tema==2:
        select="Historia"
    rand = str(random.randint(1,2))

    ans = arch[select][rand]["ans"] 
    print(ans)

    print(arch[select][rand]["qst"])
    print("A)", arch[select][rand]["a"])
    print("B)", arch[select][rand]["b"])
    print("C)", arch[select][rand]["c"])
    print("D)", arch[select][rand]["d"])
    pans=input("ingrese respuesta: ")
    if pans == ans:
        print("correcto")
    
    play = int(input("1seguir 2terminar: "))
    if play==1:
        continuar = True
    elif play==2:
        continuar = False
    

