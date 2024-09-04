# Lista de preguntas con opciones
preguntas_futbol = [
    #1
    '¿Cuál de las siguientes películas ganó el Oscar a Mejor Película en 2023? a) Everything Everywhere All at Once b) The Fabelmans c) Top Gun: Maverick d) Avatar: The Way of Water',
    #2
    '¿Quién dirigió la película "Titanic"? a) James Cameron b) Steven Spielberg c) Martin Scorsese d) Ridley Scott',
    #3
    '¿En qué película se dice la famosa frase "Que la fuerza te acompañe"? a) Star Wars b) Star Trek c) Dune d) Avatar',
    #4
    '¿Cuál de estos actores interpretó a Jack Sparrow en "Piratas del Caribe"? a) Orlando Bloom b) brad pitt c) Tom Cruise d) Johnny Depp',
    #5
    "¿Qué película ganó el Oscar a la Mejor Película en 1994? a) Pulp Fiction b) Forrest Gump c) The Shawshank Redemption d) The Lion King" 
    #6
    '¿Quién interpretó a Wolverine en la serie de películas de "X-Men"? a) Hugh Jackman b) Ryan Reynolds c) Chris Hemsworth d) Robert Downey Jr.',
    #7
    '¿En qué año se estrenó "Jurassic Park"? a) 1990 b) 1993 c)1996 d) 1999',
    #8
    '¿Qué película animada de Pixar trata sobre un grupo de ratones que quiere convertirse en chefs? a) Buscando a Nemo b) Up c) Ratatouille d) Toy Story',
    #9
    '¿Cuál es el nombre del protagonista en la serie de películas "The Matrix"? a) Neo b) Trinity c) Morpheus d) Cypher ',
    #10
    ' ¿Qué director es conocido por la trilogía "El Señor de los Anillos"? a) Guillermo del Toro b) George Lucas c) Francis Ford Coppola d) Peter Jackson',
    #11
    '¿Cuál es el nombre de la joven protagonista en "Harry Potter y la Piedra Filosofal"? a) Hermione Granger b) Ginny Weasley c) Luna Lovegood d) Molly Weasley',
    #12
    '¿Quién interpretó a la princesa Leia en "Star Wars"? a) Daisy Ridley b) Natalie Portman c) Carrie Fisher d) Emilia Clarke',
    #13
    '¿En qué película el personaje principal es un extraterrestre llamado E.T.? a) Close Encounters of the Third Kind b) E.T. the Extra-Terrestrial c) The Day the Earth Stood Still d) Men in Black',
    #14
    '¿Qué película protagonizada por Tom Hanks está ambientada en un campo de guerra durante la Segunda Guerra Mundial? a) Forrest Gump b) Cast Away c) Saving Private Ryan d) Apollo 13',
    #15
    '¿Quién dirigió "Inception" (Origen)? a) Christopher Nolan b) Quentin Tarantino c) David Fincher d) Denis Villeneuve',
    #16
    '¿Qué película cuenta la historia de un joven que se convierte en un luchador profesional en la India y se convierte en una estrella de Bollywood? a) Slumdog Millionaire b) Lagaan c) Dangal d) 3 Idiots',
    #17
    '¿Quién interpretó a Jack Dawson en "Titanic"? a) Leonardo DiCaprio b) Tom Cruise c) Brad Pitt d) Matt Damon',
    #18
    '¿En qué año se estrenó "Star Wars: Episodio IV-Una nueva esperanza"? a) 1975 b) 1977 c) 1980 d) 1983',
    #19
    '¿Qué actor interpretó al Joker en "El caballero oscuro" (2008)? a) Jack Nicholson b) Jared Leto c) Heath Ledger d) Joaquin Phoenix ',
    #20
    '¿En qué película se basa el famoso libro de J.R.R. Tolkien "El señor de los anillos"? a) Harry Potter b) Los juegos del hambre c) El señor de los anillos d) El hobbit',
    #21
    '¿Cuál es el nombre del famoso arqueólogo interpretado por Harrison Ford? a) Indiana Jones b) Han Solo c) James Bond d) Luke Skywalker',
    #22
    '¿Qué película de ciencia ficción trata sobre una invasión alienígena en una ciudad? a) E.T. b) Independence Day c) Encuentros Cercanos del Tercer Tipo d) Blade Runner',
    #23
    '¿Qué director es conocido por sus películas de terror como "El resplandor" y "La naranja mecánica"? a) Stanley Kubrick b) Steven Spielberg c) Alfred Hitchcock d) Ridley Scott',
    #24
    '¿Cual de la siguientes series es de medicina? a)Grey´s anatomy b) Dc House c) The Good Doctor d) Todas las anteriores',
    #25
    '¿Cuál de las siguientes no es una serie centrada en la física? a) The Big Bang Theory b) Breaking Bad c) Cosmos d) The IT Crowd',



]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "a",  # Everything Everywhere All at Once (1)
    "a",  # James Cameron (2)
    "a",  # Star Wars (3)
    "d",  # Johnny Depp (4)
    "b",  # Forrest Gump (5)
    "a",  # Hugh Jackman (6)
    "b",  # 1993 (7)
    "c",  # Ratatouille(8)
    "a",  # Neo (9)
    "d",  # Peter Jackson (10)
    "a",  # Hermione Granger (11)
    "c",  # Carrie Fisher (12)
    "b",  # E.T. the Extra-Terrestrial (13)
    "c",  # Saving Private Ryan (14)
    "a",  # Christopher Nolan (15)
    "c",  # Dangal (16)
    "a",  # Leonardo DiCaprio (17)
    "b",  # 1977 (18)
    "c",  # Heath Ledger (19)
    "c",  # El señor de los anillos (20)
    "a",  # Indiana Jones (21)
    "b",  # Independence Day (22)
    "a",  # Stanley Kubrick (23)
    "d",  # Todas las anteriores
    "a"  # The Big Bang Theory
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