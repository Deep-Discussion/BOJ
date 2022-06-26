package BOJ;
import java.util.*;

class BOJ_1260 {
    static int n,m,v;
    static int[][] connect = new int[1001][1001];
    static boolean[] checked = new boolean[1001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        n=sc.nextInt(); //정점의 개수 n개
        m=sc.nextInt(); //간선의 개수 m개
        v=sc.nextInt(); //시작점

        for(int i=0; i<m; i++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            connect[x][y]=1;
            connect[y][x]=1; 
        }

        dfs(v);
        //check초기화하고 bfs
        System.out.println();
        checked = new boolean[1001];
        bfs();
    }
    public static void dfs(int node){
        checked[node] = true;
        System.out.print(node+" ");
        
        for(int i=0; i<=n; i++){
            if(connect[node][i]==1 && checked[i]==false){
                dfs(i);
            }
        }
    }
    public static void bfs(){
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(v);
        checked[v]=true;
        System.out.print(v + " ");
        
        while(!queue.isEmpty()){
            int temp = queue.poll();
            for(int i=0; i<=n; i++){                
                if(connect[temp][i]==1 && checked[i] == false){
                    
                    queue.offer(i);
                    checked[i]=true;
                    System.out.print(i + " ");
                }
            }
        }

    }
}
