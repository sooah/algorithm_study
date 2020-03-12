import numpy as np

t = int(input())
board = np.zeros((5, 5), dtype='U')
for i in range(1, 6):
    row = input().split()
    board[i-1,:] = [row[0][j] for j in range(0, len(row[0]))]
print(board)

def hasWord(word):
    y = 1
    x = 1
    dx_range = [-1, 0, 1]
    dy_range = [-1, 0, 1]

    # base case 1. location of start is not in range
    if (x > board.shape[0] and y > board.shape[1]):
        # return 'case1'
        return False
    # base case 2. location of start is not equal to word first letter
    if board[x][y] != word[0][0]:
        # return 'case2'
        return False
    # base case 3. word size is 1
    if len(word) == 1:
        return True

    # word first letter equal, word size != 1
    for dx in dx_range:
        for dy in dy_range:
            x_loc, y_loc = x - dx, y - dy
            if hasWord(x_loc, y_loc, word.pop(0)):
                return True

t = int(input())
for i in range(1, t+1):
    word = input().split()
    # print(word[0][0])
    result = hasWord(word)
    print(word[0], result)
