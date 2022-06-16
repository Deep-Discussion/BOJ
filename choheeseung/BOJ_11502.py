# 에라토스테네스의 체
def get_primes(n):
    a = [False, False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes


def find_primes(target, primes):
    for i in primes:
        total = 0
        for j in primes:
            for k in primes:
                total = i + j + k
                if total == target:
                    print(i, j, k)
                    return


t = int(input())
primes = get_primes(1000)

for _ in range(t):
    target = int(input())
    filteredPrimes = list(filter(lambda x: x < target, primes))
    find_primes(target, filteredPrimes)
