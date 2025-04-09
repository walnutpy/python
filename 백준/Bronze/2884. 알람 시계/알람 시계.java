
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner scan =new Scanner(System.in);
		int a =scan.nextInt();
		int b=scan.nextInt();
		

		if (b < 45) {
			int c = 45 - b;
			b = 60 - c;
			if (a > 0) {
				a = a-1;}
			else {a = 23;}}
		else {
			b = b - 45;
		}

		System.out.println(a + " " + b);
	}
}