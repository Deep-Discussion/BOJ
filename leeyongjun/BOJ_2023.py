# 에라토스테네스의 채 메모리 초과
# n = int(input())
#
# m = int(pow(10, n))
# a = int(m ** 0.5)
# array = [True for _ in range(m)]
# array[1] = False
#
# for i in range(2, a + 1):
#     if array[i]:
#         for j in range(i + i, m, i):
#             array[j] = False
#
# _arr = [i for i in range(2, m) if array[i] and i > m/10]
#
#
# def check_specific_num(val):
#     if val < 10:
#         if array[val]:
#             return True
#         else:
#             return False
#
#     if array[val]:
#         return check_specific_num(val//10)
#
#
# for i in _arr:
#     if check_specific_num(i//10):
#         print(i)
#



# 소수 판별 함수
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solve(n):
    ans = []
    stack = [2, 3, 5, 7]

    while stack:
        data = stack.pop()
        if pow(10, n-1) <= data < pow(10, n):
            ans.append(data)
            continue

        for i in range(10):
            _data = data*10 + i
            if is_prime(_data):
                stack.append(_data)

    return sorted(ans)

n = int(input())
answer = solve(n)
for ans in answer:
    print(ans)

