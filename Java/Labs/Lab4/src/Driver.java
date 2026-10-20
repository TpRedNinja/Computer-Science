import java.util.Random;
import java.util.Scanner;
import static java.lang.System.out;

public class Driver {
	public static void main(String[] args) {
		// define variables
		int flips, guess, score = 0;
		
		//define scanner object
		Scanner s = new Scanner(System.in);
		//define random object
		Random r = new Random();
		
		// display purpose of program to user
		out.println("This program will simulate a coin toss.");
		
		//input validation
		do {
			out.println("How many times would you like to try and guess a coin flip?");
			flips = s.nextInt();
			if (flips < 0) {
				out.println("Error: Please enter a positive number.");
			}
		}while(flips < 0);
		
		// flips
		for (int i = 0; i < flips; i++) {
			out.println("Flipped coined");
			int coin = r.nextInt(2);
			
			// input validation part 2 boo-ga-loo
			do {
				out.println("Enter 1 for heads and 0 for tails");
				guess = s.nextInt();
				if (guess != 0 && guess != 1) {
					out.println("Error: Please enter 1 or 0");
				}
			}while(guess != 0 && guess != 1);
			
			//check guess 
			if (guess == coin) {
				out.println("Good job thats right");
				score++;
			} else {
				String answer;
				if(coin == 1) {
					answer = "heads";
				} else {
					answer = "tails";
				}
				out.println("Nope sorry the correct answer is " + answer);
			}
		}
		
		out.println("You got " + score + " correct out of " + flips);
		
	}
}
