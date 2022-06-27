
import sys

N = int(sys.stdin.readline().rstrip());   #2<= N <=100동아리 방의개수
M = int(sys.stdin.readline().rstrip());   #종빈빌런의 행동횟수 0 <= M <=100

print(N, M);

def solution(N, M) :

    wall = [0] * (N + 1 );

    for i in range(M):
        x, y = map(int,(sys.stdin.readline().split()));

        for j in range(x, y):
            wall[j] = 1;

    return N - wall.count(1);


print(solution(N, M));

