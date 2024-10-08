# Lista de preguntas con opciones
preguntas_autos=[
    #1
    "¿Cuál es la marca de autos más antigua aún en funcionamiento? a) Ford, b) Mercedes-Benz, c) Fiat, d) Peugeot", 
    #2
    "¿Qué marca produce el modelo Mustang? a) Chevrolet, b) Dodge, c) Ford, d) Nissan",
    #3
    "¿En qué país se fundó Ferrari? a) Alemania, b) Italia, c) Francia, d) Estados Unidos",
    #4
    "¿Cuál fue el primer auto producido en masa? a) Ford Model T, b) Mercedes-Benz 300SL, c) Chevrolet Corvette, d) Volkswagen Beetle",   
    #5
    "¿Qué marca es conocida por su modelo 911? a) Ferrari, b) Porsche, c) Lamborghini, d) Aston Martin", 
    #6
    "¿Cuál de estos autos es conocido como el auto del pueblo? a) Fiat 500, b) Citroën 2CV, c) Volkswagen Beetle, d) Mini Cooper"
    #7
    "¿Qué marca produce el superdeportivo Veyron? a) Lamborghini, b) Ferrari, c) Bugatti, d) McLaren",  
    #8
    "¿Qué auto eléctrico es producido por Tesla? a) Model X, b) Leaf, c) Bolt, d) i8" ,
    #9
    "¿Qué marca fue fundada por Enzo Ferrari? a) Maserati, b) Ferrari, c) Alfa Romeo, d) Lamborghini",  
    #10
    "¿Cuál es la marca de lujo de Toyota?  a) Acura, b) Infiniti, c) Lexus, d) Genesis",  
    #11
    "¿Qué auto es conocido por sus puertas de ala de gaviota? a) DeLorean DMC-12, b) Lamborghini Aventador, c) Ferrari LaFerrari, d) Porsche 918 ", 
    #12
    "¿En qué país se encuentra la sede de Volvo? a) Suecia, b) Alemania, c) Noruega, d) Estados Unidos ",
    #13
    "¿Qué auto fue popularmente conocido como Escarabajo? a) Citroën DS, b) Fiat 500, c) Volkswagen Beetle, d) Mini Cooper",
    #14
    "¿Qué marca produce el modelo Civic? a) Toyota, b) Nissan, c) Honda, d) Mazda ",
    #15
    "¿Cuál fue el primer auto deportivo producido por Lamborghini? a) Miura, b) Countach, c) Diablo, d) 350 GT",
    #16
    "¿Qué marca es conocida por sus autos híbridos Prius? a) Honda, b) Toyota, c) Nissan, d) Mitsubishi",
    #17
    "¿En qué año se lanzó el primer Ford Mustang?  a) 1955, b) 1964, c) 1970, d) 1980 ",
    #18
    "¿Qué marca de autos de lujo tiene un logo con un espíritu alado conocido como Espíritu del Éxtasis? a) Bentley, b) Rolls-Royce, c) Aston Martin, d) Jaguar ",
    #19
    "¿Cuál es el auto deportivo más famoso de Chevrolet?  a) Camaro, b) Corvette, c) Impala, d) Malibu",  
    #20
    "¿Qué marca alemana es conocida por el eslogan  Das Auto?  a) BMW, b) Audi, c) Volkswagen, d) Mercedes-Benz",  
    #21
    "¿Cuál fue el primer auto en superar oficialmente los 300 km/h en una prueba controlada?  a) Ferrari F40 b) Lamborghini Diablo c) McLaren F1 d) Porsche 959",
    #22
    "¿En qué año se lanzó el primer auto con frenos antibloqueo (ABS) de serie?  a) 1978 b) 1985 c) 1990 d) 1982",
    #23
    "¿Cuál es el nombre del sistema de tracción integral de Subaru?  a) 4Matic b) Symmetrical AWD c) Quattro d) xDrive",
    #24
    "¿Qué marca produjo el primer auto híbrido de producción masiva? a) Toyota b) Honda c) Nissan d) Ford",
    #25
    "¿Qué marca de autos tenía un modelo conocido como Cosmo Sport en la década de 1960? a) Toyota b) Nissan c) Mazda d) Mitsubishi",
    ]

# Lista de respuestas correctas
respuestas_correctas = [
    "d",  # Peugeot
    "c",  # Ford
    "b",  # Italia
    "a",  # Ford Model
    "b",  # Lamborghini
    "c",  # Volkswagen Beetle
    "c",  # Bugatti
    "a",  # Model X
    "b",  # Ferrari
    "c",  # Lexus 
    "a",  # DeLorean DMC-12
    "a",  # Suecia
    "c",  # Volkswagen Beetle
    "c",  # Honda
    "d",  # 350 GT
    "b",  # Toyota
    "b",  # 1964
    "b",  # Rolls-Royce
    "b",  # Corvette
    "c",  # Volkswagen
    "c",  # McLaren F1
    "a",  # 1978
    "b",  # Symmetrical AWD
    "a",  # Toyota
    "c",  # Mazda
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas_autos = [
    {"pregunta": preguntas_autos[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_autos))
]

# Función para jugar al juego de trivia
def Auto():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de autos!\n")

    for i, item in enumerate(preguntas_respuestas_autos):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_autos)}")
    if puntaje == len(preguntas_respuestas_autos):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_autos) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego


# Lista de preguntas con opciones
preguntas_cine = [
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
preguntas_respuestas_cine = [
    {"pregunta": preguntas_cine[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_cine))
]

# Función para jugar al juego de trivia
def Cine():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de Cine!\n")

    for i, item in enumerate(preguntas_respuestas_cine):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_cine)}")
    if puntaje == len(preguntas_respuestas_cine):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_cine) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego


preguntas_deporteGral = [
    #1
    "¿Cuál es el deporte más practicado a nivel mundial? A) Fútbol b) Baloncesto c) Natación d) Esgrima ",
    #2
    "¿Qué país ha ganado más Copas del Mundo de la FIFA en fútbol? a) Brasil b) Argentina c) Alemania d)EEUU",
    #3
    "¿Quién es el atleta con más medallas de oro en los Juegos Olímpicos de verano? a) Michael Phelps, b) Lebron James c) Ricardo Montaner d) Michael Jordan",
    #4
    "¿En qué año se celebraron los primeros Juegos Olímpicos modernos? a) 1896 b)1850 c)1990 d)1930",
    #5
    "¿Qué equipo ha ganado más títulos en la NBA? a)Boston Celtics b)Golden state Warriors c)Los Angeles Lakers d)Brooklyn Nets",
    #6
    "¿Qué deportista es conocido como “La Pantera Rosa” en el fútbol? a)Carlos “El Pibe” Valderrama b) Lionel Messi  c) Diego Armando Maradona d)",
    #7
    "¿Cuál es la distancia de una maratón en kilómetros? a)42.195 kilómetros b) 45.000 kilómetros c) 43.000 kilómetros d) 40.0000 kilómetros",
    #8
    "¿Qué deporte se juega en una cancha con una red en el centro y se utiliza una raqueta? a)Tenis b)Voleibol c)Pádel d)Tenis de mesa",
    #9
    "¿Quién es el tenista con más Grand Slam en la historia del tenis? a) Novak Djokovic b) Rafael Nadal c) Roger Federer d) Jannik Sinner ",
    #10
    "¿Qué evento deportivo se celebra cada cuatro años y reúne a los mejores atletas de invierno? a) Juegos Olímpicos de Invierno b) Juegos Olímpicos de Verano c) Juego Olímpicos de la juventud d) Juegos Paralímpicos",
    #11
    "¿Qué país es famoso por su deporte nacional, el cricket? a)India b)EEUU c)Japón d)Rusia",
    #12
    "¿Cuál es el nombre del torneo de tenis que se juega en Wimbledon? a) El Torneo de Wimbledon b)US open c)Torneo de Roland Garros d)ASB Classic Auckland",
    #13
    "¿En qué deporte se utiliza un balón ovalado y se juega con el objetivo de anotar tries? a) Rugby b) Bádminton c) Soccer d) Baloncesto ",
    #14
    "¿Qué equipo de fútbol español ha ganado más títulos de La Liga? a)Real Madrid, b)fc Barcelona, c)Paris Saint Germain, d)Real Betis Balompié",
    #15
    "¿Cuál es el deporte más popular en Estados Unidos? A)Fútbol americano b)Baloncesto c)Soccer d) béisbol",
    #16
    "¿Qué tipo de carrera es el Tour de Francia? a) Una carrera de ciclismo b) Un triatlón c) Un maratón d) Una competencia de relevos",
    #17
    "¿Qué deporte se juega con una pelota que se lanza a una canasta a una altura de 3,05 metros? a)Baloncesto b) Golf c)Curling d) Lanzamiento de bala",
    #18
    "¿Qué atleta es conocido como “El Reloj” y es famoso por su habilidad en la esgrima? a) Mariel Zagunis b) Zhong Weiping c)Valentina Vezzali d)Stanislav Pozdnyakov",
    #19
    "¿Cuál es el nombre del campeonato mundial de automovilismo que se celebra anualmente? a) Fórmula 1 b) Turismo c)NASCAR Cup Series d)24 horas de Le Mans",
    #20
    "¿Qué deporte combina elementos de natación, ciclismo y carrera en una sola competencia? a) Triatlón b) Ultraman c) Ironman d) Todas las acciones son correctas ",
    #21
    "¿Cuál es el club que tiene más fanáticos en el mundo? a)Club Atlético Independiente b)Galatasaray SK c)Borussia Dortmund d) Real Madrid" , 
    #22
    "¿Cuál es la cancha más conocida en el mundo? a)Estadio Benito Villamarín b)Estadio Nacional de Chile c)Estadio de Wembley d)Estadio de San Mamés",
    #23
    "¿Qué deportista ha vendido más camisetas en su carrera? a)Rafael Nadal b)Cristiano Ronaldo c)Usain Bolt d)Tiger Woods",
    #24
    "¿Qué países no han participado en un campeonato del mundo? a)Liechtenstein, b)Brasil c)Francia d)Guinea-Bisáu",
    #25
    "¿Cuál fue la primera disciplina que se consideró deporte? a)Atletismo b)Esgrima c)Boxeo d)Lucha"
]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "a",  # Fútbol
    "a",  # Brasil
    "a",  # Michael Phelps
    "a",  # 1896
    "a",  # Boston Celtics
    "a",  # Carlos “El Pibe” Valderrama
    "a",  # 42.195 kilómetros
    "a",  # Tenis
    "a",  # Novak Djokovic
    "a",  # Juegos Olímpicos de Invierno
    "a",  # India
    "a",  # El Torneo de Wimbledon
    "a",  # Rugby 
    "a",  # Real Madrid
    "a",  # Fútbol americano 
    "a",  # Una carrera de ciclismo 
    "a",  # Baloncesto 
    "a",  # Mariel Zagunis
    "a",  # Fórmula 1
    "d",  # Todas las opciones son correctas
    "d",  # Real Madrid 
    "c",  # Estadio de Wembley
    "b",  # Cristiano Ronaldo
    "a",  # Liechtenstein
    "d"   # Lucha 
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas_deporte = [
    {"pregunta": preguntas_deporteGral[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_deporteGral))
]

# Función para jugar al juego de trivia
def DeporteGral():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de Deporte General!\n")

    for i, item in enumerate(preguntas_respuestas_deporte):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_deporte)}")
    if puntaje == len(preguntas_respuestas_deporte):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_deporte) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego


# Lista de preguntas con opciones
preguntas_formula = [
        #1
        "En que circuito se establecio el record de la vuelta mas rapida? a)Nurburgring b)Monza c)Monaco d)Silverstone",
        #2
        "Cuanto duró la carrera mas larga de la historia de Formula 1? a)3 dias b)3h 30m 25s c)4h 4m 39s d)4h 19m 22s",
        #3
        "Cuantos puntos vale el primer puesto cuando terminas la carrera? a)18 pts b)25 pts c)22 pts d)30 pts",
        #4
        "Que motor utiliza Red Bull en sus autos Formula 1 2024? a)PU106C Hybrid b)Mercedes-AMG F1 M15 c)TAG Heuer R.E.18 V6 Turbo d)Honda RBPTH002 ",
        #5
        "Cuantos mecanicos hay en una parada de pits? a)12 b)20 c)15 d)8",
        #6
        "En que pais se disputo el primer gran premio de la temporada 2020? a)Australia b)Alemania c)España d)Mexico",
        #7
        "Quien fue el campeon mundial de la formula 1 en 2019? a)Lewis Hamilton b)Fernando Alonso c)Niki Lauda d)Max Verstappen",
        #8
        "Cuantas veces fue campeon munial Juan Manuel Fangio? a)más de 5 b)3 c)ninguno d)5",
        #9
        "Cuantos muniales en Formula 1 tiene Max Verstappen? a)1 b)3 c)más de 3 d)2",
        #10
        "Cuantos pilotos corren en cada carrera?  a)20 b)15 c)10 d)22",
        #11
        "Cual es la marca con mas campeonatos de constructores? a)McLaren b)Mercedes c)Ferrari d)Red Bull",
        #12
        "En que año se fundo la Formula 1? a)1890 b)1954 c)1950 d)1960",
        #13
        "En que categoria compiten los de la Formula 1? a)Gt b)Turismo c)Nascar d)Monoplazas",
        #14
        "Cual fue el ultimo piloto en perder la vida? a)Jules Bianchi b)Niki Lauda c)Ayrton Senna d)David Ferrer",
        #15
        "Cual es el circuito con mas vueltas hechas? a)Hungaroring b)Red Bull Ring c)Spa-Francorchamps d)Silverstone",
        #16
        "De que color son los neumaticos de categoria Hard? a)Azul b)Rojo c)Amarillod)Rosa",
        #17
        "De que color son los neumaticos de categoria Soft?  a)Morado b)Blanco c)Naranja d)Amarillo",
        #18
        "De que color son los neumaticos de categoria Medium? a)Blanco b)Morado c)Rojo d)Azul",
        #19
        "Cual es el circuito mas famoso del mundo? a)Nurburgring b)Spa-Francorchamps c)Silverstone d)Monaco",
        #20
        "Quien tiene la vuelta mas rapida de Formula 1 en la hitoria? a)Max Verstappen b)Fernando Alonso c)Lewis Hamilton d)Niki Lauda",
        #21
        "Que piloto dijo la iconica frace 'El muro se movio'? a)Niki Lauda b)Fernando Alonso c)Aryton Senna d)David Ferrare",
        #22
        "Cuantas banderas hay en Formula 1? a)6 b)9 c)3 d)5",
        #23
        "Quienes son los pilotos con mas poseedores de titulos mundiales? a)Lewis Hamilton y Niki Lauda b) Max Verstappen y Juan Manuel Fangio c) Lewis Hamilton y Michael Schaumer d)Niki Lauda y Max Verstappen",
        #24
        "En que año entro McLaren en la competencia de Formula 1? a) 1996 b) 1955 c) 1976 d) 1992",
        #25
        "Que piloto fue el primero en morir en Nurburgring? a)Lorenzo Bandini b)Cenek Junek c)Ayrton Senna d)Jules Bianchi"
]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "b",  # Monza 
    "c",  # 4h 4m 39s
    "b",  # 25 pts
    "d",  # Honda RBPTH002
    "b",  # 20
    "a",  # Australia
    "a",  # Lewis Hamilton
    "d",  # 5
    "b",  # 3
    "a",  # 20
    "c",  # Ferrari
    "c",  # 1950
    "d",  # Monoplaza
    "d",  # David Ferrer
    "b",  # Red Bull Ring
    "a",  # Azul
    "d",  # Amarillo
    "a",  # Blanco
    "d",  # Monaco
    "d",  # Niki Lauda
    "c",  # Aryton Senna
    "b",  # 9
    "c",  # Lewis Hamilton y Michael Schumacher
    "a",  # 1996
    "b"   # Cenek Junek
]
# Lista con las preguntas y respuestas correctas
preguntas_respuestas_formula = [
    {"pregunta": preguntas_formula[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_formula))
]

# Función para jugar al juego de trivia
def Formula():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de Formula 1!\n")

    for i, item in enumerate(preguntas_respuestas_formula):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_formula)}")
    if puntaje == len(preguntas_respuestas_formula):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_formula) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego


# Lista de preguntas con opciones
preguntas_futbol = [
    #1
    "¿Qué selección ha ganado más Copas del Mundo? a) Brasil b) Alemania c) Italia d) Argentina",
    #2
    "¿En qué año Argentina ganó su primer Mundial de fútbol? a) 1974 b) 1978 c) 1986 d) 1990",
    #3
    "¿Cuál es el club con más títulos de la UEFA Champions League? a) AC Milan b) FC Barcelona c) Real Madrid d) Bayern Múnich",
    #4
    "¿Qué jugador fue transferido por una cifra récord de 222 millones de euros en 2017? a) Cristiano Ronaldo b) Neymar Jr. c) Lionel Messi d) Kylian Mbappé",
    #5
    "¿Qué equipo ganó la Premier League en la temporada 2015-2016? a) Manchester City b) Leicester City c) Chelsea d) Liverpool",
    #6
    "¿Cuál es el máximo goleador en la historia de la selección de Portugal? a) Eusébio b) Pauleta c) Cristiano Ronaldo d) Luís Figo",
    #7
    "¿Qué equipo es conocido como 'Los Diablos Rojos'? a) Manchester United b) AC Milan c) Independiente d) Bayern Múnich",
    #8
    "¿Quién ganó el Balón de Oro en 2021? a) Lionel Messi b) Robert Lewandowski c) Karim Benzema d) Cristiano Ronaldo",
    #9
    "¿Qué selección ganó la Eurocopa en 2004? a) Portugal b) Francia c) Italia d) Grecia",
    #10
    "¿Qué club argentino tiene más títulos de la Copa Libertadores? a) River Plate b) Boca Juniors c) Independiente d) Racing Club",
    #11
    "¿En qué estadio juega el FC Barcelona? a) Santiago Bernabéu b) Camp Nou c) Anfield d) Allianz Arena",
    #12
    "¿Qué entrenador ha ganado más Champions League como entrenador? a) Carlo Ancelotti b) Pep Guardiola c) Sir Alex Ferguson d) Zinedine Zidane",
    #13
    "¿Qué país ganó la Copa América 2021? a) Argentina b) Brasil c) Chile d) Uruguay",
    #14
    "¿Qué equipo español ha ganado más títulos de La Liga? a) Atlético Madrid b) Real Madrid c) Valencia d) FC Barcelona",
    #15
    "¿En qué equipo jugó Diego Maradona entre 1984 y 1991? a) FC Barcelona b) Sevilla FC c) SSC Napoli d) Boca Juniors",
    #16
    "¿Qué país fue anfitrión del Mundial de fútbol en 2014? a) Sudáfrica b) Brasil c) Alemania d) Rusia",
    #17
    "¿Qué selección tiene el récord de más victorias consecutivas en los Mundiales? a) Alemania b) Italia c) Brasil d) Francia",
    #18
    "¿Qué equipo de la Serie A ha ganado más títulos de liga? a) Juventus b) AC Milan c) Inter de Milán d) AS Roma",
    #19
    "¿Cuál es el club más antiguo del mundo aún en existencia? a) Sheffield FC b) Notts County c) Preston North End d) Aston Villa",
    #20
    "¿Qué selección ganó la primera Copa del Mundo en 1930? a) Argentina b) Brasil c) Italia d) Uruguay"
    #21
    "¿Que club tiene mas Champions? a) Barcelona b) Sarmiento de Junin c) Real Madrid d) Liverpool",
    #22
    "¿Que seleccion gano el mundial de 2022? a) Argentina b) Francia c) Italia d) Alemania",
    #23
    "¿Contra que Equipo jugo Uruguay la final del mundial de 1930? a) Brasil b) Paraguay c) Argentina d) Colombia",
    #24
    "¿Como se llamaba el balon del mundial Sudafrica 2010? a) Jabulani b) Telstar c) Oliva d) Tango",
    #25
    "¿Que seleccion de futbol fue conocida como La Naranja Mecanica? a) La Brasil del 1970 b) La Alemania de 2014 c) La Argentina de 1978  d) La Holanda del 1974"

]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "a",  # Brasil
    "b",  # 1978
    "c",  # Real Madrid
    "b",  # Neymar Jr.
    "b",  # Leicester City
    "c",  # Cristiano Ronaldo
    "a",  # Manchester United
    "a",  # Lionel Messi
    "d",  # Grecia
    "c",  # Independiente
    "b",  # Camp Nou
    "a",  # Carlo Ancelotti
    "a",  # Argentina
    "b",  # Real Madrid
    "c",  # SSC Napoli
    "b",  # Brasil
    "c",  # Brasil
    "a",  # Juventus
    "a",  # Sheffield FC
    "d",  # Uruguay
    "c",  # Real Madrid 
    "a",  # Argentina
    "c",  # Argentina
    "a",  # Jabulani
    "d"   # La Holanda del 1974

]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas_futbol = [
    {"pregunta": preguntas_futbol[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_futbol))
]

# Función para jugar al juego de trivia
def Futbol():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de fútbol!\n")

    for i, item in enumerate(preguntas_respuestas_futbol):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_futbol)}")
    if puntaje == len(preguntas_respuestas_futbol):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_futbol) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego

# Lista de preguntas con opciones
preguntas_videojuego = [
    #1
    '¿Cuál de los siguientes personajes es el protagonista principal en la serie de videojuegos "The Legend of Zelda"? a) Ganondorf b) Link c) Zelda d) Navi',
    #2
    '¿En qué año se lanzó el videojuego "Super Mario Bros." para la consola NES? a) 1983 b) 1985 c) 1987 d) 1989',
    #3
    '¿Cuál es el nombre del mundo en el que se desarrolla la saga de "Final Fantasy VII"? a) Eorzea b) Spira c) Gaia d) Ivalice',
    #4
    '¿Cuál de estos juegos fue desarrollado por Rockstar Games? a) The Elder Scrolls V: Skyrim b) Grand Theft Auto V c) Dark Souls d) Halo: Combat Evolved',
    #5
    "¿En qué juego de la saga “The Legend of Zelda” se explora un mundo subterráneo conocido como el" '"Inframundo"'"? a) The Legend of Zelda: A Link to the Past b) The Legend of Zelda: Ocarina of Time c) The Legend of Zelda: Breath of the Wild d) The Legend of Zelda: Majora's Mask" 
    #6
    '¿En qué juego de disparos en primera persona puedes jugar como el personaje Master Chief? a) Destiny b) Battlefield c) Call of Duty d) Halo',
    #7
    '¿Cuál de estos videojuegos pertenece a la serie de rol conocida por sus batallas y exploración en el mundo de "Eorzea"? a) Final Fantasy XIV b) Dragon Age: Inquisition c)World of Warcraft d) Elder Scrolls Online',
    #8
    '¿En qué juego se encuentra el personaje llamado “Pac-Man”? a) Donkey Kong b) Space Invaders c) Pac-Man d) Galaga',
    #9
    '¿Qué tipo de juego es “Among Us”? a) Juego de plataformas b) Juego de rol c) Juego de misterio social d) Shooter en primera persona',
    #10
    '¿Cuál de los siguientes juegos es un título clásico de la consola Sega Genesis? a) Sonic the Hedgehog b) Super Mario World c) The Legend of Zelda: Ocarina of Time d) Donkey Kong Country',
    #11
    '¿En qué serie de videojuegos luchan los personajes conocidos como "Hunters" contra monstruos gigantes? a) Horizon Zero Dawn b) Dark Souls c) Bloodborne d) Monster Hunter',
    #12
    '¿Cuál de estos videojuegos fue creado por la compañía Nintendo? a) Metal Gear Solid b) Final Fantasy c) The Legend of Zelda d) Fallout'
    #13
    '¿Cuál es el objetivo principal en el juego “Minecraft”? a) Completar una campaña de historia b) Construir y explorar c) Ganar en batallas en línea d) Resolver rompecabezas',
    #14
    '¿En qué juego puedes encontrar el "Pikachu" como uno de los personajes principales? a) Pokémon b) Digimon c) Yu-Gi-Oh! d) Final Fantasy',
    #15
    '¿Qué videojuego se ambienta en una ciudad ficticia llamada Raccoon City? a) Silent Hill b) Resident Evil c) Dead Space d) Outlast',
    #16
    '¿Qué videojuego es conocido por introducir el personaje "Kratos" en un mundo de mitología griega? a) God of War b) Dante’s Inferno c) Castlevania d) Demon’s Souls',
    #17
    '¿Cuál es el nombre del universo de "Mass Effect"? a) The Elder Scrolls b) The Halo Universe c) The Mass Effect Universe d) The Star Wars Universe',
    #18
    '¿Qué videojuego se desarrolla en el universo de Star Wars y se centra en combates espaciales? a) Star Wars: Knights of the Old Republic b) Star Wars: Battlefront c) Star Wars: Jedi: Fallen Order d) Star Wars: The Old Republic',
    #19
    '¿En qué tipo de juego se basa el título “The Witcher 3: Wild Hunt”? a) Juego de rol de acción b) Juego de estrategia en tiempo real c) Juego de disparos en primera persona d) Juego de plataformas ',
    #20
    '¿Qué videojuego es conocido por sus mapas y escenarios destructibles y fue creado por DICE? a) Call of Duty b) Battlefield c) Rainbow Six Siege d) Counter-Strike',
    #21
    '¿En qué juego puedes encontrar el personaje llamado “Ellie” como uno de los protagonistas? a) The Last of Us b) Uncharted c) Red Dead Redemption d) God of War',
    #22
    '¿Cuál de estos videojuegos es conocido por su mecánica de combate basada en el uso de espadas y magia? a) Skyrim b) Dark Souls c) Overwatch d) Apex Legends',
    #23
    '¿En qué juego se destacan la construcción de estructuras y la defensa contra enemigos en un entorno de supervivencia? a) Rust b) Fornite c) ARK: Survival Evolved d) Conan Exiles',
    #24
    '¿En qué salio el juego World of Warcraft? a) 1998 b) 2002 c) 2000 d) 2004',
    #25
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
preguntas_respuestas_juegos = [
    {"pregunta": preguntas_videojuego[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_videojuego))
]

# Función para jugar al juego de trivia
def VideoJuegos():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de Videojuegos\n")

    for i, item in enumerate(preguntas_respuestas_juegos):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_juegos)}")
    if puntaje == len(preguntas_respuestas_juegos):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_juegos) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego

# Lista de preguntas con opciones
preguntas_CienNat=[
    #1
    '¿Cuál es el órgano principal del sistema circulatorio? a) Pulmón b) Hígado c) Corazón d) Riñón', 
    #2
    '¿Qué tipo de roca se forma a partir del enfriamiento del magma? a) Sedimentaria b) Ígnea c) Metamórfica d) Orgánica',
    #3
    '¿Cuál es el proceso mediante el cual las plantas producen su alimento? a) Respiración b) Fotosíntesis c) Digestión d) Fermentación',
    #4
    '¿Qué gas es fundamental para la respiración de los seres humanos? a) Dióxido de carbono b) Nitrógeno c) Hidrógeno d) Oxígeno',
    #5
    '¿Qué parte de la célula controla sus funciones? a) Citoplasma b) Membrana celular c) Núcleo d) Pared celular',
    #6
    '¿Qué es la biodiversidad? a) Variedad de especies b) Variedad de ecosistemas c) Variedad de climas d) Variedad de suelos',
    #7
    '¿Cuál de los siguientes es un mamífero? a) Cocodrilo b) Pingüino c) Ballena d)Tortuga ',
    #8
    '¿Qué tipo de energía proviene del sol? a) Energía eólica b) Energía solar c) Energía geotérmica d) Energía hidráulica',
    #9
    '¿Cuál es la función principal de los riñones? a) Filtrar la sangre b) Bombear sangre c) Producir hormonas d)Regular la temperatura ',
    #10
    '¿Qué parte de la planta absorbe agua y minerales del suelo? a) Hoja b) Tallo c) Raíz d) Flor',
    #11
    '¿Cuál es la unidad básica de la vida? a) Tejido b) Célula c) Órgano d) Sistema ',
    #12
    '¿Cuál es el gas más abundante en la atmósfera terrestre? a) Oxígeno b) Dióxido de carbono c) Nitrógeno d) Argón',
    #13
    '¿Qué tipo de roca se forma a partir de la solidificación del magma? a) Sedimentaria b) Metamórfica c) Ígnea d) Volcánica',
    #14
    '¿Cuál es la función de los glóbulos rojos en la sangre? a) Combatir infecciones b) Transportar oxígeno c) Coagulación d) Regular temperatura',
    #15
    '¿Qué es el ciclo del agua? a) Movimiento de las placas tectónicas b) Proceso de respiración de las plantas c) Evolución de los ecosistemas d) Circulación del agua en la Tierra',
    #16
    '¿Qué tipo de energía se produce a partir de la descomposición de materia orgánica? a) Energía solar b) Energía biomásica c) Energía eólica d) Energía geotérmica',
    #17
    '¿Cuál es el principal componente del aire que respiramos? a) Oxígeno b) Dióxido de carbono c) Helio d) Hidrógeno',
    #18
    '¿Qué estructura celular es responsable de la producción de energía? a) Ribosomas b) Mitocondrias c) Lisosomas d) Núcleo',
    #19
    '¿Qué tipo de energía se genera a partir del viento? a) Energía solar b) Energía hidroeléctrica c) Energía eólica d) Energía nuclear',
    #20
    '¿Qué parte del cerebro controla las funciones involuntarias? a) Corteza cerebral b) Cerebelo c) Tronco encefálico d) Hipotálamo'
    #21
    '¿Cuál es el proceso por el cual el agua se convierte en vapor? a) Evaporación b) Condensación c) Precipitación d) Sublimación',
    #22
    '¿Qué tipo de cambio ocurre cuando se quema papel? a) Cambio físico b) Cambio químico c) Cambio de estado d) Cambio mecánico',
    #23
    '¿Qué tipo de energía se obtiene de los combustibles fósiles? a) Energía solar b) Energía cinética c) Energía química d) Energía eléctrica',
    #24
    '¿Qué elemento químico es esencial para la respiración celular? a) Oxígeno b) Hidrógeno c) Nitrógeno d) Carbono',
    #25
    '¿Cuál es el principal agente erosivo en el medio ambiente? a) Viento b) Temperatura c) Luz solar d) Agua'
]

# Lista de respuestas correctas
respuestas_correctas = [
    "c",  # Corazón (1)
    "b",  # Ígnea (2)
    "b",  # Fotosíntesis (3)
    "d",  # Oxígeno (4)
    "c",  # Núcleo (5)
    "a",  # Variedad de especies (6)
    "c",  # Ballena (7)
    "b",  # Energía solar (8)
    "a",  # Filtrar la sangre (9)
    "c",  # Raíz (10)
    "b",  # Célula (11)
    "c",  # Nitrógeno (12)*4
    "c",  # Ígnea (13)
    "b",  # Transportar oxígeno (14)
    "d",  # Circulación del agua en la Tierra (15)
    "b",  # Energía biomásica (16)
    "a",  # Oxígeno (17)
    "b",  # Mitocondrias  (18)
    "c",  # Energía eólica (19)
    "c",  # Tronco encefálico (20)
    "a",  # Evaporación (21)
    "b",  # Cambio químico (22)
    "c",  # Energía química (23)
    "a",  # Oxígeno (24)
    "d"  # Agua (25)
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas_CienNat = [
    {"pregunta": preguntas_CienNat[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_CienNat))
]

# Función para jugar al juego de trivia
def CienNat():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de ciencias naturales !\n")

    for i, item in enumerate(preguntas_respuestas_CienNat):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas_CienNat)}")
    if puntaje == len(preguntas_respuestas_CienNat):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas_CienNat) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

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
def CulGen():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de cultura general!\n")

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

# Lista de preguntas con opciones
preguntas_animales = [
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
    print("¡Bienvenido al juego de trivia de animales!\n")

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