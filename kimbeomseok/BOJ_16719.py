def zoac(string: str) -> None:
    temp = ['' for _ in range(len(string))]
    arr = []

    for k, v in enumerate(string):
        arr.append((v, k))
    arr.sort(key=lambda x: x[0])
    alphabet, last_idx = arr.pop(0)
    temp[last_idx] = alphabet
    answer = [alphabet]

    while arr:
        captured = []
        for i in range(len(arr)):
            t = temp[:]
            t[arr[i][1]] = arr[i][0]
            captured.append((i, t))

        m = min(captured, key=lambda x: ''.join(x[1]))
        arr.pop(m[0])
        temp = m[1]
        answer.append(''.join(temp))

    for line in answer:
        print(line)


zoac(input())
