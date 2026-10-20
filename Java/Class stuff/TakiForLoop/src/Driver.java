import java.util.Scanner;
public class Driver {

	public static void main(String[] args) {
		System.out.println("Welcome to taki eating simulator");
		
		int servings, calories = 0;
		Scanner s = new Scanner(System.in);
		
		System.out.println("Please enter the number of servings");
		servings = s.nextInt();
		
		
		for(int i = 0; i < servings; i++) {
			System.out.println("Munching on some taki's");
			calories += 150;
		}
		
		System.out.println("You ate " + calories + " calories worth of taki's");
		s.close();
	}

}
