from colorama import Fore, Style


def MostrarPregunta(pregunta):
    print(Fore.BLUE + pregunta["pregunta"])
    for idx, opcion in enumerate(pregunta["opciones"], 1):
        print(Fore.BLUE + f"{idx}. {opcion}")
    print(Fore.BLUE + "0. Abandonar el juego")


def ObtenerRespuesta():
    respuesta = input(
        Fore.CYAN + "Ingrese el número de su respuesta (1, 2, 3) o 0 para abandonar: "
    )
    if respuesta in ["0", "1", "2", "3"]:
        return int(respuesta)
    else:
        print(Fore.RED + "Por favor, ingrese un número válido (0, 1, 2, 3).")
        return ObtenerRespuesta()


def EvaluarRespuesta(respuesta, respuestaCorrecta):
    if respuesta == respuestaCorrecta:
        print(Fore.GREEN + "¡Correcto!")
        return 10
    else:
        print(Fore.RED + "Incorrecto.")
        return 0


def JugarNivel(preguntas, puntuacion):
    for pregunta in preguntas:
        limpiar_consola()
        MostrarPregunta(pregunta)
        respuesta = ObtenerRespuesta()
        if respuesta == 0:
            limpiar_consola()
            print(Fore.YELLOW + "Has decidido abandonar el juego. ¡Hasta la próxima!")
            return (
                puntuacion,
                True,
            )  # Devolver la puntuación y un indicador de que el juego fue abandonado
        puntuacion += EvaluarRespuesta(respuesta, pregunta["respuesta_correcta"])
        print(Fore.CYAN + f"Tu puntuación actual es: {puntuacion}\n")
    return (
        puntuacion,
        False,
    )  # Devolver la puntuación y un indicador de que el juego continúa
