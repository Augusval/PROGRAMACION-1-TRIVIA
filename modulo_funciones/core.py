import os
def equipo():
    n = ["Grupo conformador por: Valentini Augusto, Jesus Quijada, Centurion G0nzalo, Leomagno Ernesto, Oksana Bernkhart, Luis Agustin Chen."]
    print(n)
    print()
    input('Presione enter para volver al menu... ')
    
def trivias():
    print("====================================================")
    print("=        ¡Bienvenido al menu de las trivias!       =")
    print("====================================================")
    print("->      1. Trivia Formula 1                      .<-")
    print("->      2. Trivia Cine                           .<-")
    print("->      3. Trivia Futbol                         .<-")
    print("->      4. Trivia Deporte General                .<-")
    print("->      5. Trivia Video Juegos                   .<-")
    print("====================================================")
    print("=                    JUEGO                         =")
    print("====================================================")
    trivia = int(input("Ingrese opcion de trivia o enter para volver al menu: "))
    if trivia == 1:
        print("======[Bienvenido trivia del Formula 1]======")
        from preguntasFormula1 import jugar_trivia
    elif trivia == 2:
        print("======[Bienvenido trivia del Cine]======")
        from preguntasCine import jugar_trivia
    elif trivia == 3:
        print("======[Bienvenido trivia del Futbol]======")
        from preguntasFutbol import jugar_trivia
    elif trivia == 4:
        print("======[Bienvenido trivia del Deporte General]======")
        from preguntasDeporteGral import jugar_trivia
    elif trivia == 5:
        print("======[Bienvenido trivia del Video Juegos]======")
        from preguntasVideojuegos import jugar_trivia
    else:
        return input("Enter para volver al menu...")
    
def main():
    repetir = True
    while repetir:
        os.system("cls")
        print("===========================================================================================================")
        print("=                    ¡Bienvenido al menu elija alguna de las opciones!                                    =")
        print("===========================================================================================================")
        print("------->          1.  Juego Trivia                                                           .<------------")
        print("------->          2.  Sobre nosotros                                                         .<------------")
        print("------->          3.  Posiciones                                                             .<------------")
        print("------->          4.  Salir                                                                  .<------------")
        print("===========================================================================================================")
        print("=                                          MENU                                                           =")
        print("===========================================================================================================")
        print("Valentini Augusto, Jesus Quijada, Centurion G0nzalo, Leomagno Ernesto, Oksana Bernkhart, Luis Agustin Chen.")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                trivias()
            elif opcion == 2:
                print("Funcion sobre el juego.")
                input('Presione enter para continuar...')
            elif opcion == 3:
                print("Funcion de puntajes.")
                input('Presione enter para continuar...')
            elif opcion == 4:
                print("Cerrando...")
                repetir = False
        except:
                print("Formato ingresado no aceptado...")
                input("Enter para continuar...")
if __name__ == "__main__":
    main()



