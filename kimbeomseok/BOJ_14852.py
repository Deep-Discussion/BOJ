n = int(input())
a, b, c = 1, 2, 7
if n == 1:
    print(b)
elif n == 2:
    print(c)
else:
    for _ in range(n - 2):
        a, b, c = b, c, (c * 3 + b - a) % 1000000007
    print(c)
