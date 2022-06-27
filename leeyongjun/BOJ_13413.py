n = int(input())


def count_change(_in, _out, num):
    n1, n2, cnt = 0, 0, 0
    for i in range(num):
        if _in[i] == 'W':
            n1 += 1
        if _out[i] == 'W':
            n2 += 1
        if _in[i] != _out[i]:
            cnt += 1

    val = abs(n1 - n2)
    return (cnt - val)//2 + val


for _ in range(n):
    num = int(input())
    _in = list(input())
    _out = list(input())
    print(count_change(_in, _out, num))