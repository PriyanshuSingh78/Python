for _ in range(int(input())):
    b, c = map(int, input().split())
    x = c
    while b != c:
        if b > c:
            b -= c
        else:
            c -= b
    print(x//b)
