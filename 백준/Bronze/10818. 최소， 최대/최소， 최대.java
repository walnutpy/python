import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n =Integer.parseInt(br.readLine());
		int[] arr=new int[n];
		StringTokenizer tk =new StringTokenizer(br.readLine(), " ");
		for(int i= 0;i<n;i++) {
			arr[i] = Integer.parseInt(tk.nextToken());
		}
		int min_num = 1000000;
		int max_num = -1000000;
		for(int i =0; i< n; i++) {
			if (arr[i]<min_num) min_num = arr[i];
			if (arr[i] > max_num) max_num = arr[i];
		}
		System.out.println(min_num+" "+max_num);
	}

}