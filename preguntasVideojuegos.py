# Lista de preguntas con opciones
preguntas_futbol = [
    '¿Cuál de los siguientes personajes es el protagonista principal en la serie de videojuegos "The Legend of Zelda"? a) Ganondorf b) Link c) Zelda d) Navi',
    '¿En qué año se lanzó el videojuego "Super Mario Bros." para la consola NES? a) 1983 b) 1985 c) 1987 d) 1989',
    '¿Cuál es el nombre del mundo en el que se desarrolla la saga de "Final Fantasy VII"? a) Eorzea b) Spira c) Gaia d) Ivalice',
    '¿Cuál de estos juegos fue desarrollado por Rockstar Games? a) The Elder Scrolls V: Skyrim b) Grand Theft Auto V c) Dark Souls d) Halo: Combat Evolved',
    "¿En qué juego de la saga “The Legend of Zelda” se explora un mundo subterráneo conocido como el" '"Inframundo"'"? a) The Legend of Zelda: A Link to the Past b) The Legend of Zelda: Ocarina of Time c) The Legend of Zelda: Breath of the Wild d) The Legend of Zelda: Majora's Mask" 
    '¿En qué juego de disparos en primera persona puedes jugar como el personaje Master Chief? a) Destiny b) Battlefield c) Call of Duty d) Halo',
    '¿Cuál de estos videojuegos pertenece a la serie de rol conocida por sus batallas y exploración en el mundo de "Eorzea"? a) Final Fantasy XIV b) Dragon Age: Inquisition c)World of Warcraft d) Elder Scrolls Online',
    '¿En qué juego se encuentra el personaje llamado “Pac-Man”? a) Donkey Kong b) Space Invaders c) Pac-Man d) Galaga',
    '¿Qué tipo de juego es “Among Us”? a) Juego de plataformas b) Juego de rol c) Juego de misterio social d) Shooter en primera persona',
    '¿Cuál de los siguientes juegos es un título clásico de la consola Sega Genesis? a) Sonic the Hedgehog b) Super Mario World c) The Legend of Zelda: Ocarina of Time d) Donkey Kong Country',
    '¿En qué serie de videojuegos luchan los personajes conocidos como "Hunters" contra monstruos gigantes? a) Horizon Zero Dawn b) Dark Souls c) Bloodborne d) Monster Hunter',
    '¿Cuál de estos videojuegos fue creado por la compañía Nintendo? a) Metal Gear Solid b) Final Fantasy c) The Legend of Zelda d) Fallout'
    '¿Cuál es el objetivo principal en el juego “Minecraft”? a) Completar una campaña de historia b) Construir y explorar c) Ganar en batallas en línea d) Resolver rompecabezas',
    '¿En qué juego puedes encontrar el "Pikachu" como uno de los personajes principales? a) Pokémon b) Digimon c) Yu-Gi-Oh! d) Final Fantasy',
    '¿Qué videojuego se ambienta en una ciudad ficticia llamada Raccoon City? a) Silent Hill b) Resident Evil c) Dead Space d) Outlast',
    '¿Qué videojuego es conocido por introducir el personaje "Kratos" en un mundo de mitología griega? a) God of War b) Dante’s Inferno c) Castlevania d) Demon’s Souls',
    '¿Cuál es el nombre del universo de "Mass Effect"? a) The Elder Scrolls b) The Halo Universe c) The Mass Effect Universe d) The Star Wars Universe',
    '¿Qué videojuego se desarrolla en el universo de Star Wars y se centra en combates espaciales? a) Star Wars: Knights of the Old Republic b) Star Wars: Battlefront c) Star Wars: Jedi: Fallen Order d) Star Wars: The Old Republic',
    '¿En qué tipo de juego se basa el título “The Witcher 3: Wild Hunt”? a) Juego de rol de acción b) Juego de estrategia en tiempo real c) Juego de disparos en primera persona d) Juego de plataformas ',
    '¿Qué videojuego es conocido por sus mapas y escenarios destructibles y fue creado por DICE? a) Call of Duty b) Battlefield c) Rainbow Six Siege d) Counter-Strike',
    '¿En qué juego puedes encontrar el personaje llamado “Ellie” como uno de los protagonistas? a) The Last of Us b) Uncharted c) Red Dead Redemption d) God of War',
    '¿Cuál de estos videojuegos es conocido por su mecánica de combate basada en el uso de espadas y magia? a) Skyrim b) Dark Souls c) Overwatch d) Apex Legends',
    '¿En qué juego se destacan la construcción de estructuras y la defensa contra enemigos en un entorno de supervivencia? a) Rust b) Fornite c) ARK: Survival Evolved d) Conan Exiles',
    '¿En qué salio el juego World of Warcraft? a) 1998 b) 2002 c) 2000 d) 2004',
    '¿Cuál de estos juegos fue uno de los primeros en popularizar el género de batalla real? a) Fortnite b) PUBG (PlayerUnknowns Battlegrounds) c) Apex Legends d) Warzone',



]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "b",  # Link (1)
    "b",  # 1985 (2)
    "c",  # Gaia (3)
    "b",  # GTA V (4)
    "a",  # The Legend of Zelda: A Link to the Past (5)
    "d",  # Halo (6)
    "a",  # Final Fantasy XIV (7)
    "c",  # Pac-Man(8)
    "c",  # Juego de misterio social (9)
    "a",  # Sonic the Hedgehog (10)
    "d",  # Monster Hunter (11)
    "c",  # The Legend of Zelda (12)
    "b",  # Construir y explorar (13)
    "a",  # Pokémon (14)
    "b",  # Resident Evil (15)
    "a",  # God of War (16)
    "c",  # The Mass Effect Universe (17)
    "b",  # Star Wars: Battlefront (18)
    "a",  # Juego de rol de acción (19)
    "b",   # Battlefield (20)
    "a",  # The Last of Us (21)
    "a",  # Skyrim (22)
    "c",  # ARK: Survival Evolved (23)
    "d",  # 2004
    "b"  # PUBG (PlayerUnknown’s Battlegrounds)
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