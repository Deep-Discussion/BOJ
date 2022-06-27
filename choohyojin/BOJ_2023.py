def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

#####################################
# dp
# 이미 소수인 것에 더 붙였을 때 소수라면 keep
n = int(input())
startNum = 10 ** (n - 1)
endNum = 10 ** n
weirdos = ['2', '3', '5', '7']

for i in range(n - 1):
    tmp = []
    for j in range(len(weirdos)):
        for k in range(10):
            toCheck = weirdos[j] + str(k)
            if isPrime(int(toCheck)):
                tmp.append(toCheck)
    weirdos = list(tmp)

for i in range(len(weirdos)):
    print(weirdos[i])


