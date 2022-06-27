package BOJ;
import java.util.*;

class BOJ_13699 {
    static long[] arr = new long[36];//0-35
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        calc();
        System.out.println(arr[n]);
    }
    public static void calc(){
        arr[0]=1;
        arr[1]=1;

        for(int i=2; i<36; i++){
            for(int j=0; j<=i-1; j++){
                arr[i]+=arr[j]*arr[i-j-1];
            }
        }
    }
}
