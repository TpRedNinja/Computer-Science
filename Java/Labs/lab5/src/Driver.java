import static java.lang.System.out;
import static java.lang.System.err;
import java.util.Scanner;

public class Driver {
	// global variable for the class
	static boolean isRunning = true;
	
	public static void displayMenu() {
		out.println("===== Please select a menu option from 1-4 =====\r\n"
				+ "1. Calculate the Surface Area of a Sphere\r\n"
				+ "2. Calculate the Surface Area of a Cone\r\n"
				+ "3. Calculate the Surface Area of a Rectangular Prism\r\n"
				+ "4. Quit\r");
	}
	
	//check if user input is valid
	public static boolean isValid(int thing, int numinputs) {
		int[] validInputs = new int[numinputs];
		//populate list with valid inputs
		for (int i = 0; i < validInputs.length; i++) {
			validInputs[i] = i+1;
		}
		
		// check list against user input
		for (int i = 0; i < validInputs.length; i++) {
			if(thing == validInputs[i])
				return true;
				
		}
		return false;
	}
	
	//check if the user input a negative and if so make it positive and return it
	public static double isNegative(double num) {
		if (num < 0)
			num = Math.abs(num);
		return num;
	}
	
	public static void SurfaceArea() {
		double len,height,breadth,raidus,surfaceArea;
		int choice;
		Scanner s = new Scanner(System.in);
		SurfaceArea sa = new SurfaceArea();
		while(isRunning) {
			out.println("This program will calculate the surface area for various shapes");
			do {
				displayMenu();
				choice = s.nextInt();
				if (!isValid(choice,4))
					err.println("Error: please enter a number from 1-4");
				
			}while(!isValid(choice,4));
			if (choice == 1) {
				out.println("Enter the raidus of the sphere");
				raidus = s.nextDouble(); // get user input
				raidus = isNegative(raidus); // if its negative convert to positive
				surfaceArea = sa.calSurfArea(raidus); //calculate surface area
				out.println("");
				out.printf("The Surface area of the sphere is %.1f units squared", surfaceArea);
				out.println("");
			} else if (choice == 2) {
				// get user input
				out.println("Enter the raidus of the cone");
				raidus = s.nextDouble(); 
				out.println("Enter the height of the cone");
				height = s.nextDouble();
				// if its negative convert to positive
				raidus = isNegative(raidus); 
				height = isNegative(height);
				surfaceArea = sa.calSurfArea(raidus,height); //calculate surface area
				out.println("");
				out.printf("The Surface area of the cone is %.1f units squared", surfaceArea);
				out.println("");
			} else if (choice == 3) {
				// get user input
				out.println("Enter the length of the rectangular prism");
				len = s.nextDouble(); 
				out.println("Enter the breadth of the rectangular prism");
				breadth = s.nextDouble();
				out.println("Enter the height of the rectangular prism");
				height = s.nextDouble();
				// if its negative convert to positive
				raidus = isNegative(len); 
				breadth = isNegative(breadth);
				height = isNegative(height);
				surfaceArea = sa.calSurfArea(len,height,breadth); //calculate surface area
				out.println("");
				out.printf("The Surface area of the rectangular prism is %.1f units squared", surfaceArea);
				out.println("");
			} else if (choice == 4) {
				out.println("");
				out.println("Good bye");
				isRunning = false;
			}
		}
		s.close();
	}
	
	public static void innerClasses() {
		out.println("This will demonstrate inner classes");
		Household hh1 = new Household("Bob", "1234 west avenue", "Westminster", "MD", "21797", 2006, "Bear", Household.Pet.species.DOG, Household.Pet.color.BLACK, false);
		Household hh2 = new Household();
		
		out.println("");
		out.println(hh1.toString());
		out.println("");
		out.println(hh2.toString());
	}
	

	public static void main(String[] args) {
		int choice;
		Scanner s = new Scanner(System.in);
		while (isRunning) {
			do {
				out.println("===== Please select a menu option from 1-2 =====\r\n"
						+ "1. Lab part 1\r\n"
						+ "2. Lab part 2\r\n");
				choice = s.nextInt();
				if(!isValid(choice, 2)) {
					err.println("Error: Invalid input");
				}
			}while(!isValid(choice, 2));
			
			switch(choice) {
			case 1:
				SurfaceArea();
				break;
			case 2:
				innerClasses();
				break;
			}
		}
		
	}

}
