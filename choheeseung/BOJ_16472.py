n = int(input())
string = str(input().strip())
result = [0, 0]

# 투 포인터
start = 0
end = 0

# 딕셔너리
dic = {}

# 예제 입력 : 2 abbcaccba
# {'a': 1}
# {'a': 1, 'b': 1}
# {'a': 1, 'b': 2}
# {'b': 2, 'c': 1}
# {'c': 1, 'a': 1}
# {'c': 2, 'a': 1}
# {'c': 3, 'a': 1}
# {'c': 2, 'b': 1}

while start < len(string) and end < len(string):
    if string[end] not in dic:
        dic[string[end]] = 1
    else:
        dic[string[end]] += 1

    if len(dic) > n:
        while start <= end and len(dic) > n:
            if dic[string[start]] == 1:
                dic.pop(string[start])
            else:
                dic[string[start]] -= 1
            start += 1

    else:
        if result[1] - result[0] < end - start:
            result[0] = start
            result[1] = end

    end += 1

print(result[1] - result[0] + 1)
