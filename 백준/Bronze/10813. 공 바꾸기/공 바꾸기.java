import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan=new Scanner(System.in);
		
		int n = scan.nextInt();
		int m = scan.nextInt();
		int arr[] = new int[n];
		for(int i=1;i<n+1;i++) {
			arr[i-1]=i;
		}
		
		for(int k=0;k<m;k++) {
			int i=scan.nextInt();
			int j =scan.nextInt();
			int temp = arr[i-1];
			arr[i-1] = arr[j-1];
			arr[j-1] = temp;
		}
		for(int i =0;i<n;i++) {
			System.out.print(arr[i]+" ");
		}
		scan.close();
	}

}
