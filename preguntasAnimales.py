# Lista de preguntas con opciones
preguntas_futbol = [
    #1
    '¿Cuál es el mamífero más grande del mundo? a) Elefante b) Ballena azul c) Jirafa d) Oso polar',
    #2
    '¿Qué tipo de animal es un delfín? a) Pez b) Mamífero c) Reptil d) Anfibio',
    #3
    '¿Cuál es el ave más rápida en vuelo? a) Halcón peregrino b) Águila c) Colibrí d) Faisán',
    #4
    '¿Qué animal es conocido por su habilidad para cambiar de color? a) Gecko b) Pulpo c) Rana d) Camaleón',
    #5
    '¿Cuál de estos animales es un marsupial? a) Oso b) Lobo c) Canguro d) Gato',
    #6
    '¿Qué animal puede vivir más tiempo sin agua? a) Camello b) Perro c) Gato d) Elefante',
    #7
    '¿Cuál es el único mamífero que puede volar? a) Ardilla voladora b)Colugo  c) Pájaro carpintero d) Murciélago',
    #8
    '¿Qué animal tiene la lengua más larga en relación a su cuerpo? a) Rana b) Camaleón c) Jirafa d) Hummingbird',
    #9
    '¿Cuál de estos animales es un depredador tope en su hábitat? a) León b) Cebra c) Jirafa d) Elefante',
    #10
    '¿Qué tipo de animal es un tiburón? a) Mamífero b) Anfibio c) Reptil d) Pez',
    #11
    '¿Cuál es el animal más rápido en tierra? a) Conejo b) Antílope c) Cheetah d) Perro',
    #12
    '¿Qué animal es conocido por ser el "rey de la selva"? a) Tigre b) León c) Gorila d) Elefante',
    #13
    '¿Cuál es la principal dieta de un panda gigante? a) Carne b) Insectos c) Bambú d) Frutas',
    #14
    '¿Qué tipo de animal es una oruga? a) Mamífero b) Reptil c) Anfibio d) Insecto',
    #15
    '¿Cuál es el único primate que no vive en los árboles? a) Humano b) Chimpancé c) Gorila d) Orangután',
    #16
    '¿Qué animal se considera el más inteligente? a) Perro b) Delfín c) Cuervo d) Elefante',
    #17
    '¿Cuál de estos animales es un roedor? a) Gato b) Conejo c) Ratón d) Serpiente',
    #18
    '¿Qué animal es conocido por su capacidad para imitar sonidos? a) Loro b) Búho c) Pájaro cantor d) Golondrina',
    #19
    '¿Cuál de estos animales vive en la Antártida? a) Leopardo b) Camello c) Cebra d) Foca',
    #20
    '¿Qué animal tiene el corazón más grande en relación a su tamaño? a) Elefante b) Ballena azul c) Gato d) Ratón',
    #21
    '¿Cuál es el animal terrestre más grande? a) Elefante africano b) Hipopótamo c) Rinoceronte d) Jirafa',
    #22
    '¿Qué tipo de animal es una anaconda? a) Reptil b) Mamífero c) Anfibio d) Pez',
    #23
    '¿Qué animal tiene la capacidad de ver en la oscuridad? a) Gato b) Perro c) Murciélago d) Todos los anteriores', 
    #24
    '¿Cuál es el principal depredador de los pingüinos? a) León marino b) Orca c) Halcón d) Tiburón',
    #25
    '¿Qué tipo de animal es un flamenco? a) Mamífero b) Pez c) Ave d) Reptil',



]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "b",  # Ballena azul (1)
    "b",  # Mamífero (2)
    "a",  # Halcón peregrino (3)
    "d",  # Camaleón (4)
    "c",  # Canguro (5)
    "a",  # Camello (6)
    "d",  # Murciélago (7)
    "b",  # Camaleón (8)
    "a",  # León (9)
    "d",  # Pez (10)
    "c",  # Cheetah (11)
    "b",  # León (12)
    "c",  # Bambú (13)
    "d",  # Insecto (14)
    "a",  # Humano (15)
    "b",  # Delfín (16)
    "c",  # Ratón (17)
    "a",  # Loro (18)
    "d",  # Foca (19)
    "b",  # Ballena azul (20)
    "a",  # Elefante africano (21)
    "a",  # Reptil (22)
    "c",  # Murciélago (23)
    "b",  # Orca (24)
    "c"  # Ave (25)
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas = [
    {"pregunta": preguntas_futbol[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_futbol))
]

# Función para jugar al juego de trivia
def jugar_trivia():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de fútbol!\n")

    for i, item in enumerate(preguntas_respuestas):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas)}")
    if puntaje == len(preguntas_respuestas):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego
jugar_trivia()