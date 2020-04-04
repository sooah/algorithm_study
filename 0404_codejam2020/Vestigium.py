t = int(input())
for i in range(1, t + 1):
    N = int(input())
    t = 0
    ch_r = 0
    ch_c = 0
    arr = []
    for n in range(N):
        row = list(map(int, input().split(" ")))
        arr.append(row)
        t += row[n]
        if len(list(set(row))) != len(row):
            ch_r += 1

    for r in range(N):
        column = []
        for c in range(N):
            column.append(arr[c][r])
        if len(list(set(column))) != len(column):
            ch_c += 1
    print("Case #{}: {} {} {}".format(i, t, ch_r, ch_c))

