from array import array as arr

rows = 10
columns = 2 * rows - 1

matrix = []

# Construyendo la cuadricula
for _ in range(rows):
    nueva_fila = arr('i', [0] * columns)
    matrix.append(nueva_fila)

# Calculando el centro de la primera fila
center = columns // 2
matrix[0][center] = 1

# Se calcula el resto de la matriz siguiendo el patrón de Sierpinski
for fila in range(1, rows):
    for columna in range(columns):
        izquierdo = 0
        derecho = 0

        if columna > 0:
            izquierdo = matrix[fila - 1][columna - 1]

        if columna < columns - 1:
            derecho = matrix[fila - 1][columna + 1]

        if izquierdo != derecho:
            matrix[fila][columna] = 1
        else:
            matrix[fila][columna] = 0

def draw_matrix(
    matrix,
    symbol="▪",
    foreground="\033[97m",
    background="\033[44m",
):
    for row in matrix:
        cells = "".join(
            f"{foreground}{symbol}" if value == 1 else " "
            for value in row
        )
        print(f"{background}{cells}\033[0m")


draw_matrix(matrix)
