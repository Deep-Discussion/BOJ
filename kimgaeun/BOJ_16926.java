package kimgaeun;
import java.util.*;

class BOJ_16926 {
    static int n,m,r;
    static int[][] arr;
    static int[][] temp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        r = sc.nextInt();
        arr = new int[n][m];
        temp = new int[n][m];

        //입력
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr[i][j]=sc.nextInt();
            }
        }

        int number = Math.min(n, m)/2;

        for(int i=0; i<r; i++){//r번만큼 돌림
            for(int j=0; j<number; j++){ //돌릴 그룹 수
               int start = arr[j][j]; //시작점(0,0/1,1)
               for(int k=j+1; k<m-j; k++){ //윗줄
                arr[j][k-1] = arr[j][k];
               }
               for(int k=j+1; k<n-j; k++){ //오른쪽
                arr[k-1][m-j-1] = arr[k][m-j-1];
               }
               for(int k=m-j-2; k>=j; k--){ //아랫줄
                arr[n-j-1][k+1] = arr[n-j-1][k];
               }
               for(int k=n-j-2; k>=j; k--){ //왼쪽
                arr[k+1][j] = arr[k][j];
               }
               arr[j+1][j] = start;
            }
        }


        //출력
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }

    }

   
}
