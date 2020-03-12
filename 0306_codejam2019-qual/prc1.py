t = int(input())
for i in range(1, t + 1):
    N = input()
    strN = str(N)
    A = ''
    B = ''
    for n, string in enumerate(strN):
        if string=="4":
            first = '1'
            second = '3'
            A = A + first
            B = B + second
        else:
            A = A + string
            B = B + '0'
    print("Case #{}: {} {}".format(i, int(A), int(B)))