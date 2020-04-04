def parenting(time_lists):
    J_list = []
    C_list = []
    order = [0 for _ in range(len(time_lists))]

    for idx, time in enumerate(time_lists):
        act = time[0]
        times = time[1]

        if idx == 0:
            J_list = times
            order[act] = 'J'
            continue

        new_act_start = min(times)
        new_act_end = max(times)

        J_min = min(J_list)
        J_max = max(J_list)
        

        if new_act_end <= J_min:
            J_list = J_list + times
            # J_list.sort()
            order[act] = 'J'
            continue

        elif J_max <= new_act_start:
            J_list = J_list + times
            # J_list.sort()
            order[act] = 'J'
            continue

        elif not C_list:
            C_list = times
            order[act] = 'C'
            C_min = min(C_list)
            C_max = max(C_list)
            continue

        elif new_act_end <= C_min:
            C_list = C_list + times
            order[act] = 'C'
            C_min = min(C_list)
            C_max = max(C_list)
            continue

        elif C_max <= new_act_start:
            C_list = C_list + times
            order[act] = 'C'
            C_min = min(C_list)
            C_max = max(C_list)
            continue

        else:
            order = ['IMPOSSIBLE']
            break
            
    order_string = ''.join(order)

    return order_string

cases = int(input())
for i in range(1, cases+1):
    acts = int(input())
    time_dict = {}
    for a in range(acts):
        times = list(map(int, input().split(" ")))
        time_dict[a] = times
    time_dict = sorted(time_dict.items(), key=(lambda x: x[1][0]))
    print('Case #{}: {}'.format(i, parenting(time_dict)))
