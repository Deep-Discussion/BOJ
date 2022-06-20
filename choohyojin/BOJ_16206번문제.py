# 입력 값 받기
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 이미 확인한 케이크 확인용
visited = [False for i in range(len(arr))]

# 길이가 10인 케이크 수, 자른 횟수
eatable = cut = 0

# 10의 배수인 케이크 먼저 확인
for i in range(len(arr)):
    # 10의 배수일 때
    if arr[i] % 10 == 0:
        visited[i] = True
        tmp = arr[i] // 10
        # 자를 수 있는 횟수 이하라면
        if cut + tmp - 1 <= m: 
            eatable += tmp
            cut += tmp - 1
        # 자를 수 있는 횟수를 넘겼을 때
        else:
            eatable += m - cut
            cut = m

# 10의 배수가 아닌 케이크 확인
if cut < m:
    for i in range(len(arr)):
        tmp = arr[i] // 10
        if not visited[i] and tmp > 0:
            # 자를 수 있는 횟수 미만이라면
            if cut + tmp < m: 
                eatable += tmp
                cut += tmp
            # 자를 수 있는 횟수를 넘겼을 때
            else:
                eatable += m - cut
                break
    
print(eatable)

# 통과하지 못한 코드입니다.