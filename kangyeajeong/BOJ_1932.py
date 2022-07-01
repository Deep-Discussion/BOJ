#정수 삼각형
#삼각형의 크기는 1이상 500이하. 
import sys
#입력받기
n = int(sys.stdin.readline());
triangle =[[0]*501 for i in range(n)];

for i in range (0, n):
    triangle[i] = list(map(int,(sys.stdin.readline().split())));


for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0 : triangle[i][j] += triangle[i-1][0];
        elif j == i : triangle[i][j] +=  triangle[i-1][j-1];
        else : triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]);


print(max(triangle[n-1]));