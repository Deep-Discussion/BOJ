#최고 길이 세고, 최고 길이 배열을 저장하기
#1. 이전거가 collect에 in 되는지 검사하기
#2. 속했을때 => if문으로 하나하나 돌면서 길이 증가
#3. 안속했을때 => 속했을 만큼의 배열과 배열의 길이를 저장해놓는다.
import sys

n = int(sys.stdin.readline().rstrip());                  #2
str = sys.stdin.read().rstrip();                  #abbcaccba

maxCount=0;
start = 0;
end = 0;
i = 0;

#dict 로 바꾸기
#들어오는 string의 길이가 길어질 시 set함수가 시간을 
dict={}
#for => i로
while (i < len(str) and end < len(str)):

#문자열을 집어넣기 전에 dict에 전처리한다. 일단 넣는건 무조건 넣어줘야 되니까
    if str[end] not in dict:
        dict[str[end]] = 1;
    else :
        dict[str[end]] += 1;
    
    #딕셔너리 안의 문자가 n 보다 크면
    if len(dict) > n :
        while (start <= end and len(dict) > n):
            if dict[str[start]] == 1:   #start값이 하나 남았다면 그냥 맨앞껄 뺴주면 된다. #abbc
                dict.pop(str[start]); #해당값을 pop해줌
            else :                      #aabac이렇게 되어 있다면
                dict[str[start]] -=1 ;     #값을 하나씩 빼주면서 끝까지 빼낼 수 있도록 찾아낸다.
            start+=1;

    #만약 연속된 n개의 문자열이 들어왔을 경우
    #result안에 최대 길이가 될 수 있도록 넣어주자.
    if( len(dict) <= n ):
        
        maxCount = max(maxCount , end - start );
    end += 1;

print(maxCount+1);
       