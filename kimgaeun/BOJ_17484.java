package kimgaeun;
import java.util.*;

class BOJ_17484{
    static int n,m;
    static int[][] grid;
    static int[] dir={-1,0,1};
    static int[] visited;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        grid= new int[n][m];
        visited = new int[n];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                grid[i][j] = sc.nextInt();
            }
        }

        for(int i=0; i<m; i++){
            visited[0] = i;
            dfs(1,i,3);
        }

        System.out.println(min);
    }
    public static void dfs(int depth, int cur, int d){
        if(depth == n){ //깊이가 같으면
            int sum = grid[0][visited[0]];
            for(int i=1; i<n; i++){
                sum+= grid[i][visited[i]];
            }
            if(min>sum)
                min = sum;
            
            return;
        }//끝남

        for(int i=0; i<3; i++){
            int next=dir[i]+cur;
            if(next< 0 || next>=m) continue;
            if(d != dir[i]){
                visited[depth]=next;
                dfs(depth+1, next, dir[i]);
            }
        }

    }
    
}
