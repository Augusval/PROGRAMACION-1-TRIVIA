#-----------------------------------------------------------------------------------Librerias----------------------------------------------------------------------------------------------------------------
import os
import os
import time 
#-----------------------------------------------------------------------------------funciones----------------------------------------------------------------------------------------------------------------
def asci():
  print("\033[33;1;10m    /$$$$$$  /$$$$$$$  /$$$$$$/$$    /$$ /$$$$$$ /$$   /$$  /$$$$$$         /$$$$$$  /$$$$$$$  /$$$$$$/$$    /$$ /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$   \033[0m")
  time.sleep(0.2)
  print("\033[33;1;10m   /$$__  $$| $$__  $$|_  $$_/ $$   | $$|_  $$_/| $$$ | $$ /$$__  $$       /$$__  $$| $$__  $$|_  $$_/ $$   | $$|_  $$_/| $$$ | $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$\033[0m")
  time.sleep(0.2)
  print("\033[31;1;10m  | $$  \\ $$| $$  \\ $$  | $$ | $$   | $$  | $$  | $$$$| $$| $$  \\ $$      | $$  \\ $$| $$  \\ $$  | $$ | $$   | $$  | $$  | $$$$| $$| $$  \\ $$| $$  \\ $$| $$  \\ $$| $$  \\ $$\033[0m")
  time.sleep(0.2)
  print("\033[31;1;10m  | $$$$$$$$| $$  | $$  | $$ |  $$ / $$/  | $$  | $$ $$ $$| $$$$$$$$      | $$$$$$$$| $$  | $$  | $$ |  $$ / $$/  | $$  | $$ $$ $$| $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$/ \033[0m")
  time.sleep(0.2)
  print("\033[36;1;10m  | $$__  $$| $$  | $$  | $$  \\  $$ $$/   | $$  | $$  $$$$| $$__  $$      | $$__  $$| $$  | $$  | $$  \\  $$ $$/   | $$  | $$  $$$$| $$__  $$| $$  | $$| $$  | $$| $$__  $$\033[0m")
  time.sleep(0.2)
  print("\033[36;1;10m  | $$  | $$| $$  | $$  | $$   \\  $$$/    | $$  | $$\\  $$$| $$  | $$      | $$  | $$| $$  | $$  | $$   \\  $$$/    | $$  | $$\\  $$$| $$  | $$| $$  | $$| $$  | $$| $$  \\ $$ \033[0m")
  time.sleep(0.2)
  print("\033[37;1;10m  | $$  | $$| $$$$$$$/ /$$$$$$  \\  $/    /$$$$$$| $$ \\  $$| $$  | $$      | $$  | $$| $$$$$$$/ /$$$$$$  \\  $/    /$$$$$$| $$ \\  $$| $$  | $$| $$$$$$$/|  $$$$$$/| $$  | $$ \033[0m")
  time.sleep(0.2)
  print("\033[37;1;10m  |__/  |__/|_______/ |______/   \\_/    |______/|__/  \\__/|__/  |__/      |__/  |__/|_______/ |______/   \\_/    |______/|__/  \\__/|__/  |__/|_______/  \\______/ |__/  |__/ \033[0m")

def borde():
    print("\033[30;1;10m===========================================================================================================================================================================\033[0m")

def borde2():
    borde()
    time.sleep(0.2)
    print(f"\033[97;1;22m{"="}{"¿?"*85}{"="}\033[0m")
    time.sleep(0.2)
    borde()

def logo():
    borde2()
    asci()
    borde2()

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
        time.sleep(0.2)
    borde2()

    integrantes=["Valentini Augusto","Centurion Gonzalo","Leomagno Ernesto","Oksana Bernkhart","Luis Agustin Chen","Jesus Quijada"]
    for i in integrantes:
        print(f"\033[97;1;22m{i}\033[0m")
    borde2()
    input("Enter para continuar...")


def juegoinfo():
    os.system("cls")
    logo()
    print(" Es un juego interactivo de preguntas y respuestas que ofrece a los jugadores una experiencia desafiante y educativa.\n Gracias a una amplia gama de temas y niveles de dificultad, diseñadas para jugadores de todas las edades. \n Este juego combina elementos de competencia y aprendizaje, permitiendo a los usuarios probar y ampliar sus conocimientos en diversas áreas")
    print('La forma de jugar: \n 1)Si queremos jugar a alguna trivia, primero debemos seleccionar la opción "1.Juego Trivia" en el primer menu. Luego debemos seleccionar el modo de juego. Tendremos que decidir entre "1.Un jugador","2.Versus","3.Volver". Ahora lo unico que nos queda por hacer es elegir la trivia a la que querramos jugar. ')
    borde()
    input("Enter para continuar...")
#-----------------------------------------------------------------------------------MENU----------------------------------------------------------------------------------------------------------------
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
            time.sleep(0.2)
        borde2()
        time.sleep(0.2)
        print(f"\033[97;1;22m{" "*45}{"¡Bienvenido al menú elija alguna de las opciones!"}{" "*60}\033[0m")
        borde()
        modos=("1.Juego Trivia","2.Crear preguntas ","3.Puntajes","4.Instrucciones/descripcion del juego","5.Equipo","6.Salir")
        for i in modos:
            print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
        borde2()
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
                #puntajes()
                os.system("cls")
            elif opcion_menu == 5:
                equipos()
            elif opcion_menu == 6:
                print("Cerrando...")
                time.sleep(2)
                salir = True
        except:
            print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
            return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")

def modo():
    os.system("cls")
    logo()
    print(f"\033[97;1;22m{" "*70}{"¡Seleccione el modo de juego!"}{" "*70}\033[0m")
    borde()
    modosjuego=("1.Un jugador","2.Versus","3.Volver")
    for i in modosjuego:
        print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
    borde()
    print(f"\033[97;1;22m{"="}{" "*83}{"Menu"}{" "*83}{"="}\033[0m")
    borde()

    opcion_modo = int(input("Ingrese opción_modo: "))
    if opcion_modo == 1:
        selectdificultad()

    elif opcion_modo == 2:
        print("Función de selección de temas aún no implementada.")
        input("Presione Enter para continuar...")
        #versus()

    elif opcion_modo ==3:
        input("Enter para volver al menu...")

    else:
        print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
        return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")

def crear_preguntas():
    os.system("cls")
    logo()
    borde()
    print(f"\033[97;1;22m{" "*57}{"¡Seleccione el tema para el que desea crear preguntas!"}{" "*58}\033[0m")
    borde()
    temas=["1.  Seleccionar tema","2.  Volver"]
    for i in temas:
        print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
        time.sleep(0.2)
    borde()
    print(f"\033[97;1;22m{" "*82}{"MENU"}{" "*83}\033[0m")
    borde()
    
    opcion_crear = int(input("Ingrese opción_crear: "))
    if opcion_crear == 1:
        print("Función de selección de temas aún no implementada.")
        input("Presione Enter para continuar...")
        #crearpregunta()
    elif opcion_crear == 2:
       input("Enter para volver al menu...")
    else:
        print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
        return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")

def crear_preguntas():
    os.system("cls")
    logo()
    borde()
    print(f"\033[97;1;22m{" "*57}{"¡Seleccione el tema para el que desea crear preguntas!"}{" "*58}\033[0m")
    borde()
    temas=["1.  Seleccionar tema","2.  Volver"]
    for i in temas:
        print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
        time.sleep(0.2)
    borde()
    print(f"\033[97;1;22m{" "*82}{"MENU"}{" "*83}\033[0m")
    borde()
    
    opcion_crear = int(input("Ingrese opción_crear: "))
    if opcion_crear == 1:
        print("Función de selección de temas aún no implementada.")
        input("Presione Enter para continuar...")
        #crearpregunta()
    elif opcion_crear == 2:
       input("Enter para volver al menu...")
    else:
        print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
        return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")

def selectdificultad():
    os.system("cls")
    logo()
    borde()
    print(f"\033[97;1;22m{" "*71}{"¡Seleccione la dificultad"}{" "*72}\033[0m")
    borde()
    dificultad=("1.  Facil","2.  Medio","3.  Dificil","4.  Volver")
    for i in dificultad:
        print(f"\033[97;1;22m{"-"*2}{">"}{i}\033[0m")
    borde()
    print(f"\033[97;1;22m{" "*82}{"MENU"}{" "*83}\033[0m")
    borde()

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
        print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
        return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")

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
        time.sleep(0.2)

    borde()
    print(f"\033[97;1;22m{" "*79}{"¡Bienvenido!"}{" "*78}\033[0m")
    borde()

    d=["1. Trivia Formula 1","2. Trivia Cine","3. Trivia Futbol","4. Trivia Deporte General","5. Trivia Video Juegos","6. Trivia Autos","7. Trivia Ciencias Naturales","8. Trivia Cultura General","9.Trivia Animales","8. Trivia Literatura"]
    for i in d:
        print(f"\033[97;1;22m{"-"*4}{">."}{i}\033[0m")
    borde()
    print(f"\033[97;1;22m{" "*79}{"JUEGO"}{" "*78}\033[0m")
    borde()
    trivia = int(input("Ingrese opcion de trivia o enter para volver al menu: "))
#-----------------------------------------------------------------------------------CODIGO PRINCIPAL DEL JUEGO----------------------------------------------------------------------------------------------------------------  
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
            time.sleep(0.2)
        borde()
        print(f"\033[97;1;22m{"="}{"¿?"*85}{"="}\033[0m")
        borde()
        Formula()
        input("Enter Para Continuar...")

    elif trivia == 2:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import Cine
        g=[
            "    /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$",
            "   /$$__  $$|_  $$_/| $$$ | $$| $$_____/",
            "  | $$  \\__/  | $$  | $$$$| $$| $$",
            "  | $$        | $$  | $$ $$ $$| $$$$$",
            "  | $$        | $$  | $$  $$$$| $$__/",
            "  | $$    $$  | $$  | $$\\  $$$| $$",
            "  |  $$$$$$/ /$$$$$$| $$ \\  $$| $$$$$$$$",
            "  \\______/ |______/|__/  \\__/|________/", 
        ]
        for i in g:
            print(f"\033[93;1;22m{" "*62}{i}\033[0m")
            time.sleep(0.2)
        borde()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        Cine()
        input("Enter Para Continuar...")

    elif trivia == 3:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import Futbol
        h=[
        "  /$$$$$$$$          /$$     /$$                 /$$",
        " | $$_____/         | $$    | $$                | $$",
        " | $$    /$$   /$$ /$$$$$$  | $$$$$$$   /$$$$$$ | $$",
        " | $$$$$| $$  | $$|_  $$_/  | $$__  $$ /$$__  $$| $$",
        " | $$__/| $$  | $$  | $$    | $$  \\ $$| $$  \\ $$| $$",
        " | $$   | $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$",
        " | $$   |  $$$$$$/  |  $$$$/| $$$$$$$/|  $$$$$$/| $$",
        " |__/    \\______/    \\___/  |_______/  \\______/ |__/" 
        ]
        for i in h:
            print(f"\033[92;1;22m{" "*53}{i}\033[0m")
            time.sleep(0.2)
        borde()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        Futbol()
        input("Enter Para Continuar...")

    elif trivia == 4:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import DeporteGral
        j=[
            "  /$$$$$$$                                            /$$                      /$$$$$$                                                   /$$",
            " | $$__  $$                                          | $$                     /$$__  $$                                                 | $$",
            " | $$  \\ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$       | $$  \\__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ | $$",
            " | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$      | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$| $$",
            " | $$  | $$| $$$$$$$$| $$  \\ $$| $$  \\ $$| $$  \\__/  | $$    | $$$$$$$$      | $$|_  $$| $$$$$$$$| $$  \\ $$| $$$$$$$$| $$  \\__/ /$$$$$$$| $$",
            " | $$  | $$| $$_____/| $$  | $$| $$  | $$| $$        | $$ /$$| $$_____/      | $$  \\ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$| $$",
            " | $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$        |  $$$$/|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$| $$",
            " |_______/  \\_______/| $$____/  \\______/ |__/         \\___/   \\_______/       \\______/  \\_______/|__/  |__/ \\_______/|__/      \\_______/|__/",
            "                      | $$                                                                                                              ",
            "                      | $$                                                                                                                   ",
            "                      |__/                                                                                                                   "
        ]
        for i in j:
            print(f"\033[94;1;22m{" "*15}{i}\033[0m")
            time.sleep(0.2)
        borde()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        DeporteGral()
        input("Enter Para Continuar...")

    elif trivia == 5:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import VideoJuegos
        K=[
            "  /$$    /$$ /$$       /$$                              /$$$$$                                                  ",
            " | $$   | $$|__/      | $$                             |__  $$                                                  ",
            " | $$   | $$ /$$  /$$$$$$$  /$$$$$$   /$$$$$$             | $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$",
            " |  $$ / $$/| $$ /$$__  $$ /$$__  $$ /$$__  $$            | $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/",
            "  \\  $$ $$/ | $$| $$  | $$| $$$$$$$$| $$  \\ $$       /$$  | $$| $$  | $$| $$$$$$$$| $$  \\ $$| $$  \\ $$|  $$$$$$ ",
            "   \\  $$$/  | $$| $$  | $$| $$_____/| $$  | $$      | $$  | $$| $$  | $$| $$_____/| $$  | $$| $$  | $$ \\____  $$",
            "    \\  $/   | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/      |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/ /$$$$$$$/",
            "     \\_/    |__/ \\_______/ \\_______/ \\______/        \\______/  \\______/  \\_______/ \\____  $$ \\______/ |_______/ ",
            "                                                                                        /$$  \\ $$                ",
            "                                                                                       |  $$$$$$/                   ",
            "                                                                                        \\______/"
        ]
        for i in K:
            print(f"\033[92;1;22m{" "*15}{i}\033[0m")
            time.sleep(0.2)
        borde()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        VideoJuegos()
        input("Enter Para Continuar...")

    elif  trivia == 6:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import Auto
        m=[
        "   /$$$$$$              /$$                        ",
        "  /$$__  $$            | $$                        ",
        " | $$  \\ $$ /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$",
        " | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/",
        " | $$__  $$| $$  | $$  | $$    | $$  \\ $$|  $$$$$$ ",
        " | $$  | $$| $$  | $$  | $$ /$$| $$  | $$ \\____  $$",
        " | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/ /$$$$$$$/",
        " |__/  |__/ \\______/    \\___/   \\______/ |_______/"
        ]
        for i in m:
            print(f"\033[36;1;22m{" "*55}{i}\033[0m")
            time.sleep(0.2)
        borde()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        Auto()
        input("Enter Para Continuar...")

    elif trivia == 7:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import ciennat
        n=[
            "  /$$$$$$  /$$                               /$$                           /$$   /$$             /$$                                  /$$                    ",
            " /$$__  $$|__/                              |__/                          | $$$ | $$            | $$                                 | $$                    ",
            "| $$  \\__/ /$$  /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$$      | $$$$| $$  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$$ ",
            "| $$      | $$ /$$__  $$| $$__  $$ /$$_____/| $$ |____  $$ /$$_____/      | $$ $$ $$ |____  $$|_  $$_/  | $$  | $$ /$$__  $$|____  $$| $$ /$$__  $$ /$$_____/",
            "| $$      | $$| $$$$$$$$| $$  \\ $$| $$      | $$  /$$$$$$$|  $$$$$$       | $$  $$$$  /$$$$$$$  | $$    | $$  | $$| $$  \\__/ /$$$$$$$| $$| $$$$$$$$|  $$$$$$",
            "| $$    $$| $$| $$_____/| $$  | $$| $$      | $$ /$$__  $$ \\____  $$      | $$\\  $$$ /$$__  $$  | $$ /$$| $$  | $$| $$      /$$__  $$| $$| $$_____/ \\____  $$",
            "|  $$$$$$/| $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/      | $$ \\  $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$     |  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/",
            " \\______/ |__/ \\_______/|__/  |__/ \\_______/|__/ \\_______/|_______/       |__/  \\__/ \\_______/   \\___/   \\______/ |__/      \\_______/|__/ \\_______/|_______/"
        ]
        for i in n:
            print(f"\033[36;1;22m{" "*8}{i}\033[0m")
            time.sleep(0.2)
        borde()
        ciennat()
        input("Enter para continuar...")

    elif trivia == 8:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import CulGen
        l=[
            "    /$$$$$$            /$$   /$$                                         /$$$$$$                                                   /$$",
            "   /$$__  $$          | $$  | $$                                        /$$__  $$                                                 | $$",
            "  | $$  \\__/ /$$   /$$| $$ /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$       | $$  \\__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ | $$",
            "  | $$      | $$  | $$| $$|_  $$_/  | $$  | $$ /$$__  $$|____  $$      | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$| $$",
            "  | $$      | $$  | $$| $$  | $$    | $$  | $$| $$  \\__/ /$$$$$$$      | $$|_  $$| $$$$$$$$| $$  \\ $$| $$$$$$$$| $$  \\__/ /$$$$$$$| $$",
            "  | $$    $$| $$  | $$| $$  | $$ /$$| $$  | $$| $$      /$$__  $$      | $$  \\ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$| $$",
            "  |  $$$$$$/|  $$$$$$/| $$  |  $$$$/|  $$$$$$/| $$     |  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$| $$",
            "  \\______/  \\______/ |__/   \\___/   \\______/ |__/      \\_______/       \\______/  \\_______/|__/  |__/ \\_______/|__/      \\_______/|__/"
        ]
        for i in l:
            print(f"\033[92;1;22m{" "*18}{i}\033[0m")
            time.sleep(0.2)
        borde()
        CulGen()
        input("Enter para continuar...")

    elif trivia == 9:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import animales
        o=[
            "       /$$$$$$            /$$                         /$$                    ",
            "      /$$__  $$          |__/                        | $$                    ",
            "     | $$  \\ $$ /$$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$$",
            "     | $$$$$$$$| $$__  $$| $$| $$_  $$_  $$ |____  $$| $$ /$$__  $$ /$$_____/",
            "     | $$__  $$| $$  \\ $$| $$| $$ \\ $$ \\ $$  /$$$$$$$| $$| $$$$$$$$|  $$$$$$",
            "     | $$  | $$| $$  | $$| $$| $$ | $$ | $$ /$$__  $$| $$| $$_____/ \\____  $$",
            "     | $$  | $$| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/",
            "     |__/  |__/|__/  |__/|__/|__/ |__/ |__/ \\_______/|__/ \\_______/|_______/"
        ]
        for i in o:
            print(f"\033[96;1;22m{" "*40}{i}\033[0m")
            time.sleep(0.2)
        borde()
        animales()
        input("Enter para continuar...")

    elif trivia == 10:
        os.system("cls")
        logo()
        print(f"\033[97;1;22m{" "*66}{"¡Bienvenido a la trivia!"}{" "*66}\033[0m")
        borde()
        from preguntas import Lite
        p=[
            "      /$$       /$$   /$$                                    /$$                                 ",
            "     | $$      |__/  | $$                                   | $$                                 ",
            "     | $$       /$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$ ",
            "     | $$      | $$|_  $$_/   /$$__  $$ /$$__  $$|____  $$|_  $$_/  | $$  | $$ /$$__  $$|____  $$",
            "     | $$      | $$  | $$    | $$$$$$$$| $$  \\__/ /$$$$$$$  | $$    | $$  | $$| $$  \\__/ /$$$$$$$",
            "     | $$      | $$  | $$ /$$| $$_____/| $$      /$$__  $$  | $$ /$$| $$  | $$| $$      /$$__  $$",
            "     | $$$$$$$$| $$  |  $$$$/|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$     |  $$$$$$$",
            "     |________/|__/   \\___/   \\_______/|__/      \\_______/   \\___/   \\______/ |__/      \\_______/"
        ]
        for i in p:
            print(f"\033[97;1;22m{" "*30}{i}\033[0m")
            time.sleep(0.2)
        borde()
        Lite()
        input("Enter para continuar...")
    else:
        print(f"\033[91;1;22m{"Formato ingresado no aceptado..."}\033[0m")
        return print(f"\033[96;1;22m{input("Enter para continuar...") }\033[0m")


#if __name__ == "__main__":
#    main()



