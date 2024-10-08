import time
import os
import random

def dibujarPantalla():
    os.system("cls")
    for i in range(96):
        print("=",end="")
    for i in range(2,6):
        print("\033["+ str(i) +";0H*")
        print("\033["+ str(i) +";96H|")
    for i in range(96):
        print("=",end="")
caballo1="A"
caballo2="B"
caballo3="C"
caballo4="D"
os.system("cls")
dibujarPantalla()
repetir=True
while repetir:
    #os.system("cls")
    caballo1= ("." * random.randint(1,4)) + caballo1
    caballo2= ("." * random.randint(1,4)) + caballo2
    caballo3= ("." * random.randint(1,4)) + caballo3
    caballo4= ("." * random.randint(1,4)) + caballo4

    print("\033[2;2H" + caballo1)
    print("\033[3;2H" + caballo2)
    print("\033[4;2H" + caballo3)
    print("\033[5;2H" + caballo4)
    time.sleep(0.5)
    if len(caballo1)>=94 or len(caballo2)>=94 or len(caballo3)>=94 or len(caballo4)>=94:
        repetir=False

lista_caballos=[]
caballo=[]
lista_caballos.append(len(caballo1))
lista_caballos.append(len(caballo2))
lista_caballos.append(len(caballo3))
lista_caballos.append(len(caballo4))
print("\033[10;0H")
print(f"caballo A {len(caballo1)}")
print(f"caballo B {len(caballo2)}")
print(f"caballo C {len(caballo3)}")
print(f"caballo D {len(caballo4)}")


