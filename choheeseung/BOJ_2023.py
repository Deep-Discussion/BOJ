# 소수를 판별하는 함수
def prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


# n자리수
n = int(input())
prime = [2, 3, 5, 7]

# for i in range(pow(10, n-1), pow(10, n) - 1):
#     if prime_number(i):
#         third = str(i)[:-1]
#         if prime_number(int(third)):
#             second = str(third)[:-1]
#             if prime_number(int(second)):
#                 first = str(second)[:-1]
#                 if prime_number(int(first)):
#                     print(i)

# 가지치기
# 2 -> 23 -> 233 -> 2333
# 2 -> 23 -> 233 -> 2339 이런식으로


def find(num, n):
    if len(str(num)) == n:
        print(num)
        return

    # 둘째자리부터는 홀수만
    for i in range(1, 10, 2):
        if prime_number(num * 10 + i):
            find(num * 10 + i, n)


# 첫번째 자리수가 2, 3, 5, 7 인 것만
for i in prime:
    find(i, n)
