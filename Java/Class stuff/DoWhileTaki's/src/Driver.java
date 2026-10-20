import java.util.Scanner;

public class Driver {

	public static void main(String[] args) {
		System.out.println("Welcome to taki eating simulator");
		
		int servings;
		
		Scanner s = new Scanner(System.in);
		
		do {
			System.out.println("Please enter the number of servings");
			servings = s.nextInt();
		}while(servings < 0 || servings > 9);
		
		while(servings <= 9 && servings > 0) {
			System.out.println("Munching on some taki's");
			servings--;
		}
		s.close();


	}

}
