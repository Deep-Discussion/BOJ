#16198 : 에너지 모으기
#풀이 : 재귀사용 

#1. 에너지 구슬 하나를 고르고 고른 에너지 구슬의 번호 x 첫번째와 마지막은 고를수 x
#2. x번째 에너지 구슬을 제거
#3. 에너지 w(n-1) * w(n+1)
#4. n을 1 감소시키고 에너지 구슬을 1~n까지 다시 번호를 매긴다. 

#1.) 값 입력받기
n = int(input());
energyBall = list(map(int,(input().split())));

max = 0;
#2.) 첫번째, 마지막 구슬 돌리기
def maxBall(balls, sum) :
    global max;

    if len(balls) <=2 :
        if max < sum :
            max = sum;
        return ;

    for i in range (1, len(balls)-1) :  #중간에 for문으로 돌리는걸 잊었다. 함수 내에서 하면 됨
        weight = balls[i-1] * balls[i+1];
        val = balls.pop(i);
        maxBall(balls, i, sum + weight);
        balls.insert(i,val);     #훼손된 배열 원상복구 해주기 
        #값 증가시켜주기

maxBall(energyBall,1,0);
print(max);
#3.) 에너지 구슬 하나를 고르고 n<3 return 해주기
