import numpy as np

def cover(matrix, method_num = 0):
    if np.sum(matrix)%3 != 0 and method_num == 0:
        print('case1')
        return method_num

    if np.sum(matrix) == 0:
        print('case2')
        return method_num

    for h in range(matrix.shape[0]):
        row = np.nonzero(matrix[h])[0]
        if len(row) != 0:
            break
    first = row[0]

    if matrix[h][first+1] == 1 and matrix[h+1][first+1] == 1:
        matrix[h][first+1] = 0
        matrix[h+1][first+1] = 0
        matrix[h][first] = 0
        method_num += 1

    elif matrix[h+1][first] == 1 and matrix[h+1][first+1] == 1:
        matrix[h+1][first] = 0
        matrix[h+1][first+1] = 0
        matrix[h][first] = 0
        method_num += 1

    elif matrix[h][first+1] == 1 and matrix[h+1][first] == 1:
        matrix[h][first+1] = 0
        matrix[h+1][first] = 0
        matrix[h][first] = 0
        method_num += 1

    elif matrix[h+1][first] == 1 and matrix[h+1][first-1] == 1:
        matrix[h+1][first] = 0
        matrix[h+1][first-1] = 0
        matrix[h][first] = 0
        method_num += 1

    return cover(matrix)

t = int(input())
for i in range(1, t+1):
    H, W = [int(s) for s in input().split()]
    matrix = np.ones(H, W)
    for h in range(H):
        row = input().split()
        row = [row[0][w] for w in range(0, len(row[0]))]
        for column, w in enumerate(row):
            if w == "#":
                matrix[h][column] = 0
            else:
                matrix[h][column] = 1
    print(cover(matrix))



