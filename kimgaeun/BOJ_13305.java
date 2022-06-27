package kimgaeun;
import java.util.*;;
class BOJ_13305 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt(); //도시 개수
        int []distances = new int[N-1];
        int []prices = new int[N];
        int min = Integer.MAX_VALUE;
        long total = 0;

        for(int i=0; i<N-1; i++){
            distances[i] = sc.nextInt();
        }
        for(int i=0; i<N; i++){
            int x = sc.nextInt();
            min = Math.min(x, min);
            prices[i] = x;
        }

        /*
            비용계산
            1. 맨처음에는 무조건 비용내야함.
            2. min나오면 그때부터 나머지 비용 계산 
            3. 마지막 서브태스크때문에 total과 cost는 long을 써야함!      
        */
        
        long cost = prices[0];
        for(int i=0; i<N-1; i++){
            if(cost>prices[i]) cost = prices[i];
            total += cost*distances[i];
        }

        System.out.println(total);
    }
}
