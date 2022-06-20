package kimgaeun;
import java.util.*;

class BOJ_14719{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt(); //세로길이
        int w = sc.nextInt(); //가로길이
        int[] blocks = new int[w];
        for(int i=0; i<w; i++){ //블록 개수 입력
            blocks[i] = sc.nextInt();
        }

        int[] left = new int[w]; 
        int[] right = new int[w]; 
        int count = 0; //빗물 count

         //빗물은 좌우 차이가 존재해야 담을 수 있음.
        //왼쪽에서 부터의 블록의 max값 - 오른쪽으로부터의 블록의 max값 중 min값을 구하기

        left[0] = blocks[0]; //leftMax값
        for(int i=1; i<w; i++){ 
            left[i] = Math.max(blocks[i],left[i-1]);
        }

        
        right[w-1] = blocks[w-1]; //rightMax값
        for(int i=w-2; i>=0; i--){
            right[i] = Math.max(blocks[i],right[i+1]);
        }

        
        for(int i=0; i<w; i++){ //count값
            count += Math.min(left[i],right[i])-blocks[i];
        }

        System.out.println(count);
       
    }

}