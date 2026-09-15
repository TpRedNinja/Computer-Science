import java.util.Scanner;

public class ClassExample1 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int num;
		boolean isValid = false;
		/*while(!isValid) {
			try {
				System.out.print("Please input a number: ");
				num = keyboard.nextInt();
				isValid = true;
			}catch(Exception e) {
				System.out.println("error you did not enter a number");
				keyboard.next();
				num = keyboard.nextInt();
			}
		}*/
		System.out.print("Please input a number: ");
		num = keyboard.nextInt();
		
		keyboard.nextLine();
		
		System.out.println("Please input a name");
		String name = keyboard.nextLine(); 
		
		System.out.println("Graduating class of " + num + ": Validictorian is " + name);
	}

}
