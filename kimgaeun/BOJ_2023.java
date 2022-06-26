package BOJ;
import java.util.*;

class BOJ_2023 {
    static int n;
    static String s = new String();
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt(); //입력받을 자리수
   
        number(2, 1);
        number(3, 1);
        number(5, 1);
        number(7, 1);

        System.out.println(sb.toString());
    }

    public static void number(int num, int len){
        if(len == n){
            sb.append(num).append('\n');
            return;
        }

        for(int i=1; i<=9; i++){
           int a = num*10+i;
           if(isPrime(a)) number(a, len+1);
           else continue;
        }

    }

    public static boolean isPrime(int num){
        for (int i=2; i*i<=num; i++) {
            if(num%i==0){
               return false;
            }
        }
        return true;
    }
}
