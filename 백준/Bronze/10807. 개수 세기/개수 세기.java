import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer tk=new StringTokenizer(br.readLine());
		int arr[]=new int[N];
		
		for (int i =0; i<N;i++) {
			arr[i]=Integer.parseInt(tk.nextToken());
		}
		
		int v=Integer.parseInt(br.readLine());
		int count =0;
		for(int i:arr) {
			if(i==v) count++;
		}
		System.out.println(count);
	}

}