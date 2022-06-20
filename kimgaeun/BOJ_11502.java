package kimgaeun;
import java.util.*;

class BOJ_11502{
    static int[] primes = new int[1001];
    static int[] cases;
    static int index = 0;
    // static int end=0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt(); //testcase개수
        cases = new int[t];
        
        for(int i=0; i<t; i++){
            cases[i] = sc.nextInt();
        }

        //소수구하기
        int n = 0;
        for (int i=2; i<=1000; i++) {
            for (int j=2; j<=i; j++){
                if(i%j==0){
                    n++;
                }
            }
            if(n==1){
                primes[index++] =i;
            }
            n=0;
        }

        // for(int j=0; j<index; j++){
        //     System.out.println(primes[j]);
        // }

        for(int i=0; i<t; i++){
            int cnt = 0;
            outer: for(int j=0; j<index; j++){
                for(int k=0; k<index; k++){
                    for(int l=0; l<index; l++){
                       if(primes[j]+primes[k]+primes[l] == cases[i]) {
                        cnt++;
                        System.out.println(primes[j]+" "+primes[k]+" "+ primes[l]);
                        break outer;
                        }
                    }
                }
            }
            if(cnt==0) System.out.println(0);
        }

        
        

    }
 

}