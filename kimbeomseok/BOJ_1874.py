def stack_sequence(input_value_n: str) -> None:
    n = int(input_value_n)

    cnt = 0
    res = []
    stack = []
    isValid = True
    
    for i in range(n):
        cur = int(input())
        while cnt < cur:
            cnt += 1
            res.append("+")
            stack.append(cnt)
        if stack[-1] == cur:
            stack.pop()
            res.append("-")
            continue
        isValid = False
        break
    
    if isValid:
        print("\n".join(res))
        return
    print("NO")
stack_sequence(input())