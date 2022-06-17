package kimgaeun;
import java.util.*;

class BOJ_16206{
    static int num;
	static int max;
	static int count = 0;
	
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        num = sc.nextInt();
        max = sc.nextInt();
		int cakes[] = new int[num];
		int rest[] = new int[num];
		int index = 0;
		
		for (int i=0; i<num; i++) {
			int len = sc.nextInt();
			cakes[i] = len;
		}

		Arrays.sort(cakes);		
		
		for(int i=0; i<num; i++) {
			if(cakes[i] == 10) count++;
			else if(cakes[i] > 10) {
				 if(cakes[i] % 10 == 0)
					 cut(cakes[i]);
				 else rest[index++] = cakes[i];
			}
		}
		
		if(max > 0)
			for(int i=0; i<index; i++) cut(rest[i]);
		
		System.out.println(count);
	}
	
	private static void cut(int len) {
		if(max <= 0) return;
		else {
			count++;
			max--;
			int length = len - 10;
			if(length > 10) {
				cut(length);
			}
			else {
				if(length == 10) count++;
				return;
			}
		}
	}
}