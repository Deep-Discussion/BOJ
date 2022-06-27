n = int(input())

start = []
target = [int(input()) for _ in range(n)]
idx = 0
t = target[idx]
prev = float('inf')
ans = []

# 1~n 까지 입력 받는데 타겟에 가장 첫째로 들어가는 값이 나올 때 까지 push
# 타겟의 그 다음 값이 이전 값보다 작으면 이전의 스텍의 꼭데기 값이랑 비교
# 만약 꼭데기 값이랑 다르면 -> NO , 같으면 Pop
for i in range(1, n + 1):
    if i == t:
        ans.append('+')
        ans.append('-')
        if idx < n-1:
            idx += 1
        prev, t = t, target[idx]

        while prev > t and prev != float('inf'):
            if not start:
                print('NO')
                exit(0)
            else:
                if start[-1] == t:
                    prev = start.pop()
                    if idx < n-1:
                        idx += 1
                        t = target[idx]
                    ans.append('-')
                else:
                    print('NO')
                    exit(0)
    else:
        start.append(i)
        ans.append('+')

for i in range(len(start)):
    if start[i] == target[n-1-i]:
        ans.append('-')
    else:
        print("NO")
        exit(0)

for a in ans:
    print(a)