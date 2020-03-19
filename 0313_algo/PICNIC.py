import numpy as np

def delete_row(matrix, n = 1):
    if matrix.shape[0] == 2:
        return n
    first_row = np.nonzero(matrix[0])[0]
    n = len(first_row) * n
    matrix = np.delete(matrix, 0, 1)
    matrix = np.delete(matrix, 0, 0)
    matrix = np.delete(matrix, first_row[0]-1, 0)
    matrix = np.delete(matrix, first_row[0]-1, 1)
    return delete_row(matrix, n)

t = int(input())
for i in range(0, t):
    n, m = [int(s) for s in input().split()]
    map_array = np.zeros((n, n))
    map_list = [int(s) for s in input().split()]
    for j in range(0, len(map_list),2):
        map_array[map_list[j]][map_list[j+1]] = 1
    map_array = np.maximum(map_array, map_array.T)
    print(delete_row(map_array))
