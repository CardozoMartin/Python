

def MostrarPregunta(pregunta):
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)

def ObtenerRespuesta():
    respuesta = input("Ingrese el número de su respuesta (1, 2, o 3): ")
    if respuesta in ['1', '2', '3']:
        return int(respuesta)
    else:
        print("Por favor, ingrese un número válido (1, 2, o 3).")
        return ObtenerRespuesta()

def EvaluarRespuesta(respuesta, respuestaCorrecta):
    if respuesta == respuestaCorrecta:
        print("¡Correcto!")
        
        return 10
    else:
        print("Incorrecto.")
        
        return 0

def JugarNivel(preguntas , puntuacion):
    for pregunta in preguntas:
        MostrarPregunta(pregunta)
        respuesta = ObtenerRespuesta()
        puntuacion += EvaluarRespuesta(respuesta, pregunta["respuesta_correcta"])
        print(f"Tu puntuación actual es: {puntuacion}\n")
    return puntuacion
