#홀수일경우
#짝수일 경우
# dp(5)일경우 2(n-1) + 2(n-3)*(n-2) + (n-1)

#입력 : 정수 한개
    #입력이 홀수일때와 입력이 짝수일때가 다름
    #홀수라면 f(n) = 2*(n-1) + 2(n-2)*(n-3) +... + 1

    #짝수라면 f(n) = 2*(n-1) + 2(n-2)(n-3) + ... +2*(1)*(2)
#출력 : 정수 한개

#반복횟수는 len(n/3) but n 이 홀수일때와 짝수일때를 다르게 해야함
#dp배열을 만들어서 각 이전값들을 저장해야함
n = int(input());


dpList = [0] * (36) ;

dpList[0] = 1;
dpList[1] = 1;
dpList[2] = 2;


for  i in range(3 , n+1 ):
    for j in range(0 , i):
        dpList[i] += dpList[j]*dpList[i-1-j];
            

print(dpList[n]);
#?ㅇ?