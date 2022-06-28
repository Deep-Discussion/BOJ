#BOJ_15970 
#점들은 N개의 색깔을 가진다.
#1부터 N까지의 수로 표시한다.

#점들의 순서쌍 (위치, 색깔)
#화살표길이의 합

import sys

#입력받기
n = int(sys.stdin.readline().rstrip());
dots = [[] for i in range(n)];

#색깔로 받기
for i in range(n):
    x, y = map(int,(sys.stdin.readline().rstrip().split()));
    dots[y-1].append(x);

hap = 0;

for i in range(n):
    temp = sorted(dots[i]);
    for i in range(len(temp)):
        if i ==0 :
            hap += temp[i+1] - temp[i];
        elif i == len(temp) - 1 :
            hap += temp[i] - temp[i-1];
        else : 
            hap += min(temp[i+1]-temp[i], temp[i]- temp[i-1])

print(hap);






