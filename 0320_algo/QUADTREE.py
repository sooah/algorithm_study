def quadtree(tree, idx):
    first = tree[idx]
    if first == 'w' or first == 'b':
        return first

    # fill left top
    idx = idx+1
    left_top = quadtree(tree, idx)

    # fill right top
    idx = idx + len(left_top)
    right_top = quadtree(tree, idx)

    # fill left bottom
    idx = idx + len(right_top)
    left_bot = quadtree(tree, idx)

    # fill right bottom
    idx = idx + len(left_bot)
    right_bot = quadtree(tree, idx)

    # 왼위/왼아래(1,3) 순서 바꾸고 오위/오아래(2,4) 순서 바꾸면 됨
    return 'x' + left_bot + right_bot + left_top + right_top

t = int(input())
for i in range(t):
    tree = input()
    print(quadtree(tree, 0))


