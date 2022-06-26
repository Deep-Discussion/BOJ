s =input();

#1. 접미사 배열 만들기
arr = [];

for  i in range(len(s)) :
    arr.append((s[0+i:] ));
arr.sort();

for i in range(len(s)) :
    print(arr[i])


#2. 정렬해서 순서 출력