#BOJ_2667
#단지 번호 붙이기
import sys

n = int(sys.stdin.readline());
visit = [[False]*n for _ in range(n)]

mapp = []
dx = [-1, 1 ,0 ,0]; #동 서 남 북
dy = [0, 0, -1, 1];

for i in range (n):
    mapp.append(list(map(int,sys.stdin.readline().rstrip())));

count = 0;

def DFS(x, y, visit):
    global count;

    if (x < 0 or y < 0 or x >= n or y >= n or visit[x][y] == True): return 0;
    visit[x][y] = True;

    if mapp[x][y] == 1 :
        count+=1;
        for i in range (4):
            nx = x + dx[i];
            ny = y + dy[i];

            DFS(nx,ny,visit);
        return True;
    return False;



# 4방향으로 탐색한다음, 1이면 해당 단지에 +1
#BFS의 횟수 = 단지의 개수, 1의 개수 = 해당 bfs회차의 단지개수
#4방향 돌면서 1BFS마다 1의 개수를 센다


           #시작점과 graph를 보낸다.
m = 0;
answer = [];
for i in range(n):
    for j in range(n):
        count = 0;
        if DFS(i,j,visit) == True :
            m+=1;
            answer.append(count)
            count = 0;

print(m);
answer.sort();
for i in range(len(answer)):
    print(answer[i]);