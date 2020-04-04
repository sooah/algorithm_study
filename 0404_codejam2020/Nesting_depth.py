def nesting(numbers):
    nest = ''
    for n, number in enumerate(numbers):
        if n == 0:
            nest = nest + '('*number
            nest = nest + str(number)
        else:
            nest = nest + str(number)

        if (n+1) == len(numbers):
            gap = number
        else:
            gap = number - numbers[n+1]

        if gap > 0:
            nest = nest + ')'*gap

        elif gap < 0:
            # nest.append('('*abs(gap))
            nest = nest + '('*abs(gap)
            # nest.append(number)

        # if (n+1) == len(numbers) and number != 0:
        #     nest.append(')'*number)

    return nest


cases = int(input())
for i in range(1,cases+1):
    nums = list(input())
    nums = list(map(int, nums))
    print('Case #{}: {}'.format(i, nesting(nums)))
