# Dimensiones del laberinto (5x5)
filas = 5
columnas = 5

# Lista de listas del laberinto con espacios ' '
laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Definir coordenadas de las casillas con muro
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Colocar 'X' en las casillas con muro
for i, j in muro:
    laberinto[i][j] = 'X'

# Colocar inicio (S) y final (E) en laberinto directamente
laberinto[0][0] = 'E'
laberinto[4][4] = 'S'

#Función menú del juego:
def menú():
    print("Bienvenido:")
    print("-Introduzca 1 para visualizar el laberinto")
    print("-Introduzca 2 si quiere salir del programa")

#Función llamada desde el launcher para iniciar el juego:
def jugar():
    while True:
        menú()
        opcion = int(input("Tu elección: "))

        if opcion == 1:
            for fila in laberinto:
                print(' '.join(fila))
        elif opcion ==2:
            break