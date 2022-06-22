import math


def sum_square_number(n: int) -> int:
    d = [0 for _ in range(n + 1)]
    maximum_sqrt = int(math.sqrt(100000))
    square_numbers = [x ** 2 for x in range(1, maximum_sqrt)]

    for i in range(1, n + 1):

        avaliable_square_numbers = []
        for square_number in square_numbers:
            if i < square_number:
                break
            avaliable_square_numbers.append(d[i - square_number])
        d[i] = min(avaliable_square_numbers) + 1
    return d[n]
print(sum_square_number(int(input())))