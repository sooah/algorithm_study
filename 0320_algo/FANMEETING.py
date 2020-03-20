def fanmeeting(members, fans):
    re_mems = int(members.replace("F", "0").replace("M", "1"),2)
    re_fans = int(fans.replace("F", "0").replace("M", "1"),2)

    hug = 0
    for i in range(len(fans) - len(members) + 1):
        if int(re_fans & re_mems) == 0:
            hug = hug+1
        re_mems = re_mems << 1

    return hug

t = int(input())
for i in range(t):
    members = input()
    fans = input()
    print(fanmeeting(members, fans))