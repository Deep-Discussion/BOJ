#t = int(input())
t = [i for i in range(7, 999, 2)]

prime = [True] * 1001
m = int(1000**0.5)

#에라토스테네스의 체
for i in range(2, m+1):
    if prime[i]:
        for j in range(i+i, 1001, i):
            prime[j] = False

#소수인 값들만 선별
primeList = [i for i in range(2, 1001) if prime[i]]

answer = []


def print_number(t):
    for i in primeList:
        for j in primeList:
            for z in primeList:
                if i + j + z == t:
                    print(i, j, z, i+j+z)
                    return
    print(0)


for i in t:
    print_number(i)