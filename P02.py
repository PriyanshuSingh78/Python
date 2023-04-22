t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    num_of_runs = 0
    for i in range(0, n):
        num_of_runs += arr[i]
        if num_of_runs*100/(i+1) == 100:
            count += 1
    print(count)
