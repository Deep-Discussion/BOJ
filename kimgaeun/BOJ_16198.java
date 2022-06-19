package kimgaeun;
import java.util.*;

class BOJ_16198 {
    static ArrayList<Integer> marbles = new ArrayList<>();
    static int n;
    static int energy = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        

        for(int i=0; i<n; i++){
            int x=sc.nextInt();
            marbles.add(x);
        }

        dfs(n, marbles, 0);
        System.out.println(energy);


    }
    public static void dfs(int n, ArrayList<Integer> marbles, int sum){
        
        if(n == 2){
            energy = Math.max(energy,sum);
            return;
        }
        
        for(int i=1; i<n-1; i++){
            
            int mul = marbles.get(i-1)*marbles.get(i+1);
            int cur = marbles.get(i);
            // System.out.println("i "+cur+" sum " + sum);
            marbles.remove(i);
            
            dfs(n-1, marbles, sum+mul);
            marbles.add(i, cur);
        }

    }
}
