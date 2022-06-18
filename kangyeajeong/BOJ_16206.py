#BOJ_16206 롤케이크
#재현이 욕심많음 
#그리디 알고리즘
#최대값을 찾아야 하는 문제다

#if 10이 들어올 때, 
#자르지 않고 count 그대로

#elif 10의 배수가 들어올때
#여유있는 count로 10의 배수를 자르면 -> 10으로 자른횟수 + 1
#마지막 count로 10의 배수를 자르면  -> myCake = 10으로 자른횟수 1

#elif 10의 배수가 아닐 때. -> myCake = 자른 횟수


#a문제는 케이크를 자를 수 있는 최대횟수를 찾으라고 하고 있음.
# 10의 배수인 값들만 미리 뽑아서 => 계산후에, 나머지 계산하기


#값을 입력받음

N, chop = list(map(int,input().split()));
cakes = list(map(int,input().split()));

jeahyonCakes = 0;


#최대값을 구하기 위해 데이터 전처리

cakeMul10 = list(filter(lambda x : x%10 == 0 , cakes)) ; #10의 배수만 뽑기 
cakeNot10 = [x for x in cakes if x not in cakeMul10] ; 
cakeMul10.sort();
cakeMul10.extend(cakeNot10);


def chopchop(myCake) :
    global jeahyonCakes,chop;

    for i in range(len(myCake)):
        if(chop <= 0 ): break;
        while (myCake[i] >= 10 and chop >= 0 ):
            if(myCake[i] == 10):            #cake가 10이면
                jeahyonCakes += 1;
                myCake[i] -= 10;
            
            elif(myCake[i] % 10 == 0) :          #cake가 10의 배수면
                if chop == 0 : chop -=1 ; break;
                jeahyonCakes += 1;
                chop -= 1;
                myCake[i] -= 10 ;

            else :                          #cake 10이상의 정수면
                if chop == 0 : chop -=1 ;break;
                myCake[i] = myCake[i] - 10 ;
                jeahyonCakes += 1;
                chop -= 1;

chopchop(cakeMul10);
print(jeahyonCakes);



#testCast 
#3 2
#100 10 1
#을 통과하기 위해선 정렬을 해줘야 한다.


