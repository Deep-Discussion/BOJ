n, m = map(int, input().split())
cake = list(map(int, input().split()))
cake = sorted(cake)
cake = sorted(cake, key=lambda x: x % 10)

count = 0

for cut in cake:
    if m > 0:
        if cut < 10:
            continue
        elif cut % 10 == 0:
            temp = (cut // 10) - 1  # 자르는 횟수
            if temp == 0:
                count += 1
            else:
                if (m >= temp):  # 자른 횟수가 최대 횟수보다 작으면
                    count += temp + 1
                    m -= temp
                else:
                    count += m
                    break
        else:
            temp = (cut // 10)
            if (m >= temp):  # 자른 횟수가 최대 횟수보다 작으면
                count += temp
                m -= temp
            else:
                count += m
                break
    else:
        break

print(count)
