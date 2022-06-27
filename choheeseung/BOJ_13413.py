t = int(input())

for i in range(t):
    n = int(input())
    textCount = 0
    goalCount = 0

    text = str(input().rstrip())  # 초기 상태
    goal = str(input().rstrip())  # 목표 상태

    for j in range(n):
        if text[j] == 'W' and goal[j] == 'B':
            textCount += 1
        elif text[j] == 'B' and goal[j] == 'W':
            goalCount += 1

    print(max(textCount, goalCount))
