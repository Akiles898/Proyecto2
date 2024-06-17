import random

def mostrar_tablero(tablero):
    # Función para mostrar el tablero actual
    print("\n  Tablero")
    print("  1 | 2 | 3 ")
    print(" -----------")
    print(f"1 {tablero[(0, 0)]} | {tablero[(0, 1)]} | {tablero[(0, 2)]} ")
    print(" -----------")
    print(f"2 {tablero[(1, 0)]} | {tablero[(1, 1)]} | {tablero[(1, 2)]} ")
    print(" -----------")
    print(f"3 {tablero[(2, 0)]} | {tablero[(2, 1)]} | {tablero[(2, 2)]} \n")

def verificar_ganador(tablero, jugador):
    # Función para verificar si hay un ganador
    lineas_ganadoras = [
        [(0, 0), (0, 1), (0, 2)], # Fila 1
        [(1, 0), (1, 1), (1, 2)], # Fila 2
        [(2, 0), (2, 1), (2, 2)], # Fila 3
        [(0, 0), (1, 0), (2, 0)], # Columna 1
        [(0, 1), (1, 1), (2, 1)], # Columna 2
        [(0, 2), (1, 2), (2, 2)], # Columna 3
        [(0, 0), (1, 1), (2, 2)], # Diagonal \
        [(0, 2), (1, 1), (2, 0)]  # Diagonal /
    ]

    for linea in lineas_ganadoras:
        simbolos = [tablero[casilla] for casilla in linea]
        if all(simbolo == jugador for simbolo in simbolos):
            return True
    return False

def turno_jugador(tablero, jugador):
    # Función para el turno de un jugador humano
    while True:
        try:
            fila = int(input(f'Jugador {jugador}, ingresa la fila (1-3): ')) - 1
            columna = int(input(f'Jugador {jugador}, ingresa la columna (1-3): ')) - 1
            if (fila, columna) in tablero and tablero[(fila, columna)] == ' ':
                tablero[(fila, columna)] = jugador
                break
            else:
                print("Casilla ocupada o fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

def turno_computadora(tablero, jugador):
    # Función para el turno de la computadora (movimiento aleatorio)
    print(f'Turno de la computadora ({jugador}):')
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[(fila, columna)] == ' ':
            tablero[(fila, columna)] = jugador
            break

def jugar_gato():
    # Función principal para jugar Gato
    tablero = {(i, j): ' ' for i in range(3) for j in range(3)}
    jugadores = ['X', 'O']
    jugador_actual = 0
    jugando = True

    print("¡Bienvenido al juego Gato!")

    while jugando:
        mostrar_tablero(tablero)
        jugador = jugadores[jugador_actual]

        if jugador == 'X':
            turno_jugador(tablero, jugador)
        else:
            turno_computadora(tablero, jugador)

        if verificar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f'¡El jugador {jugador} ha ganado!')
            jugando = False
        elif all(tablero[casilla] != ' ' for casilla in tablero):
            mostrar_tablero(tablero)
            print("¡Es un empate!")
            jugando = False

        jugador_actual = (jugador_actual + 1) % 2

def menu():
    # Función para mostrar el menú y manejar las opciones
    while True:
        print("\nMenu:")
        print("1. Nueva partida (Jugador VS Computadora)")
        print("2. Versus (Jugador 1 VS Jugador 2)")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            jugar_gato()
        elif opcion == '2':
            print("¡Modo Versus seleccionado!")
            jugar_gato()
        elif opcion == '3':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
