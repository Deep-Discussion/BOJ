#오셀로 초기 데이터엔 두가지 상태가 있다.
#1. 색의 개수는 똑같은데 위치만 다를경우
#2. 색의 개수도 다를경우
#이때의 최소 개수를 구해야 한다.

import sys

#입력받기
T = int(sys.stdin.readline().rstrip());

k, count = 0, 0;
wCount, bCount = [0,0], [0,0];

while( k < T ) : 
    count = 0;
    temp = [];
    n = int(sys.stdin.readline().rstrip());
    before = list(sys.stdin.readline().rstrip());
    target = list(sys.stdin.readline().rstrip());
    
    #색깔이 같을때의 수 세기
    matchBefore = [];
    matchTarget = [];
    #색깔이 무조건 다름
    for i in range(n) :
        if(before[i] != target[i]):
            matchBefore.append(before[i]);
            matchTarget.append(target[i]);

    matchBefore.sort();
    matchTarget.sort();

    #count를 증가시켜줌 무조건 한번 올려야함
    #색깔은 같은데 자릿수가 다름 : 자릿수는 무조건 짝으로 다를 수밖에 없음. = 다른 자리의 개수 /2 하믄 댐
    for i in range(len(matchBefore)):
        if matchBefore[i]!= matchTarget[i] :
            count += 1 ;
        else :
            count += 0.5 ;


    print(int(count));
    k += 1;







