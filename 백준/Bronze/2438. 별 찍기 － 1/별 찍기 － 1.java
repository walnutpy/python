
import java.awt.print.Printable;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner =new Scanner(System.in);
		
		int n =scanner.nextInt();
		
		for (int i=1;i<n+1;i++) {
			for (int j=1;j<i+1;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}

}
