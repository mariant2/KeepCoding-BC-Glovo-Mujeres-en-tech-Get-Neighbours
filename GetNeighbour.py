from functools import reduce
from tkinter import X


def process_matrix(matrix):
    """recebe uma lista de numeros e dvolve uma nova
    com os elementos mudados. Cada elemento sera a media do valor
    antigo e de seus vizinhos"""
    #crio uma lista vazia onde ira acumulando
    new_matrix = []

    for i, fila in enumerate(matrix):
        matrix_avg=[]
        new_matrix.append(matrix_avg)

        for j, valor in enumerate(fila):
            new=process_element(i,j,matrix)
            matrix_avg.append(new)

    return new_matrix

def process_element(i, j, matrix):
    """Recebe el indice de un elemento y la lista
    en la que esta, calcula sua media com seus
    vizinhos e devolve a media"""
    neighbor_value = get_neighbour_values(i,j,matrix)
    average = get_average(neighbor_value)
    return average

def get_neighbour_values(i, j, matrix):
    values = []

    height = len(matrix)
    if height <= 0:
        return values

    width = len(matrix[0])
    if width <= 0:
        return values

    values.append(matrix[i][j])

    if i > 0:
        values.append(matrix[i-1][j])

    if i < height-1:
        values.append(matrix[i+1][j])

    if j > 0:
        values.append(matrix[i][j-1])

    if j < width-1:
        values.append(matrix[i][j+1])

    return values


def get_average(numbers):
    """recebe uma lista e devolve promedio"""
    #reduce hace la soma y divide
    return round(reduce(lambda a, b: a + b, numbers, 0 ) / len(numbers),1)



if __name__ == "__main__":
    matrix = [[1, 4, 1, 1, 1, 7],
              [1, 2, 3, 4, 5, 6],         
              [3, 6, 0, 0, 1, 1],
              [7, 6, 3, 4, 0, 1],
              [0, 0, 1, 1, 7, 2],
              [0, 1, 0, 1, 1, 3]]

print("New Matrix:")
processed_matrix = process_matrix(matrix)
for i, fila in enumerate(processed_matrix):
    print(fila)





