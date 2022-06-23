from itertools import combinations
from functools import reduce

def ynUnion(str1, str2):
    res = ""
    for i in range(len(str1)):
        if str1[i] == "Y" or str2[i] == "Y":
            res += "Y"
        else:
            res += "N"
    return res    

def countYes(str1):
    cnt = 0
    for i in str1:
        if i == "Y":
            cnt += 1
    return cnt

#############################
# 비트연산처럼 접근해보기

n, m = map(int, input().split())
inputArr = []

for i in range(n):
    # 기타 이름은 쓰이지 않는다
    inputArr.append(input().split()[1])

# 초기 문자열 설정
tmp = "N" * m
# 최대 연주 가능 곡 갯수 파악하기
for i in range(len(inputArr)):
    tmp = ynUnion(inputArr[i], tmp)
playable = countYes(tmp)

if playable == 0:
    print("-1")
    exit()

# 루프를 순회하며 1개, 2개, 3개, 4개 선택해나가며 늘려감
# 최대 연주 가능 곡 갯수에 도달하면 break
for i in range(n):
    tmp = str(inputArr[0])
    candidates = list(combinations(inputArr, i + 1))
    
    for j in range(len(candidates)):
        tmp = "N" * m
        # 리스트 안의 각 요소끼리 더함
        tmp = reduce(ynUnion, candidates[j], tmp)
        if countYes(tmp) == playable:
            print(i + 1)
            exit()
    