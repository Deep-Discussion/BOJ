n = int(input())
d = [1 for _ in range(n + 1)]

for k in range(1, n + 1):
    temp = 0
    for i, j in zip(range(k), range(k - 1, -1, -1)):
        temp += d[i] * d[j]
    d[k] = temp
print(d[n])