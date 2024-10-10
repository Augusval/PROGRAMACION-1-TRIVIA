import os
def equipos():
    print("==================================")
    print("=           EQUIPOS              =")
    print("==================================")
    n = ("---> Valentini Augusto\n ---> Jesus Quijada\n ---> Centurion Gonzalo\n ---> Leomagno Ernesto\n ---> Oksana Bernkhart\n ---> Luis Agustin Chen")
    print("Equipos conformados por: \n" ,n)
    input("Enter para continuar...")
def juegoinfo():
    print("\n'El trivia'\n Es un juego interactivo de preguntas y respuestas que ofrece a los jugadores una experiencia desafiante y educativa.\n Gracias a una amplia gama de temas y niveles de dificultad, diseñadas para jugadores de todas las edades. \n Este juego combina elementos de competencia y aprendizaje, permitiendo a los usuarios probar y ampliar sus conocimientos en diversas áreas")
    print(" ")
    input("Enter para continuar...")
def trivias():
    os.system("cls")
    print("====================================================")
    print("=        ¡Bienvenido al menu de las trivias!       =")
    print("====================================================")
    print("->      1. Trivia Formula 1                      .<-")
    print("->      2. Trivia Cine                           .<-")
    print("->      3. Trivia Futbol                         .<-")
    print("->      4. Trivia Deporte General                .<-")
    print("->      5. Trivia Video Juegos                   .<-")
    print("->      6. Trivia Autos                          .<-")
    print("->      7. Trivia Ciencias Naturales             .<-")
    print("->      8. Trivia Cultura General                .<-")
    print("->      9. Trivia Animales                       .<-")
    print("->     10. Trivia Literatura                     .<-")
    print("====================================================")
    print("=                    JUEGO                         =")
    print("====================================================")
    trivia = int(input("Ingrese opcion de trivia o enter para volver al menu: "))
    if trivia == 1:
        print()
        print("======[Bienvenido trivia del Formula 1]======")
        print()
        from preguntas import Formula
        print("""
        $$$$$$$$\  $$$$$$\  $$$$$$$\  $$\      $$\ $$\   $$\ $$\       $$$$$$\        $$\   $$\ $$\   $$\  $$$$$$\  
        $$  _____|$$  __$$\ $$  __$$\ $$$\    $$$ |$$ |  $$ |$$ |     $$  __$$\       $$ |  $$ |$$$\  $$ |$$  __$$\ 
        $$ |      $$ /  $$ |$$ |  $$ |$$$$\  $$$$ |$$ |  $$ |$$ |     $$ /  $$ |      $$ |  $$ |$$$$\ $$ |$$ /  $$ |
        $$$$$\    $$ |  $$ |$$$$$$$  |$$\$$\$$ $$ |$$ |  $$ |$$ |     $$$$$$$$ |      $$ |  $$ |$$ $$\$$ |$$ |  $$ |
        $$  __|   $$ |  $$ |$$  __$$< $$ \$$$  $$ |$$ |  $$ |$$ |     $$  __$$ |      $$ |  $$ |$$ \$$$$ |$$ |  $$ |
        $$ |      $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |     $$ |  $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |
        $$ |       $$$$$$  |$$ |  $$ |$$ | \_/ $$ |\$$$$$$  |$$$$$$$$\$$ |  $$ |      \$$$$$$  |$$ | \$$ | $$$$$$  |
        \__|       \______/ \__|  \__|\__|     \__| \______/ \________\__|  \__|       \______/ \__|  \__| \______/ 
                                                                                                            
        """)
        Formula()
        input("Enter Para Continuar...")
    elif trivia == 2:
        print()
        print("======[Bienvenido trivia del Cine]======")
        print()
        from preguntas import Cine
        print("""
          /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$
         /$$__  $$|_  $$_/| $$$ | $$| $$_____/
        | $$  \__/  | $$  | $$$$| $$| $$      
        | $$        | $$  | $$ $$ $$| $$$$$   
        | $$        | $$  | $$  $$$$| $$__/   
        | $$    $$  | $$  | $$\  $$$| $$      
        |  $$$$$$/ /$$$$$$| $$ \  $$| $$$$$$$$
        \______/ |______/|__/  \__/|________/
                           
        """)
        Cine()
        input("Enter Para Continuar...")
    elif trivia == 3:
        print()
        print("======[Bienvenido trivia del Futbol]======")
        print()
        from preguntas import Futbol
        print("""
         /$$$$$$$$          /$$     /$$                 /$$
        | $$_____/         | $$    | $$                | $$
        | $$    /$$   /$$ /$$$$$$  | $$$$$$$   /$$$$$$ | $$
        | $$$$$| $$  | $$|_  $$_/  | $$__  $$ /$$__  $$| $$
        | $$__/| $$  | $$  | $$    | $$  \ $$| $$  \ $$| $$
        | $$   | $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$
        | $$   |  $$$$$$/  |  $$$$/| $$$$$$$/|  $$$$$$/| $$
        |__/    \______/    \___/  |_______/  \______/ |__/
                                                                                
        """)
        Futbol()
        input("Enter Para Continuar...")
    elif trivia == 4:
        print()
        print("======[Bienvenido trivia del Deporte General]======")
        print()
        from preguntas import DeporteGral
        print("""
         /$$$$$$$                                            /$$                      /$$$$$$                                                   /$$
        | $$__  $$                                          | $$                     /$$__  $$                                                 | $$
        | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ | $$
        | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$      | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$| $$
        | $$  | $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/  | $$    | $$$$$$$$      | $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$| $$
        | $$  | $$| $$_____/| $$  | $$| $$  | $$| $$        | $$ /$$| $$_____/      | $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$| $$
        | $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$        |  $$$$/|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$| $$
        |_______/  \_______/| $$____/  \______/ |__/         \___/   \_______/       \______/  \_______/|__/  |__/ \_______/|__/      \_______/|__/
                            | $$                                                                                                                   
                            | $$                                                                                                                   
                            |__/                                                                                                                   
        """)
        DeporteGral()
        input("Enter Para Continuar...")
    elif trivia == 5:
        print()
        print("======[Bienvenido trivia del Video Juegos]======")
        print()
        from preguntas import VideoJuegos
        print("""
         /$$    /$$ /$$       /$$                              /$$$$$                                                  
        | $$   | $$|__/      | $$                             |__  $$                                                  
        | $$   | $$ /$$  /$$$$$$$  /$$$$$$   /$$$$$$             | $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$
        |  $$ / $$/| $$ /$$__  $$ /$$__  $$ /$$__  $$            | $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/
        \  $$ $$/ | $$| $$  | $$| $$$$$$$$| $$  \ $$       /$$  | $$| $$  | $$| $$$$$$$$| $$  \ $$| $$  \ $$|  $$$$$$ 
         \  $$$/  | $$| $$  | $$| $$_____/| $$  | $$      | $$  | $$| $$  | $$| $$_____/| $$  | $$| $$  | $$ \____  $$
          \  $/   | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/      |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/ /$$$$$$$/
           \_/    |__/ \_______/ \_______/ \______/        \______/  \______/  \_______/ \____  $$ \______/ |_______/ 
                                                                                           /$$  \ $$                    
                                                                                           |  $$$$$$/                    
                                                                                            \______/                      
        """)
        VideoJuegos()
        input("Enter Para Continuar...")
    elif  trivia == 6:
        print()
        print("======[Bienvenido trivia de Autos]======")
        print()
        from preguntas import Auto
        print(""")
          /$$$$$$              /$$                        
         /$$__  $$            | $$                        
        | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$
        | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/
        | $$__  $$| $$  | $$  | $$    | $$  \ $$|  $$$$$$ 
        | $$  | $$| $$  | $$  | $$ /$$| $$  | $$ \____  $$
        | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/ /$$$$$$$/
        |__/  |__/ \______/    \___/   \______/ |_______/ 
                                                  
        """)
        Auto()
        input("Enter Para Continuar...")
    elif trivia == 7:
        print()
        print("======[Bienvenido trivia de Ciencias Naturales]======")
        print()
        from preguntas import CienNat
        print("""
             /$$$$$$  /$$                               /$$                           /$$   /$$             /$$                                  /$$                    
            /$$__  $$|__/                              |__/                          | $$$ | $$            | $$                                 | $$                    
            | $$  \__/ /$$  /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$$      | $$$$| $$  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$$
            | $$      | $$ /$$__  $$| $$__  $$ /$$_____/| $$ |____  $$ /$$_____/      | $$ $$ $$ |____  $$|_  $$_/  | $$  | $$ /$$__  $$|____  $$| $$ /$$__  $$ /$$_____/
            | $$      | $$| $$$$$$$$| $$  \ $$| $$      | $$  /$$$$$$$|  $$$$$$       | $$  $$$$  /$$$$$$$  | $$    | $$  | $$| $$  \__/ /$$$$$$$| $$| $$$$$$$$|  $$$$$$ 
            | $$    $$| $$| $$_____/| $$  | $$| $$      | $$ /$$__  $$ \____  $$      | $$\  $$$ /$$__  $$  | $$ /$$| $$  | $$| $$      /$$__  $$| $$| $$_____/ \____  $$
            |  $$$$$$/| $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/      | $$ \  $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$     |  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/
            \______/ |__/ \_______/|__/  |__/ \_______/|__/ \_______/|_______/       |__/  \__/ \_______/   \___/   \______/ |__/      \_______/|__/ \_______/|_______/                                                                                                                                       
              """)
        print()
        CienNat()
        input("Enter para continuar...")
    elif trivia == 8:
        print()
        print("======[Bienvenido trivia de Cultura General]======")
        print()
        from preguntas import CulGen
        print("""
                 /$$$$$$            /$$   /$$                                         /$$$$$$                                                   /$$
                /$$__  $$          | $$  | $$                                        /$$__  $$                                                 | $$
                | $$  \__/ /$$   /$$| $$ /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ | $$
                | $$      | $$  | $$| $$|_  $$_/  | $$  | $$ /$$__  $$|____  $$      | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$| $$
                | $$      | $$  | $$| $$  | $$    | $$  | $$| $$  \__/ /$$$$$$$      | $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$| $$
                | $$    $$| $$  | $$| $$  | $$ /$$| $$  | $$| $$      /$$__  $$      | $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$| $$
                |  $$$$$$/|  $$$$$$/| $$  |  $$$$/|  $$$$$$/| $$     |  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$| $$
                \______/  \______/ |__/   \___/   \______/ |__/      \_______/       \______/  \_______/|__/  |__/ \_______/|__/      \_______/|__/                                                                                                                                                                                                                                                        
         """)
        print()
        CulGen()
        input("Enter para continuar...")
    elif trivia == 9:
        print()
        print("======[Bienvenido trivia de Animales]======")
        print()
        from preguntas import animales
        print("""
                 /$$$$$$            /$$                         /$$                    
                /$$__  $$          |__/                        | $$                    
                | $$  \ $$ /$$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$$
                | $$$$$$$$| $$__  $$| $$| $$_  $$_  $$ |____  $$| $$ /$$__  $$ /$$_____/
                | $$__  $$| $$  \ $$| $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$$$$$$$|  $$$$$$ 
                | $$  | $$| $$  | $$| $$| $$ | $$ | $$ /$$__  $$| $$| $$_____/ \____  $$
                | $$  | $$| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/
                |__/  |__/|__/  |__/|__/|__/ |__/ |__/ \_______/|__/ \_______/|_______/                                                                                                                                                                                                                                         
            """)  
        print()
        animales()
        input("Enter para continuar...")
    elif trivia == 10:
        print()
        print("======[Bienvenido trivia de Literatura]======")
        print()
        from preguntas import Lite
        print("""
                 /$$       /$$   /$$                                    /$$                                 
                | $$      |__/  | $$                                   | $$                                 
                | $$       /$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$ 
                | $$      | $$|_  $$_/   /$$__  $$ /$$__  $$|____  $$|_  $$_/  | $$  | $$ /$$__  $$|____  $$
                | $$      | $$  | $$    | $$$$$$$$| $$  \__/ /$$$$$$$  | $$    | $$  | $$| $$  \__/ /$$$$$$$
                | $$      | $$  | $$ /$$| $$_____/| $$      /$$__  $$  | $$ /$$| $$  | $$| $$      /$$__  $$
                | $$$$$$$$| $$  |  $$$$/|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$     |  $$$$$$$
                |________/|__/   \___/   \_______/|__/      \_______/   \___/   \______/ |__/      \_______/
            """)
        print()
        Lite()
        input("Enter para continuar...")
    else:
        print("Error de ingreso...")
        return input("Enter para volver al menu...")

def menu():
    salir = False
    while not salir:
        os.system("cls")
        print("============================================================================================")
        print("=                 ¡Bienvenido al menu elija alguna de las opciones!                        =")
        print("============================================================================================")
        print("------->          1.  Juego Trivia                                            .<------------")
        print("------->          2.  Crear preguntas                                         .<------------")
        print("------->          3.  Puntajes                                                .<------------")
        print("------->          4.  Instrucciones                                           .<------------")
        print("------->          5.  Equipo                                                  .<------------")
        print("------->          6.  Salir                                                   .<------------")
        print("============================================================================================")
        print("=                                          MENU                                            =")
        print("============================================================================================")
        try:
            opcion_menu = int(input("Ingrese opción_menu: "))
            if opcion_menu == 1:
                modo()
            elif opcion_menu == 2:
                crear_preguntas()
            elif opcion_menu == 4:
                juegoinfo()
            elif opcion_menu == 3:
                print("Funcion de puntajes.")
                input('Presione enter para continuar...')
            elif opcion_menu == 5:
                equipos()
            elif opcion_menu == 6:
                print("Cerrando...")
                salir = True
        except:
                print("Formato ingresado no aceptado...")
                input("Enter para continuar...")
def modo():
    os.system("cls")
    print("============================================================================================")
    print("=                      ¡Seleccione el modo de juego!                                       =")
    print("============================================================================================")
    print("------->          1.  Un jugador                                              .<------------")
    print("------->          2.  Versus                                                  .<------------")
    print("------->          3.  Volver                                                  .<------------")
    print("============================================================================================")
    print("=                                          MENU                                            =")
    print("============================================================================================")
    opcion_modo = int(input("Ingrese opción_modo: "))
    if opcion_modo == 1:
        selectdificultad()
    elif opcion_modo == 2:
        #versus()
        pass
    elif opcion_modo ==3:
        input("Enter para volver al menu...")
    else:
        print("Formato ingresado no aceptado...")
        return input("Enter para continuar...")  

def crear_preguntas():
    os.system("cls")
    print("============================================================================================")
    print("=                ¡Seleccione el tema para el que desea crear preguntas!                    =")
    print("============================================================================================")
    print("------->          1.  Seleccionar tema                                        .<------------")
    print("------->          2.  Volver                                                  .<------------")
    print("============================================================================================")
    print("=                                          MENU                                            =")
    print("============================================================================================")
    opcion_crear = int(input("Ingrese opción_crear: "))
    if opcion_crear == 1:
        #crearpregunta()
        pass
    elif opcion_crear == 2:
       input("Enter para volver al menu...")
    else:
        print("Formato ingresado no aceptado...")
        return input("Enter para continuar...")

def selectdificultad():
    os.system("cls")
    print("============================================================================================")
    print("=                      ¡Seleccione la dificultad!                                          =")
    print("============================================================================================")
    print("------->          1.  Facil                                                   .<------------")
    print("------->          2.  Medio                                                   .<------------")
    print("------->          3.  Dificil                                                 .<------------")
    print("------->          4.  Volver                                                  .<------------")
    print("============================================================================================")
    print("=                                          MENU                                            =")
    print("============================================================================================")
    opcion_dificultad = int(input("Ingrese opción_dificultad: "))
    if opcion_dificultad == 1:
        #variable dificultad facil
        trivias()
    elif opcion_dificultad == 2:
        #variable dificultad medio
        trivias()
    elif opcion_dificultad == 3:
        #variable dificultad dificl
        trivias()
    elif opcion_dificultad == 4:
        input("Enter para volver al menu...")
    else:
        print("Formato ingresado no aceptado...")
        return input("Enter para continuar...")
#if __name__ == "__main__":
#    main()



