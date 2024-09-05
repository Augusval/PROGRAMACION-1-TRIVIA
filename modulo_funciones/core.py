import os
def equipos():
    print("==================================")
    print("=           EQUIPOS              =")
    print("==================================")
    n = ("---> Valentini Augusto\n --->Jesus Quijada\n --->Centurion G0nzalo\n --->Leomagno Ernesto\n --->Oksana Bernkhart\n --->Luis Agustin Chen")
    print("Equipos conformados por: \n" ,n)
    input("Enter para continuar...")
def juegoinfo():
    print("\n'El trivia'\n Es un juego interactivo de preguntas y respuestas que ofrece a los jugadores una experiencia desafiante y educativa.\n Gracias a una amplia gama de temas y niveles de dificultad, diseñadas para jugadores de todas las edades. \n Este juego combina elementos de competencia y aprendizaje, permitiendo a los usuarios probar y ampliar sus conocimientos en diversas áreas")
    print(" ")
    input("Enter para continuar...")
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
        print()
        print("======[Bienvenido trivia del Formula 1]======")
        print()
        from preguntasFormula1 import jugar_trivia
    elif trivia == 2:
        print()
        print("======[Bienvenido trivia del Cine]======")
        print()
        from preguntasCine import jugar_trivia
    elif trivia == 3:
        print()
        print("======[Bienvenido trivia del Futbol]======")
        print()
        from preguntasFutbol import jugar_trivia
    elif trivia == 4:
        print()
        print("======[Bienvenido trivia del Deporte General]======")
        print()
        from preguntasDeporteGral import jugar_trivia
    elif trivia == 5:
        print()
        print("======[Bienvenido trivia del Video Juegos]======")
        print()
        from preguntasVideojuegos import jugar_trivia
    else:
        return input("Enter para volver al menu...")
    
def main():
    repetir = True
    while repetir:
        os.system("cls")
        print("============================================================================================")
        print("=                 ¡Bienvenido al menu elija alguna de las opciones!                        =")
        print("============================================================================================")
        print("------->          1.  Juego Trivia                                            .<------------")
        print("------->          2.  Sobre nosotros                                          .<------------")
        print("------->          3.  Posiciones                                              .<------------")
        print("------->          4.  Equipo                                                  .<------------")
        print("------->          5.  Salir                                                   .<------------")
        print("============================================================================================")
        print("=                                          MENU                                            =")
        print("============================================================================================")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                trivias()
            elif opcion == 2:
                juegoinfo()
            elif opcion == 3:
                print("Funcion de puntajes.")
                input('Presione enter para continuar...')
            elif opcion == 4:
                equipos()
            elif opcion == 5:
                print("Cerrando...")
                repetir = False
        except:
                print("Formato ingresado no aceptado...")
                input("Enter para continuar...")
if __name__ == "__main__":
    main()



