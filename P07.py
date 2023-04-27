for i in range(int(input())):
    x = int(input())
    if x == 1:
        print(-1)
    elif x <= 10**6+1:
        print(1, x-1, 1)
    else:
        if x%10**6 != 0:
            print(x//10**6, 10**6, x%10**6)
        else:
            print(x//10**6-1, 10**6, 10**6)
