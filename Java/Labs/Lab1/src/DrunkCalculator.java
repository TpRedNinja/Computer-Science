/**********************************************************************
* This program will do some calculations on if you will make the dunk *
* for CIS-132														  *
* By Harris Domangue 												  *
***********************************************************************/

//imports
import static java.lang.System.out;   // import system.out
import java.util.Scanner; // import scanner object

// This class will do some calculations for a dunk
public class DrunkCalculator {

	public static void main(String[] args) {
		// declare variables
		double bodyMass, height; // declaration of body mass and height variables
		String name; // declare name variable
		Scanner keyboard = new Scanner(System.in);
		
		// get user input and assign them to variables
		out.println("What is your height in feet?: ");
		height = keyboard.nextDouble();
		keyboard.nextLine();
		out.println("What is your bodymass in pounds?: ");
		bodyMass = keyboard.nextDouble();
		keyboard.nextLine();
		out.println("What is your name?: ");
		name = keyboard.nextLine();
		
		// define more variables
		final double GRAVITY = 32.174; // this contains the constant gravitational force
		double mLeapHeight = 10-height*1.3; // this stores the minimum leap height
		double jumpEnergy = bodyMass * GRAVITY * mLeapHeight; // this stores the jump energy
		double iJumpSpeed = Math.sqrt(2 * GRAVITY * mLeapHeight); // this store the initial jumping speed 
		double hangTime = Math.sqrt(8 * mLeapHeight/GRAVITY); // this stores the hang time
		
		// display variables to user in a neat format
		out.printf("Hi there %s", name);
		out.printf("\nThe minimum leap height required is: %.2f ft.", mLeapHeight);
		out.printf("\nThe jump energy required is: %.2f ft-lbs.", jumpEnergy);
		out.printf("\nThe initial jumping speed required is: %.2f ft/sec.", iJumpSpeed);
		out.printf("\nThe hang time required is: %.2f secs.", hangTime);
	}

}
