# Lista de preguntas con opciones
preguntas_CulGen=[
#1
"¿Cuál es la capital de Francia? a) Berlín b) Madrid c) Roma d) París", 
#2
'¿Quién escribió "Cien años de soledad"? a) Julio Cortázar b) Gabriel García Márquez c) Jorge Luis Borges d) Mario Vargas Llosa',
#3
"¿Cuál es el continente más grande?  a) África b) Europa c) Asia d) América",
#4
"¿En qué año llegó el hombre a la Luna? a) 1965 b) 1969 c) 1972 d) 1975",   
#5
"¿Qué océano es el más grande del mundo? a) Atlántico b) Índico c) Pacífico d) Ártico", 
#6
"¿Quién pintó la Mona Lisa? a) Vincent van Gogh b) Pablo Picasso  c) Leonardo da Vinci d) Salvador Dalí",
#7
"¿Cuál es la moneda oficial de Japón? a) Yen b) Won c) Yuan d) Dólar",  
#8
'¿Qué planeta es conocido como el "planeta rojo"? a) Venus b) Júpiter c) Saturno d) Marte' ,
#9
"¿Quién fue el primer presidente de los Estados Unidos? a) Thomas Jefferson b) Abraham Lincoln c) George Washington d) John Adams",  
#10
"¿Cuál es el río más largo del mundo? a) Amazonas b) Nilo c) Yangtsé d) Misisipi",  
#11
"¿Qué idioma se habla principalmente en Brasil? a) Español b) Inglés c) Portugués  d) Francés", 
#12
"¿Cuál es la capital de Egipto? a)Alejandría  b) El Cairo c) Casablanca d) Túnez",
#13
'¿Qué deporte es conocido como "el rey de los deportes"?  a) Fútbol b) Baloncesto c) Tenis d) Rugby',
#14
"¿Cuál es la principal fuente de energía del sol? a) Fisión nuclear b) Química c) Geotérmica d) Fusión nuclear",
#15
'¿Quién es el autor de "Don Quijote de la Mancha"? a) Lope de Vega b) Miguel de Cervantes c) Gabriel García Márquez d) Federico García Lorca',
#16
"¿Cuál es el animal terrestre más grande? a) Elefante africano b) Jirafa c) Hipopótamo d) Rinoceronte",
#17
"¿Qué estructura es considerada una de las siete maravillas del mundo antiguo? a) La Gran Muralla b) Las Pirámides de Giza c) El Coloso de Rodas d) El Partenón",
#18
"¿Qué tipo de animal es un delfín? a) Pez b) Reptil c) Anfibio d) Mamífero",
#19
"¿Cuál es el deporte más practicado en el mundo? a) Baloncesto b) Tenis c) Fútbol d) Rugby ",  
#20
"¿Qué invento es atribuido a Thomas Edison? a) Bombilla eléctrica b) Teléfonno c) Radio d) Computadora",  
#21
"¿Cuál es el sistema operativo de Apple? a) Windows b) Linux c) macOS d) Andoroid",
#22
'¿Qué elemento químico tiene el símbolo "H"? a) Helio b) Hidrógeno c) Mercurio d) Oxígeno',
#23
"¿En qué país se originó el tango?  a) Argentina b) Uruguay c) Chile d) Perú",
#24
"¿Qué famoso científico desarrolló la teoría de la relatividad? a) Isaac Newton b) Stephen Hawking c) Nikola Tesla d) Albert Einstein",
#25
"¿Qué planeta es conocido por tener anillos? a) Júpiter b) Saturno c) Urano d) Neptuno",
]

# Lista de respuestas correctas
respuestas_correctas = [
    "d",  # París (1)
    "b",  # Gabriel García Márquez(2)
    "c",  # Asia (3)
    "b",  # 1969 (4)
    "c",  # Pacífico (5)
    "c",  # Leonardo da Vinci (6)
    "a",  # Yen (7)
    "d",  # Marte  (8)
    "c",  # George Washington  (9)
    "a",  #  Amazonas (10)
    "c",  # Portugués  (11)
    "b",  # El Cairo  (12)
    "a",  # Fútbol   (13)
    "d",  # Fusión nuclear (14)
    "b",  # Miguel de Cervantes (15)
    "a",  # Elefante africano (16)
    "b",  # Las Pirámides de Giza (17)
    "d",  # Mamífero (18)
    "c",  # Fútbol (19)
    "a",  # Bombilla eléctrica (20)
    "c",  # macOS (21)
    "b",  # Hidrógeno (22)
    "a",  # Argentina (23)
    "d",  # Albert Einstein (24)
    "b",  # Saturno (25)
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas_CulGen = [
    {"pregunta": preguntas_CulGen[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_CulGen))
]

# Función para jugar al juego de trivia
def Auto():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de autos!\n")

    for i, item in enumerate(preguntas_respuestas_CulGen):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_CulGen)}")
    if puntaje == len(preguntas_respuestas_CulGen):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_CulGen) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")