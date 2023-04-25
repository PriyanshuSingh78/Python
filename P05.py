for i in range(int(input())):
    S = input()
    flag = 0
    for i in S:
        if i == '1' and flag == 0:
            flag = 1
        elif flag == 1 and i == '0':
            flag = 2
        elif flag == 2 and i == '1':
            flag = 3
            break
    if flag == 0 or flag == 3:
        print("NO")
    else:
        print("YES")
