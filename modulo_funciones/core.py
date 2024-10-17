import os
def asci():
  print("\033[33;1;10m    /$$$$$$  /$$$$$$$  /$$$$$$/$$    /$$ /$$$$$$ /$$   /$$  /$$$$$$         /$$$$$$  /$$$$$$$  /$$$$$$/$$    /$$ /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$   \033[0m")
  print("\033[33;1;10m   /$$__  $$| $$__  $$|_  $$_/ $$   | $$|_  $$_/| $$$ | $$ /$$__  $$       /$$__  $$| $$__  $$|_  $$_/ $$   | $$|_  $$_/| $$$ | $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$\033[0m")
  print("\033[31;1;10m  | $$  \\ $$| $$  \\ $$  | $$ | $$   | $$  | $$  | $$$$| $$| $$  \\ $$      | $$  \\ $$| $$  \\ $$  | $$ | $$   | $$  | $$  | $$$$| $$| $$  \\ $$| $$  \\ $$| $$  \\ $$| $$  \\ $$\033[0m")
  print("\033[31;1;10m  | $$$$$$$$| $$  | $$  | $$ |  $$ / $$/  | $$  | $$ $$ $$| $$$$$$$$      | $$$$$$$$| $$  | $$  | $$ |  $$ / $$/  | $$  | $$ $$ $$| $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$/ \033[0m")
  print("\033[36;1;10m  | $$__  $$| $$  | $$  | $$  \\  $$ $$/   | $$  | $$  $$$$| $$__  $$      | $$__  $$| $$  | $$  | $$  \\  $$ $$/   | $$  | $$  $$$$| $$__  $$| $$  | $$| $$  | $$| $$__  $$\033[0m")
  print("\033[36;1;10m  | $$  | $$| $$  | $$  | $$   \\  $$$/    | $$  | $$\\  $$$| $$  | $$      | $$  | $$| $$  | $$  | $$   \\  $$$/    | $$  | $$\\  $$$| $$  | $$| $$  | $$| $$  | $$| $$  \\ $$ \033[0m")
  print("\033[37;1;10m  | $$  | $$| $$$$$$$/ /$$$$$$  \\  $/    /$$$$$$| $$ \\  $$| $$  | $$      | $$  | $$| $$$$$$$/ /$$$$$$  \\  $/    /$$$$$$| $$ \\  $$| $$  | $$| $$$$$$$/|  $$$$$$/| $$  | $$ \033[0m")
  print("\033[37;1;10m  |__/  |__/|_______/ |______/   \\_/    |______/|__/  \\__/|__/  |__/      |__/  |__/|_______/ |______/   \\_/    |______/|__/  \\__/|__/  |__/|_______/  \\______/ |__/  |__/ \033[0m")

def borde():
    print("\033[30;1;10m===========================================================================================================================================================================\033[0m")

def borde2():
    borde()
    print(f"\033[97;1;22m{"="}{"¿?"*85}{"="}\033[0m")
    borde()

def logo():
    borde2
    asci()
    borde2

def equipos():
    os.system("cls")
    logo()
    b=[

   " /$$$$$$$$/$$$$$$$$  /$$$$$$  /$$      /$$",
   "|__  $$__/ $$_____/ /$$__  $$| $$$    /$$$",
   "   | $$  | $$      | $$  \\ $$| $$$$  /$$$$",
   "   | $$  | $$$$$   | $$$$$$$$| $$ $$/$$ $$",
   "   | $$  | $$__/   | $$__  $$| $$  $$$| $$",
   "   | $$  | $$      | $$  | $$| $$\\  $ | $$",
   "   | $$  | $$$$$$$$| $$  | $$| $$ \\/  | $$",
   "   |__/  |________/|__/  |__/|__/     |__/ "                                                                                     
    ]
    for i in b:
        print(f"\033[32;1;22m{" "*50}{i}\033[0m")
    borde()
    print(f"\033[97;1;22m{"="}{"¿?"*85}{"="}\033[0m")
    borde()

    integrantes=["Valentini Augusto","Centurion Gonzalo","Leomagno Ernesto","Oksana Bernkhart","Luis Agustin Chen","Jesus Quijada"]
    for i in integrantes:
        print(f"\033[97;1;22m{i}\033[0m")
    
    borde()
    print(f"\033[97;1;22m{"="}{"¿?"*85}{"="}\033[0m")
    
    borde()
    input("Enter para continuar...")

def juegoinfo():
    logo()
    print(" Es un juego interactivo de preguntas y respuestas que ofrece a los jugadores una experiencia desafiante y educativa.\n Gracias a una amplia gama de temas y niveles de dificultad, diseñadas para jugadores de todas las edades. \n Este juego combina elementos de competencia y aprendizaje, permitiendo a los usuarios probar y ampliar sus conocimientos en diversas áreas")
    borde()
    input("Enter para continuar...")

def trivias():
    os.system("cls")
    logo()
    e=[
        "    /$$      /$$ /$$$$$$$$ /$$   /$$ /$$   /$$       /$$$$$$$  /$$$$$$$$       /$$$$$$$$/$$$$$$$  /$$$$$$/$$    /$$ /$$$$$$  /$$$$$$   /$$$$$$", 
        "   | $$$    /$$$| $$_____/| $$$ | $$| $$  | $$      | $$__  $$| $$_____/      |__  $$__/ $$__  $$|_  $$_/ $$   | $$|_  $$_/ /$$__  $$ /$$__  $$",
        "   | $$$$  /$$$$| $$      | $$$$| $$| $$  | $$      | $$  \\ $$| $$               | $$  | $$  \\ $$  | $$ | $$   | $$  | $$  | $$  \\ $$| $$  \\__/",
        "   | $$ $$/$$ $$| $$$$$   | $$ $$ $$| $$  | $$      | $$  | $$| $$$$$            | $$  | $$$$$$$/  | $$ |  $$ / $$/  | $$  | $$$$$$$$|  $$$$$$",
        "   | $$  $$$| $$| $$__/   | $$  $$$$| $$  | $$      | $$  | $$| $$__/            | $$  | $$__  $$  | $$  \\  $$ $$/   | $$  | $$__  $$ \\____  $$",
        "   | $$\\  $ | $$| $$      | $$\\  $$$| $$  | $$      | $$  | $$| $$               | $$  | $$  \\ $$  | $$   \\  $$$/    | $$  | $$  | $$ /$$  \\ $$",
        "   | $$ \\/  | $$| $$$$$$$$| $$ \\  $$|  $$$$$$/      | $$$$$$$/| $$$$$$$$         | $$  | $$  | $$ /$$$$$$  \\  $/    /$$$$$$| $$  | $$|  $$$$$$/",
        "   |__/     |__/|________/|__/  \\__/ \\______/       |_______/ |________/         |__/  |__/  |__/|______/   \\_/    |______/|__/  |__/ \\______/" 
                                                                                                                                                
    ]

    for i in e:
        print(f"\033[33;1;22m{" "*15}{i}\033[0m")
    
    borde()
    print(f"\033[97;1;22m{" "*79}{"¡Bienvenido!"}{" "*78}\033[0m")
    borde()

    d=["1. Trivia Formula 1","2. Trivia Cine","3. Trivia Futbol","3. Trivia Futbol","4. Trivia Deporte General","5. Trivia Video Juegos","6. Trivia Autos","7. Trivia Ciencias Naturales"]
    for i in d:
        print(f"\033[97;1;22m{"-"*4}{">."}{i}\033[0m")
    borde()
    print(f"\033[97;1;22m{" "*79}{"JUEGO"}{" "*78}\033[0m")
    borde()
    trivia = int(input("Ingrese opcion de trivia o enter para volver al menu: "))
    
    if trivia == 1:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import Formula

        f=[
            "  /$$$$$$$$                                         /$$                   /$$ ",
            " | $$_____/                                        | $$                 /$$$$ ",
            " | $$    /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$   /$$| $$  /$$$$$$       |_  $$ ",
            " | $$$$$/$$__  $$ /$$__  $$| $$_  $$_  $$| $$  | $$| $$ |____  $$        | $$ ",
            " | $$__/ $$  \\ $$| $$  \\__/| $$ \\ $$ \\ $$| $$  | $$| $$  /$$$$$$$        | $$ ",
            " | $$  | $$  | $$| $$      | $$ | $$ | $$| $$  | $$| $$ /$$__  $$        | $$ ",
            " | $$  |  $$$$$$/| $$      | $$ | $$ | $$|  $$$$$$/| $$|  $$$$$$$       /$$$$$$",
            " |__/   \\______/ |__/      |__/ |__/ |__/ \\______/ |__/ \\_______/      |______/"
                                                        
        ]
        for i in f:
            print(f"\033[31;1;22m{" "*48}{i}\033[0m")
        borde2
        Formula()
        input("Enter Para Continuar...")

    elif trivia == 2:
        print()
        print("="*7+"[Bienvenido trivia del cine]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia del Futbol]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia del Deporte General]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia de Video Juegos]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia de Autos]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia de Ciencias Naturales]"+ "="*7)
        print()
        from preguntas import ciennat
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
        ciennat()
        input("Enter para continuar...")

    elif trivia == 8:
        print()
        print("="*7+"[Bienvenido trivia de Cultura General]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia de Animales]"+ "="*7)
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
        print("="*7+"[Bienvenido trivia de Literatura]"+"="*7)
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
        logo()
        h=[
        "  /$$      /$$                              ",
        " | $$$    /$$$                              ",
        " | $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$   /$$",
        " | $$ $$/$$ $$ /$$__  $$| $$__  $$| $$  | $$",
        " | $$  $$$| $$| $$$$$$$$| $$\\ \\ $$| $$  | $$",
        " | $$\\  $ | $$| $$_____/| $$  | $$| $$  | $$",
        " | $$ \\/  | $$|  $$$$$$$| $$  | $$|  $$$$$$/",
        " |__/     |__/ \\_______/|__/  |__/ \\______/",
        ]
        for i in h:
            print(f"\033[32;1;22m{" "*48}{i}\033[0m")
        borde2
        print(f"\033[97;1;22m{" "*60}{"¡Bienvenido al menú elija alguna de las opciones!"}{" "*60}\033[0m")
        borde()
        modos=("1. Juego Trivia","2. Crear preguntas ","3. Puntajes","4.  Instrucciones","5.  Equipo","6.  Salir")
        for i in modos:
            print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
        borde2
        try:
            opcion_menu = int(input("Ingrese opción_menu: "))
            if opcion_menu == 1:
                modo()
                os.system("cls")
            elif opcion_menu == 2:
                crear_preguntas()
                os.system("cls")
            elif opcion_menu == 4:
                juegoinfo()
                os.system("cls")
            elif opcion_menu == 3:
                print("Funcion de puntajes.")
                input('Presione enter para continuar...')
                os.system("cls")
            elif opcion_menu == 5:
                equipos()
                os.system("cls")
            elif opcion_menu == 6:
                print("Cerrando...")
                salir = True
        except:
                print("Formato ingresado no aceptado...")
                input("Enter para continuar...")

def modo():
    os.system("cls")
    logo()
    print(f"\033[97;1;22m{" "*70}{"¡Seleccione el modo de juego!"}{" "*70}\033[0m")
    borde()
    modosjuego=("1.  Un jugador","2.  Versus","3.  Volver")
    for i in modosjuego:
        print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
    borde()
    print(f"\033[97;1;22m{"="}{" "*83}{"Menu"}{" "*83}{"="}\033[0m")
    borde()

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
    print("""
    ============================================================================================
    =                ¡Seleccione el tema para el que desea crear preguntas!                    =
    ============================================================================================
    ------->          1.  Seleccionar tema                                        .<------------
    ------->          2.  Volver                                                  .<------------
    ============================================================================================
    =                                          MENU                                            =
    ============================================================================================
    """)

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
    print("""
    ============================================================================================
    =                      ¡Seleccione la dificultad!                                          =
    ============================================================================================
    ------->          1.  Facil                                                   .<------------
    ------->          2.  Medio                                                   .<------------
    ------->          3.  Dificil                                                 .<------------
    ------->          4.  Volver                                                  .<------------
    ============================================================================================
    =                                          MENU                                            =
    ============================================================================================
    """)
    
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



