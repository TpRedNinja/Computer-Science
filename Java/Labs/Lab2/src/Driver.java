import java.util.Scanner;

public class Driver {
	public static void main(String[] args) {
		// create student object
		Student student = new Student();
		
		// get user input
		Scanner Keyboard = new Scanner(System.in);
		System.out.println("What is your name? ");
		String name = Keyboard.nextLine();0
		System.out.println("What is your major? ");
		String major = Keyboard.nextLine();
		System.out.println("What is your student id? ");
		int id = Keyboard.nextInt();
		System.out.println("How many credits have you completed? ");
		int credits = Keyboard.nextInt();
		
		// use user input
		student.setName(name);
		student.setMajor(major);
		student.setId(id);
		student.setCredits(credits);
		
		// display student class info with getters
		System.out.println(); // new line from user input
		System.out.println("Displaying Student class info with getters");
		System.out.println("Student Name: " + student.getName());
		System.out.println("Student Major: " + student.getMajor());
		System.out.println("Student Id: " + student.getId());
		System.out.println("Student Credits: " + student.getCredits());
		
		// display student class info with toString method
		System.out.println(); // new line from displaying info with getter methods
		System.out.println("Display Student class with toString method");
		System.out.println(student.toString());
		

	}

}
