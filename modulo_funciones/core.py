import os
def equipo():
    n = ["Valentini Augusto, Jesus Quijada, Centurion G0nzalo, Leomagno Ernesto, Oksana Bernkhart, Luis Agustin Chen"]
    print(n)
    input('Presione enter para volver al menu... ')
    
def trivia_Formula():
    from preguntasFormula1 import jugar_trivia
    return input("Enter para volver al menu...")
def main():
    repetir = True
    while repetir:
        os.system("cls")
        print("->1. Equipos       .<------------")
        print("->2. Juego         .<------------")
        print("->3. Opcion 3      .<------------")
        print("->4. Opcion 4      .<------------")
        print("->5. Salir         .<------------")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                print("Opcion elegido 1.")
                equipo()
            elif opcion == 2:
                print("Opcion elegido 2.")
                trivia_Formula()
            elif opcion == 3:
                print("Opcion elegido 3.")
                input('Presione enter para continuar...')
            elif opcion == 4:
                print("Opcion elegido 4.")
                input('Presione enter para continuar...')
                
            elif opcion == 5:
                print("Chau mundo!")
                repetir = False
        except:
                print("Error")

if __name__ == "__main__":
    main()



