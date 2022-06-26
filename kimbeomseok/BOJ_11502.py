import math
from typing import List


def is_prime_num(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True


def find_three_decimal(decimals: List[int], number: int):
    result = []
    for a in decimals:
        for b in decimals:
            for c in decimals:
                if a + b + c == number:
                    result.extend([a, b, c])
                    return result
    return result


def three_decimal(number: int) -> None:

    decimals = []
    for x in range(2, 1000):
        if is_prime_num(x):
            decimals.append(x)

    result = find_three_decimal(decimals, number)

    if result:
        print(*result)
        return
    print(0)
