#11502 세개의 소수 문제
#부르트포스 , 에라토스테네스의 체

import sys



#에토체
def isPrime(num) :
    if (num < 2) : return;
    i = 2 ;
    while(i * i <= num) :
        if (num % i == 0) :
            i += 1;
            return ;
        i+=1;
    return num;

numList = [];
primes =[];
maxNum = 0;
answer = []

T =  int(sys.stdin.readline().rstrip());

#입력받기
for i in range(T):
    numList.append( int(sys.stdin.readline().rstrip()) );

maxNum = max(numList);

#소수구하기
for i in range(maxNum):
    a = isPrime(i);
    if a != None : primes.append(a);

for idx in range (len(numList)):
    myList = [0]
    for i in primes :
        if(myList[0] != 0):
            break;
        for j in primes :
            if(myList[0] != 0):
                break;
            for k in primes :
                sum = i + j + k ;
                if( sum == numList[idx]) :
                    myList = [i,j,k];
                    answer.append(myList);
                    break;


for ans in answer:
    print(*ans)
