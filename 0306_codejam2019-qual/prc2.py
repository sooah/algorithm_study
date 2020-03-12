t = int(input())
for i in range(1, 2*t+1, 2):
    N = input()
    L = str(input())
    path = ''
    for _, string in enumerate(L):
        if string == 'S':
            next = 'E'
        else:
            next = 'S'
        path = path + next
    print("Case #{}: {}".format(int((i+1)/2), path))





