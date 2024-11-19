import json 
import time
"""
def temasascii(select):
    with open("temas.json", "r") as archivo:
        datos = json.load(archivo)
            
    # Acceso a una lista específica
    lista_especifica = datos[str(select)]["1"]

    # Imprimir la lista
    for elemento in lista_especifica:
        print(f"\033[36;1;22m{" "*8}{elemento}\033[0m")
        time.sleep(0.1)

select=1
temasascii(select)
"""

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


