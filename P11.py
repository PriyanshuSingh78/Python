for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    r = sum(lst)//(n+1)
    for i in lst:
        print(i-r, end=" ")
    print()
