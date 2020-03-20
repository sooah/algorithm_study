def fence(heights, fence_num):
    heights.append(0)
    stack = []
    width = 0
    result = 0
    for idx in range(fence_num+1):
        while stack and heights[stack[-1]] >= heights[idx]:
            right = stack[-1]
            del stack[-1]
            if not stack:
                width = idx
            else:
                width = idx - stack[-1]-1
            area = width * heights[right]
            result = max(result, area)
        stack.append(idx)
    return result

t = int(input())
for i in range(t):
    fence_num = int(input())
    heights = list(map(int, input().split(' ')))
    print(fence(heights, fence_num))