#ZOAC
#배열 두개 쓰면 될 것같은 문제

# 문자열 순으로 정렬한 배열 1개
# 그 문자열 순대로 자리값을 저장하는 배열 한개

#첫번째 값은 그냥 문자열에서 가장 큰 값
#그 다음부턴 자리값으로 앞에 pop한 자리값과 비교하여
#앞에다가 놓을지 뒤에다가 놓을지
#정렬 문제같음


#0. 입력받기
nums = {};
strNums = [];
myStr = list(input());


#1. 문자열 순으로 sort할 것.
valPos = {};

for i in range(len(myStr)):
    a = myStr[i];
    nums[a] = ord(a);
    valPos[a] = i;

#2. 문자열과 자리값의 위치를 맞출 것

print(nums);
# print(valPos);
result ="";
result2= ["" for i in range(len(myStr))];

# print(result2);
pre="";
next = ""
preStr = ["" for i in range(len(myStr))];
maxStr=["" for i in range(len(myStr))];
strSorted = sorted(myStr);
for i in range(len(myStr)) :  #크기순대로 한번
        v1 = strSorted[i];
        result =result+ v1;
        print(f'strSorted:{strSorted}');
        print(f'valPos:{valPos}');
        print(f' {v1}');

        for j in range(len(myStr)): #두개의 문자의 크기를 비교
            print(f' {v1}');
        
            for k in range(i+1, len(myStr)):
                v = strSorted[k];
                idxx = valPos[v];
                preStr[idxx] = v;
                if preStr > maxStr :
                    maxStr = preStr;
        
                print("maxStr========")
                print("".join(maxStr));            
            # idx = valPos[v1];
            # result2[idx]=v1;

            
    # for i in range(len(myStr)):                          #자리순대로 한번