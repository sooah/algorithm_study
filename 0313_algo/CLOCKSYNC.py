import numpy as np

t = int(input())

matrix = np.zeros((4,4))
clock_con = np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                     [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]])

def checkAlign(matrix):
    if np.sum(matrix%12)== 0:
        return True

def clockAlign(clock_con, matrix, min_num=41, num=0):
    if checkAlign(matrix):
        return min_num

    for s in range(10):
        connect_clocks = np.nonzero(clock_con[s])[0]
        for idx, clock in enumerate(connect_clocks):
            clock_con[idx//4][idx%4] += 3
            clock_con = clock_con%12

            num += 1


for i in range(1, t+1):
    times = [int(s) for s in input().split()]
    for idx, t in enumerate(times):
        matrix[idx//4][idx%4] = t



    print(matrix%13)
