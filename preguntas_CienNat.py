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
def Auto():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de autos!\n")

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