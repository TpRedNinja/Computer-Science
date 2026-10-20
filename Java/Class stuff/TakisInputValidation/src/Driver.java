import java.util.Scanner;
public class Driver {

	public static void main(String[] args) {
		System.out.println("Welcome to taki eating simulator");
		
		int servings;
		Scanner s = new Scanner(System.in);
		
		System.out.println("Please enter the number of servings");
		servings = s.nextInt();
		
		while(servings < 0 || servings > 10)
		{
			if(servings < 10 || servings > 10)
			{
				System.out.println("Error: Please enter a positive number or less than 10");
			}
			System.out.println("Please enter the number of servings");
			servings = s.nextInt();
		}
		
		while(servings <= 9) {
			System.out.println("Munching on some taki's");
			servings++;
		}
		s.close();
	}

}
