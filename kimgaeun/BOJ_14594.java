package BOJ;
import java.util.*;

class BOJ_14594 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N,M;
        N = sc.nextInt();
        M = sc.nextInt();
        int []arr = new int[N-1];

        for(int i=0; i<N-1; i++){
            arr[i]=0;
        }

        for(int i=0; i<M; i++){
            int x,y;
            x = sc.nextInt();
            y = sc.nextInt();

            for(int j=x-1; j<y-1; j++){
                arr[j]=1;
            }
        }

        int cnt=0;
        for(int i=0; i<N-1; i++){
            if(arr[i]==0) cnt++;
        }

        System.out.println(cnt+1);
    }

}
