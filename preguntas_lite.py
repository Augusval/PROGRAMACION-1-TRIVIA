# Lista de preguntas con opciones
preguntas_Lite=[
    #1
    '¿Quién escribió "Cien años de soledad"? a) Julio Cortázar  b) Gabriel García Márquez  c) Mario Vargas Llosa  d) Jorge Luis Borges ',
    #2
    '¿Qué novela comienza con la frase "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"? a) La casa de los espíritus b) Don Quijote de la Mancha c) La colmena d) Crónica de una muerte anunciada',
    #3
    '¿Quién es el autor de "1984"? a) Aldous Huxley b) Ray Bradbury c) George Orwell d) H.G. Wells',
    #4
    '¿Cuál es el autor de "Don Quijote de la Mancha"? a) Miguel de Unamuno b) Gabriel García Márquez c) Miguel de Cervantes d) Lope de Vega',
    #5
    '¿Qué obra es famosa por la frase "Soy un hombre en busca de sentido"? a) El extranjero b) El guardián entre el centeno c) El hombre en busca de sentido d) La nausea',
    #6 
    '¿Quién escribió "La metamorfosis"? a) Franz Kafka b) Fiódor Dostoyevski c) Thomas Mann d) Hermann Hesse',
    #7
    '¿Cuál es la obra más famosa de Shakespeare? a) El sueño de una noche de verano b) Hamlet c) Romeo y Julieta d) Otelo',
    #8
    '¿Qué autor escribió "Orgullo y prejuicio"? a) Charlotte Brontë b) Jane Austen c) Emily Brontë d) Mary Shelley',
    #9
    '¿Quién es el protagonista de "Moby Dick"? a) Ahab b) Ishmael c) Queequeg d) Starbuck',
    #10
    '¿En qué obra aparece el personaje de Holden Caulfield? a) El guardián entre el centeno b) El gran Gatsby c) Las uvas de la ira d) Moby Dick',
    #11
    '¿Qué autor es conocido por su obra "El proceso"? a) Fiódor Dostoyevski b) Franz Kafka  c) Albert Camus d) Leo Tolstoy',
    #12
    '¿Quién escribió "El viejo y el mar"? a) Mark Twain b) John Steinbeck c) F. Scott Fitzgerald d) Ernest Hemingway',
    #13
    '¿Cuál es la temática central de "La casa de los espíritus"? a) La guerra b) La soledad c) La familia y la historia d) La libertad',
    #14
    '¿Quién es el autor de "Crónica de una muerte anunciada"? a) Gabriel García Márquez b) Mario Vargas Llosa c) Julio Cortázar d) Isabel Allende',
    #15
    '¿Qué poeta escribió "Rimas y leyendas"? a) Gustavo Adolfo Bécquer b) Rubén Darío c) Pablo Neruda d) Vicente Huidobro',
    #16
    '¿Cuál es la obra más famosa de Gabriel García Márquez? a) El amor en los tiempos del cólera b) Cien años de soledad c) El otoño del patriarca d) Crónica de una muerte anunciada',
    #17
    '¿Quién escribió "En busca del tiempo perdido"? a) Marcel Proust b) Virginia Woolf c) James Joyce d) Franz Kafka',
    #18
    '¿Qué novela tiene como protagonista a un joven llamado Santiago Nasar? a) El túnel b) Crónica de una muerte anunciada c) La sombra del viento d) La casa de los espíritus',
    #19
    '¿Quién es el autor de "Rayuela"? a) Gabriel García Márquez b) Julio Cortázar c) Mario Vargas Llosa d) Jorge Luis Borges',
    #20
    '¿Qué obra de teatro es considerada una tragedia griega clásica? a) La Orestíada b) Antígona c) Edipo Rey d) Las bacantes',
    #21
    '¿Quién escribió "Los miserables"? a) Honoré de Balzac b) Victor Hugo c) Gustave Flaubert d) Émile Zola',
    #22
    '¿Qué poeta es conocido por su obra "Veinte poemas de amor y una canción desesperada"? a) Pablo Neruda b) Gabriela Mistral c) Vicente Huidobro d) Jorge Luis Borges',
    #23
    '¿Quién es el autor de "El retrato de Dorian Gray"? a) Oscar Wilde b) Bram Stoker c) Charles Dickens d) Mark Twain',
    #24
    '¿Qué novela de Miguel de Cervantes sigue las aventuras de un caballero loco? a) La Galatea b) Don Quijote de la Mancha c) Novelas ejemplares d) Los trabajos de Persiles y Sigismunda',
    #25
    '¿Qué autora escribió "El cuento de la criada"? a) Margaret Atwood b) Virginia Woolf c) Toni Morrison d) Sylvia Plath',

]

# Lista de respuestas correctas
respuestas_correctas_Lite = [
    "b",  # Gabriel García Márquez (1)
    "b",  # Don Quijote de la Mancha (2)
    "c",  # George Orwell (3)
    "c",  # Miguel de Cervantes (4)
    "c",  #  El hombre en busca de sentido (5)
    "a",  # Franz Kafka (6)
    "b",  # Hamlet (7)
    "b",  # Jane Austen (8)
    "a",  # Ahab (9)
    "a",  # El guardián entre el centeno (10)
    "b",  # Franz Kafka (11)
    "d",  # Ernest Hemingway (12)
    "c",  # La familia y la historia (13)
    "a",  # Gabriel García Márquez (14)
    "a",  # Gustavo Adolfo Bécquer (15)
    "b",  # Cien años de soledad (16)
    "a",  # Marcel Proust (17)
    "b",  # Crónica de una muerte anunciada (18)
    "b",  # Julio Cortázar (19)
    "a",  # La Orestíada (20)
    "b",  # Victor Hugo (21)
    "a",  # Pablo Neruda (22)
    "a",  # Oscar Wilde (23)
    "b",  # Don Quijote de la Mancha (24)
    "a"  # Margaret Atwood (25)
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas_Lite = [
    {"pregunta": preguntas_Lite[i], "respuesta_correcta": respuestas_correctas_Lite[i]} 
    for i in range(len(preguntas_Lite))
]

# Función para jugar al juego de trivia
def Auto():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de autos!\n")

    for i, item in enumerate(preguntas_respuestas_Lite):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_Lite)}")
    if puntaje == len(preguntas_respuestas_Lite):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_Lite) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")