def printCombination(n):
    # 에라토스테네스의 체
    allNum = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if allNum[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                allNum[j] = False

    for i in primes:
        for j in primes:
            for k in primes:
                if i + j + k == n:
                    print(i, j, k)
                    return
    
    print("0")
    return


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    printCombination(arr[i])