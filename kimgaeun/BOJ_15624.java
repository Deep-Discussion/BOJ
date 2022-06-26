package BOJ;
import java.util.*;

class BOJ_15624 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] arr = new long[1000001];

        arr[0]=0;
        arr[1]=1;
        for(int i=2; i<=n; i++){
            arr[i]=0;
        }

        for(int i=2; i<=n; i++){
            arr[i]=(arr[i-1]+arr[i-2])%1000000007;
        }

        System.out.println(arr[n]);

    }
}
