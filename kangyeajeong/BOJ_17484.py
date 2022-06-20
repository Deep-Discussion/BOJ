
N,M = list(map(int,(input().split())) );
ydir =[-1, 0 , 1];
min = 10000000000000000000000;
def dfs(depth, y, dir):
    if(depth == N):
        sums = trip[0][visited[0]];
        for i in range(N):
            sum+= trip[i][visited[i]];
        
        min =  sums if (min > sums) else min;
        return ;

    for i in range (3):
        dy = y + ydir[i];
        if(isValidPosition(dy) & dir != i) :
            visited[depth] = dy;
            dfs(depth+1, dy, i);


def isValidPosition(y):
    if(y < 0 | y >=  M) :
        return False;
    return True;



trip = [[0 for col in range(M)] for row in range(N)] 
visited = [[0 for col in range(M)] for row in range(N)] 


#trip에 값 복사
for i in range (N) :
    line = list(map(int,(input().split())) );
    trip[i] = line ;
    

for i in range(M):
    visited[0] = i;
    dfs(1, i , -1);

print(min);