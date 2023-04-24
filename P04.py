a, b, c, d = map(int, input().split())
if a/b == c/d or a/c == d/c:
    print("Possible")
elif a/c == b/d or a/c == d/b:
    print("Possible")
elif a/d == b/c or a/d == c/b:
    print("Possible")
else:
    print("Impossible")
