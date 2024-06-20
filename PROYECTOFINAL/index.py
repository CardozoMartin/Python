import os
import json
from FuncionesJuego import JugarNivel
from preguntas import preguntasNivel1, preguntasNivel2, preguntasNivel3
from colorama import init, Fore, Style

init(autoreset=True)  # Inicializar colorama

RANKING_FILE = "ranking.json"


def limpiar_consola():
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Unix (Linux y macOS)
        os.system("clear")


def descripcion_del_juego():
    print(Fore.MAGENTA + "Bienvenido al Juego de Preguntas de Biología.")
    print(
        Fore.MAGENTA
        + "En este juego, se te presentarán preguntas de opción múltiple sobre animales."
    )
    print(Fore.MAGENTA + "El juego está dividido en niveles de dificultad creciente.")
    print(
        Fore.MAGENTA
        + "Deberás seleccionar la respuesta correcta ingresando el número correspondiente."
    )
    print(
        Fore.MAGENTA
        + "Puedes abandonar el juego en cualquier momento ingresando '0' como respuesta."
    )
    print(
        Fore.MAGENTA
        + "Tu puntuación se irá acumulando a medida que respondas correctamente."
    )
    print(Fore.MAGENTA + "¡Buena suerte y diviértete!")


def guardar_ranking(nombre, puntuacion):
    try:
        with open(RANKING_FILE, "r") as file:
            ranking = json.load(file)
    except FileNotFoundError:
        ranking = []

    ranking.append({"nombre": nombre, "puntuacion": puntuacion})

    with open(RANKING_FILE, "w") as file:
        json.dump(ranking, file)


def mostrar_ranking():
    try:
        with open(RANKING_FILE, "r") as file:
            ranking = json.load(file)
    except FileNotFoundError:
        print(Fore.RED + "No hay datos de ranking disponibles.")
        return

    print(Fore.CYAN + "\n--- Ranking ---")
    for entry in sorted(ranking, key=lambda x: x["puntuacion"], reverse=True):
        print(Fore.CYAN + f"{entry['nombre']}: {entry['puntuacion']} puntos")


def JuegoPreguntas():
    niveles = [
        (preguntasNivel1, 70),  # Nivel 1
        (preguntasNivel2, 130),  # Nivel 2
        (preguntasNivel3, 190),  # Nivel 3 (referencia de puntos)
    ]

    # Puntuación inicial del jugador
    puntuacion = 0

    # Pedir nombre del jugador
    nombre = input(Fore.CYAN + "Ingrese su nombre: ")

    # Mostrar menú inicial para seleccionar el nivel de inicio
    while True:
        limpiar_consola()
        print(Fore.GREEN + "BIENVENIDO")
        print(Fore.CYAN + "\n--- Menú de Inicio ---")
        print(Fore.CYAN + "1. Comenzar desde el Nivel 1")
        print(Fore.CYAN + "2. Comenzar desde el Nivel 2")
        print(Fore.CYAN + "3. Comenzar desde el Nivel 3")
        print(Fore.CYAN + "4. Ver el ranking")
        print(Fore.CYAN + "5. Abandonar el juego")
        eleccion = input(Fore.CYAN + "Selecciona una opción (1/2/3/4/5): ")

        if eleccion in ["1", "2", "3"]:
            nivel_inicial = int(eleccion) - 1
            break
        elif eleccion == "4":
            limpiar_consola()
            mostrar_ranking()
            input(Fore.CYAN + "Presiona Enter para volver al menú.")
        elif eleccion == "5":
            limpiar_consola()
            print(Fore.YELLOW + "Has decidido abandonar el juego. ¡Hasta la próxima!")
            return
        else:
            limpiar_consola()
            print(Fore.RED + "Selección inválida. Por favor, elige 1, 2, 3, 4 o 5.")

    # Iterar sobre cada nivel y jugar desde el nivel inicial seleccionado
    for i in range(nivel_inicial, len(niveles)):
        limpiar_consola()
        preguntas, _ = niveles[i]

        # Mostrar el número de nivel actual
        print(Fore.CYAN + f"\n--- Nivel {i + 1} ---")

        # Jugar el nivel actual y actualizar la puntuación del jugador
        puntuacion, abandono = JugarNivel(preguntas, puntuacion)

        if abandono:
            limpiar_consola()
            print(
                Fore.YELLOW + f"Juego terminado. Tu puntuación final es: {puntuacion}"
            )
            guardar_ranking(nombre, puntuacion)
            return

        if i < len(niveles) - 1:  # Si no es el último nivel
            continuar = input(
                Fore.CYAN + "¿Quieres jugar el siguiente nivel? (s/n): "
            ).lower()
            if continuar != "s":
                limpiar_consola()
                print(
                    Fore.YELLOW
                    + f"Juego terminado. Tu puntuación final es: {puntuacion}"
                )
                guardar_ranking(nombre, puntuacion)
                return

    limpiar_consola()
    # Mostrar la puntuación final al completar todos los niveles
    print(
        Fore.GREEN
        + f"¡Felicitaciones! Has completado todos los niveles. Tu puntuación final es: {puntuacion}"
    )
    guardar_ranking(nombre, puntuacion)


def iniciar_juego():
    usuario = "martin"
    contraseña = "123456"
    intentos = 1
    while intentos <= 3:
       
        usuarioIngresado = input(Fore.CYAN + "Ingrese su usuario: ")
        contraseñaIngresada = input(Fore.CYAN + "Ingrese su contraseña: ")
        if usuario == usuarioIngresado and contraseña == contraseñaIngresada:
            limpiar_consola()
            print(Fore.GREEN + "Felicidades, ingresaste correctamente.")
            descripcion_del_juego()
            jugar = input(Fore.CYAN + "¿Quieres jugar? (s/n): ").lower()
            if jugar == "s":
                limpiar_consola()
                JuegoPreguntas()
            else:
                limpiar_consola()
                print(Fore.YELLOW + "¡Hasta la próxima!")
            break  # Asegúrate de romper el ciclo después de ingresar correctamente
        else:
            print(Fore.RED + f"Usuario o contraseña incorrectos, llevas {intentos}/3 intentos")
            intentos += 1

    if intentos > 3:
        limpiar_consola()
        print(Fore.RED + "¡Alcanzaste el máximo de intentos!")

        # Iniciar el juego


iniciar_juego()
