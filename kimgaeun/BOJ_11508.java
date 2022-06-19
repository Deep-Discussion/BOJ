package kimgaeun;
import java.util.*;

class BOJ_11508 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++){
            int x = sc.nextInt();
            arr.add(x);  
        }
       
        Collections.sort(arr, Collections.reverseOrder()); //내림차순 정렬

        //비싼순으로 3개씩 사고 3번째꺼는 할인받는게 이득

        int sum =0;
        for(int i=0; i<arr.size(); i++){
            if((i+1)%3==0) continue;
            sum += arr.get(i);
        }
       
        System.out.println(sum);
    }
    
}
