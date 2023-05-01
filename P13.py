for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a < b and b < c:
        print(0)
    elif b^a < c^a:
        print(a)
    elif b^c < a^b and b^c < a^c:
        print(a^b^c)
    else:
        print(-1)
