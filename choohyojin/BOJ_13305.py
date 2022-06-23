n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 마지막 지점을 강제로 포함시키기 위한 원소 추가, 수정
distances.append(0)
prices[-1] = 1000000000

checked = [False for i in range(n)]
distance = price = 0

for i in range(n - 1):
    # 현재 도시에서 주유를 할 필요가 있는지 확인
    if checked[i]:
        continue
    else:
        checked[i] = True

    # 다음 지점들이 현재 지점보다 가격이 높은지 확인        
    distance = distances[i]
    for j in range(i + 1, n):
        if prices[i] < prices[j]:
            distance += distances[j]
            checked[j] = True
        else:
            break
    
    price += distance * prices[i]

print(price)