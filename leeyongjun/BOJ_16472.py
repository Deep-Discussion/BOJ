# (*ΦωΦ*) 고냥이문제
import collections

n = int(input())
str = list(input())

mid = len(str) // 2
max_length = 0
dic = collections.defaultdict(int)
dic[str[0]] = 1

#two pointer
p1, p2 = 0, 0
st, end = 0, len(str) - 1

while p1 != end:
    # dictionay 를 사용하지 않고 길이가 길어질때마다 set을 이용한 길이 계산을 하였더니 시간초과가 발생
    # dictionary 값을 이용하여 값이 0 이 되면 pop 시켜서 총 길이를 계산하였다.
    # 투포인터를 이용하여 길이가 입력 n보다 커지면 p1 값 증가 , n보다 작거나 같으면 p2값 증가
    if len(dic) <= n:
        max_length = max(max_length, p2-p1+1)
        if p2 == end:
            break
        p2 += 1
        dic[str[p2]] += 1
    else:
        if dic[str[p1]] == 1:
            dic.pop(str[p1])
        else:
            dic[str[p1]] -= 1
        p1 += 1

print(max_length)