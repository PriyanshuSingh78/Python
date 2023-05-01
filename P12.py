for i in range(int(input())):
    n = int(input())
    count = 0
    while n != 0:
        if n%2 == 1:
            count += 1
        n //= 2
    print(count-1)
