from FuncionesJuego import JugarNivel


def JuegoPreguntas():

    preguntasNivel1 = [
        {
            "pregunta": "¿Qué animal es conocido por su gran trompa?",
            "opciones": ["1. Elefante", "2. León", "3. Jirafa"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Cuál de estos animales es un mamífero marino?",
            "opciones": ["1. Delfín", "2. León", "3. Tigre"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Qué animal se caracteriza por tener rayas en su pelaje?",
            "opciones": ["1. Elefante", "2. Cebra", "3. Rinoceronte"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales es un reptil?",
            "opciones": ["1. Ballena", "2. Cocodrilo", "3. Delfín"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Qué animal es conocido por ser el rey de la selva?",
            "opciones": ["1. Tigre", "2. León", "3. Oso"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales vuela?",
            "opciones": ["1. Elefante", "2. León", "3. Águila"],
            "respuesta_correcta": 3,
        },
        {
            "pregunta": "¿Qué animal es conocido por ser un depredador marino?",
            "opciones": ["1. León", "2. Tiburón", "3. Cocodrilo"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales tiene aletas y branquias?",
            "opciones": ["1. Ballena", "2. Delfín", "3. Tiburón"],
            "respuesta_correcta": 3,
        },
        {
            "pregunta": "¿Qué animal es conocido por ser el más grande del mundo?",
            "opciones": ["1. Elefante", "2. Ballena Azul", "3. Jirafa"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales es un marsupial?",
            "opciones": ["1. Canguro", "2. León", "3. Tigre"],
            "respuesta_correcta": 1,
        },
    ]

    preguntasNivel2 = [
        {
            "pregunta": "¿Cuál de los siguientes es un animal abiótico?",
            "opciones": ["1. León", "2. Cactus", "3. Pingüino"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales es un reptil?",
            "opciones": ["1. Ballena", "2. Serpiente", "3. Gorila"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Qué animal es un mamífero marino?",
            "opciones": ["1. Tortuga", "2. Delfín", "3. Cocodrilo"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales es carnívoro?",
            "opciones": ["1. Vaca", "2. León", "3. Caballo"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Qué animal tiene como característica principal el plumaje?",
            "opciones": ["1. Pez", "2. Pájaro", "3. Tortuga"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales es un insecto?",
            "opciones": ["1. Araña", "2. Abeja", "3. Serpiente"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Qué animal es conocido por su aguijón venenoso?",
            "opciones": ["1. Avispa", "2. Hormiga", "3. Escarabajo"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Cuál de estos animales es ovíparo?",
            "opciones": ["1. León", "2. Cocodrilo", "3. Pato"],
            "respuesta_correcta": 3,
        },
        {
            "pregunta": "¿Qué animal es un herbívoro rumiante?",
            "opciones": ["1. Tigre", "2. Vaca", "3. Lobo"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Cuál de estos animales es conocido por su larga lengua?",
            "opciones": ["1. León", "2. Jirafa", "3. Oso"],
            "respuesta_correcta": 2,
        },
    ]

    preguntasNivel3 = [
        {
            "pregunta": "¿Cuál de estos animales es ovíparo?",
            "opciones": ["1. Ballena", "2. Tigre", "3. Rana"],
            "respuesta_correcta": 3,
        },
        {
            "pregunta": "¿Qué animal es conocido por ser un parásito del ser humano?",
            "opciones": ["1. Pulga", "2. Mariposa", "3. Abeja"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Cuál de estos animales tiene un sistema de ecolocación?",
            "opciones": ["1. Murciélago", "2. Serpiente", "3. Lobo"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Qué animal es capaz de cambiar de color para camuflarse?",
            "opciones": ["1. Camaleón", "2. Tortuga", "3. Cocodrilo"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Cuál de estos animales es venenoso y mortal?",
            "opciones": ["1. Medusa", "2. Estrella de Mar", "3. Pez Payaso"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Qué animal es conocido por ser el más rápido en tierra?",
            "opciones": ["1. Guepardo", "2. León", "3. Elefante"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Cuál de estos animales tiene un cerebro muy desarrollado similar al humano?",
            "opciones": ["1. Chimpancé", "2. Tigre", "3. Serpiente"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Qué animal es capaz de regenerar partes de su cuerpo?",
            "opciones": ["1. Estrella de Mar", "2. Tiburón", "3. Tortuga"],
            "respuesta_correcta": 1,
        },
        {
            "pregunta": "¿Cuál de estos animales es conocido por su longevidad?",
            "opciones": ["1. Elefante", "2. Tortuga", "3. León"],
            "respuesta_correcta": 2,
        },
        {
            "pregunta": "¿Qué animal tiene un órgano llamado buche para almacenar alimentos?",
            "opciones": ["1. Pollo", "2. Cocodrilo", "3. Elefante"],
            "respuesta_correcta": 1,
        },
    ]

    niveles = [
        (preguntasNivel1, 70),  # Nivel 1
        (preguntasNivel2, 130),  # Nivel 2
        (preguntasNivel3, 190),  # Nivel 3 (requiere 190 puntos para jugar)
    ]

    # Puntuación inicial del jugador
    puntuacion = 0

    # Iterar sobre cada nivel y jugar
    for i, (preguntas, puntosParaPasar) in enumerate(niveles):
        # Mostrar el número de nivel actual
        print(f"\n--- Nivel {i + 1} ---")

        # Verificar si es el nivel 3 y el jugador no tiene suficientes puntos
        if i == 2 and puntuacion < puntosParaPasar:
            print("No tienes suficientes puntos para desbloquear este nivel.")
            continue  # Pasar al siguiente nivel o terminar el juego según lo deseado

        # Jugar el nivel actual y actualizar la puntuación del jugador
        puntuacion = JugarNivel(preguntas, puntuacion)

        # Verificar si el jugador no alcanzó el puntaje mínimo para pasar al siguiente nivel
        if puntuacion < puntosParaPasar:
            # Mostrar un mensaje de que el jugador no pasó el nivel
            print(
                f"No alcanzaste los {puntosParaPasar} puntos necesarios para pasar al siguiente nivel."
            )
            # Preguntar al jugador si desea volver a intentar el juego
            if input("¿Quieres volver a intentar el juego? (s/n): ").lower() == "s":
                # Si el jugador quiere volver a intentarlo, reiniciar el juego
                JuegoPreguntas()
            else:
                # Si el jugador no quiere volver a intentarlo, mostrar la puntuación final y terminar el juego
                print(f"Juego terminado. Tu puntuación final es: {puntuacion}")
            return

    # Si el jugador completa todos los niveles exitosamente, mostrar la puntuación final
    print(
        f"¡Felicitaciones! Has completado todos los niveles. Tu puntuación final es: {puntuacion}"
    )

# Iniciar el juego
JuegoPreguntas()
