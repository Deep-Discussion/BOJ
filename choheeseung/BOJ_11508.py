n = int(input())
arr = []
sum = 0

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n):
    if (i % 3 != 2):
        sum += arr[i]

print(sum)
