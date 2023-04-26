for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split())) 
    lst.sort()
    s = lst[0]
    m = lst[0]
    
    for i in range(1, n):
        s += lst[i] - lst[0]

    if n%2 == 1 and s%2 == 0 or n%2 == 0 and s%2 == 0 and m%2 == 0:
        print("Chefina")
    else:
        print("Chef")
