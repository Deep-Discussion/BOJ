import sys
#2+1 세일
#최소비용으로 유제품 구매하기
#가장 싼건 무료, 나머지 두개의 제품 가격만 지불하면됨
#최소비용으로 친구들과 같이 먹을 n팩의 유제품을 구매

#변수
amount = 0;
dairy=[];
n = int(sys.stdin.readline().rstrip());

#유제품 개수 입력 받기
dairy = list(map(int,(sys.stdin.read().splitlines())));

#dairy 정렬하기
dairy.sort(reverse=True);

#3팩씩 나누고 0번째 1번째만 추가하기
count = 0 ;
for i in range(len(dairy)) :
    if( count ==2 ) :
        count = 0;
    else :
        amount += dairy[i];
        count += 1;

print(amount);